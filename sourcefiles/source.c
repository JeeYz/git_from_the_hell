#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define d 4 // d = capacity order

typedef struct rec
{
	char name[100];  // 여기에는 각 줄의 첫 단어
	char pos[10];    // 이 단어의 가능한 품사 중 첫번째 품사.
} type_rec;

typedef struct node *nodeptr;
typedef struct node
{
	int fill_cnt;
	type_rec ele[2 * d];
	nodeptr ptr[2 * d + 1];
} node;

typedef struct big_node
{
	type_rec ele[2 * d + 1];
	nodeptr ptr[2 * d + 2];
} big_node;

int B_tree_Insertion(type_rec in_rec, nodeptr *root);
int B_tree_Search(char word[100], nodeptr *root);
int B_tree_Deletion(char word[100], nodeptr *root);
int B_tree_Sequential_print(nodeptr root);

int main()
{
	FILE *fp;
	errno_t errno;
	int i, k;

	char input[300];
	char name[100];
	char pos[10];
	char input_ch;
	char command[30], command2[100];

	struct rec rec, in_rec;
	struct node node;
	nodeptr root = NULL;

	errno = fopen_s(&fp, "wordlist.txt", "r");
	if (errno != 0)
	{
		printf("File Error!");
		return;
	}	// 파일 에러 나게 될 시 출력

	while ((fgets(input, sizeof(input), fp) != NULL))
	{
		fgets(input, sizeof(input), fp);

		// 비어있는 줄이나 문자로 시작하지 않는 줄은 다음 줄로 넘긴다.
		if (input[0] < 65 || (90 < input[0] && input[0] < 97) || 122 < input[0])
		{
			continue;
		}

		// name을 받고, name이 끝나는 지점을 찾는 과정
		for (i = 0; input[i] != ' '; i++)
		{
			rec.name[i] = input[i];
		}
		rec.name[i] = NULL;

		// 숫자 시작하는 지점을 찾는 과정 정하는 과정, 현재 i : name 끝나는 지점
		for (input_ch = input[i]; !(atoi(&input_ch) != 0 || input_ch == '0'); ++i, input_ch = input[i]) {}

		// pos가 시작하는 지점을 찾는 과정, 현재 i : 숫자 시작하는 지점
		for (input_ch = input[i]; input_ch < 65 || (90 < input_ch && input_ch < 97) || 122 < input_ch; ++i, input_ch = input[i]) {}

		// pos를 받는 과정, 현재 i : pos 시작하는 지점
		for (k = 0, input_ch = input[i]; (64 < input_ch && input_ch < 91) || (96 < input_ch && input_ch < 123); ++i, ++k, input_ch = input[i])
		{
			rec.pos[k] = input[i];
		}
		rec.pos[k] = NULL;

		B_tree_Insertion(rec, &root);
	}
	fclose(fp);

	do
	{
		printf("Command? ");
		scanf_s("%s", &command, sizeof(command));

		if (strcmp(command, "insert") == 0)
		{
			scanf_s("%s", &command2, sizeof(command2));
			strcpy_s(in_rec.name, sizeof(in_rec.name), command2);
			in_rec.pos[0] = NULL; // 안되면 고치기
			B_tree_Insertion(in_rec, &root);
		}
		else if (strcmp(command, "retrieve") == 0)
		{
			scanf_s("%s", &command2, sizeof(command2));
			B_tree_Search(command2, &root);
		}
		else if (strcmp(command, "delete") == 0)
		{
			scanf_s("%s", &command2, sizeof(command2));
			B_tree_Deletion(command2, &root);
		}
		else if (strcmp(command, "seqprint") == 0)
		{
			errno = fopen_s(&fp, "SeqData.txt", "w");
			if (errno != 0)
			{
				printf("File Error!");
				return;
			}	// 파일 에러 나게 될 시 출력
			fclose(fp);
			// seqprint 명령을 여러번 반복했을 때 파일내용이 계속 반복되지 않게 함
			B_tree_Sequential_print(root);
		}
		else if (strcmp(command, "exit") == 0)
		{
			return;
		}
		else
		{
			printf("잘못된 명령어 입력.\n");
		}
	} while (1);

	scanf_s("%d", &i, sizeof(i));	// 콘솔창이 바로 꺼지는 것을 막기 위함
	return 0;
}


int B_tree_Insertion(type_rec in_rec, nodeptr *root)
{
	char in_key[100];
	int a, i;
	int found, finished;
	nodeptr curr, parent, child, new_ptr, tptr = NULL;
	nodeptr now, now_child, find = NULL;
	big_node bnode;

	strcpy_s(in_key, sizeof(in_key), in_rec.name);

	if (!(*root))
	{
		*root = (nodeptr)malloc(sizeof(node));
		(*root)->ele[0] = in_rec;
		(*root)->ptr[0] = (*root)->ptr[1] = NULL;
		(*root)->fill_cnt = 1;
		return 0;
	}

	curr = *root;
	parent = curr;
	finished = 0;

	do
	{
		for (i = 0; i < curr->fill_cnt; i++)
		{
			if (strcmp(in_key, curr->ele[i].name) < 0) break;
			else if (strcmp(in_key, curr->ele[i].name) == 0) // 중복된 레코드가 있다면 종료
			{
				return 0;
			}
		}
		child = curr->ptr[i];
		if (child)	// 자식이 있다면 (리프노드가 아니라면) 반복
		{
			parent = curr;
			curr = child;
		}
		else	// 자식이 없다면 (리프노드라면) 반복 끝
		{
			finished = 1;
		}
	} while (!finished);	// 레코드가 들어갈 자리 찾음 (curr : 리프노드)

	do
	{
		strcpy_s(in_key, sizeof(in_key), in_rec.name);

		if (curr->fill_cnt < 2 * d)	// curr의 레코드 수가 2d 미만이면 여기에 정렬
		{
			for (i = 0; i < curr->fill_cnt; i++)
			{
				if (strcmp(in_key, curr->ele[i].name) < 0) break;	// i : 레코드가 들어갈 자리
			}
			for (a = curr->fill_cnt; i < a; a--)
			{
				curr->ele[a] = curr->ele[a - 1];
				curr->ptr[a + 1] = curr->ptr[a];
			}
			curr->ele[i] = in_rec;	// 제 자리에 레코드 삽입
			curr->ptr[i + 1] = child; // 제 위치에 포인트 삽입
			(curr->fill_cnt)++;
			return 0;
		}

		for (i = 0; i < 2 * d; i++)	// curr의 레코드 수가 2d면 bnode 만들어서 정렬
		{
			if (strcmp(in_key, curr->ele[i].name) < 0) break;	// i : 레코드가 들어갈 자리
		}

		bnode.ptr[0] = curr->ptr[0];
		for (a = 0; a < i; a++)
		{
			bnode.ele[a] = curr->ele[a];
			bnode.ptr[a + 1] = curr->ptr[a + 1];
		}	// bnode에 i 앞부분 삽입

		bnode.ele[i] = in_rec;	// bnode의 i에 레코드 삽입
		bnode.ptr[i + 1] = child;	// bnode의 i+1에 포인터 삽입

		for (a = i + 1; a <= 2 * d; a++)
		{
			bnode.ele[a] = curr->ele[a - 1];
			bnode.ptr[a + 1] = curr->ptr[a];
		}	// bnode에 i 뒷부분 삽입

		for (i = 0; i < d; i++)
		{
			curr->ele[i] = bnode.ele[i];
			curr->ptr[i] = bnode.ptr[i];
		}
		curr->ptr[i] = bnode.ptr[i];
		for (i = curr->fill_cnt; d < i; i--)
		{
			curr->ptr[i] = NULL;
		}
		curr->fill_cnt = d;
		// curr에 bnode의 앞부분 삽입 (가운데 레코드의 앞부분)

		new_ptr = (nodeptr)malloc(sizeof(node));

		for (i = 0; i < d; i++)
		{
			new_ptr->ele[i] = bnode.ele[i + d + 1];
			new_ptr->ptr[i] = bnode.ptr[i + d + 1];
		}
		new_ptr->ptr[i] = bnode.ptr[2 * d + 1];
		new_ptr->fill_cnt = d;
		// new_ptr에 bnode의 뒷부분 삽입 (가운데 레코드의 뒷부분)

		in_rec = bnode.ele[d];	// bnode의 중간 레코드를 in_rec로 둠
		child = new_ptr;	// new_ptr을 child로 둠

		if (curr == *root)	// curr이 root일 때, tptr로 새로운 root 생성 후 종료
		{
			tptr = (nodeptr)malloc(sizeof(node));
			tptr->ele[0] = in_rec; // tptr->ele[0] = bnode.ele[d];
			tptr->ptr[0] = curr; 
			tptr->ptr[1] = child;
			tptr->fill_cnt = 1;
			*root = tptr;

			return 0;
		}

		find = parent;	// find(찾을 노드) = 부모노드
		now = *root;	// now를 root로 두고 찾기 시작
		parent = now;
		found = 0;

		do
		{
			for (i = 0; i < now->fill_cnt; i++)
			{
				if (strcmp(find->ele[0].name, now->ele[i].name) < 0) break;
				else if (strcmp(find->ele[0].name, now->ele[i].name) == 0)	// find 값 찾으면 found=1
				{
					found = 1;
				}
			}
			if (found == 0)	// find 값을 찾지 못했을 때, now_child 값 설정 후 반복
			{
				now_child = now->ptr[i];
				parent = now;
				now = now_child;
			}
		} while (!found);
		curr = now;	// curr = now(원래 부모노드)로 두고 반복

	} while (1);
}

int B_tree_Search(char word[100], nodeptr *root)
{
	char find_key[100];
	int i, level, found;
	nodeptr curr = NULL;

	strcpy_s(find_key, sizeof(find_key), word);
	level = 1;
	found = 0;
	curr = *root;

	do
	{
		for (i = 0; i <= curr->fill_cnt; i++)
		{
			if (strcmp(find_key, curr->ele[i].name) < 0) break;
			else if (strcmp(find_key, curr->ele[i].name) == 0)
			{
				found = 1; break; // 찾았으면 for 반복문 종료 (i : 노드 안에서 레코드의 위치)
			}
		}
		if (found == 1) break; // 찾았으면 do 반복문 종료
		else // 못 찾았으면
		{
			if (curr->ptr[i])	// 자식 노드가 있다면, level 증가 후 반복
			{
				level++;
				curr = curr->ptr[i];
			}
			else
			{
				printf("없는 레코드입니다.\n");
				return 0;
			}
		}
	} while (1); // 레코드의 위치 찾음 (curr->ele[i])

	printf("레코드의 레벨 : %d, 노드 안에서 레코드의 위치 : %d\n", level, (i+1));
	return 0;
}

int B_tree_Deletion(char word[100], nodeptr *root)
{
	char out_key[100];
	int a, i, found;
	nodeptr curr, right, left, parent, leaf = NULL;

	strcpy_s(out_key, sizeof(out_key), word);
	
	curr = *root;
	parent = curr;
	found = 0;

	do
	{
		for (i = 0; i < curr->fill_cnt; i++)
		{
			if (strcmp(out_key, curr->ele[i].name) < 0) break;
			else if (strcmp(out_key, curr->ele[i].name) == 0)
			{
				found = 1; break; // 찾았으면 for 반복문 종료
			}
		}
		if (found == 1) break; // 찾았으면 do 반복문 종료
		else // 못 찾았을 때
		{
			if (curr->ptr[i]) // 자식이 있다면 반복
			{
				parent = curr;
				curr = curr->ptr[i];
			}
			else // 자식이 없다면 없는 레코드
			{
				printf("없는 레코드입니다.\n");
				return 0;
			}
		}
	} while (1); // 노드 위치 찾음 (curr->ele[i])

	if (!(curr->ptr[i]))	// curr이 리프노드일 경우 바로 삭제 완료.
	{
		for (a = i; a < (curr->fill_cnt - 1); a++)
		{
			curr->ele[a] = curr->ele[a + 1];
		}
		(curr->fill_cnt)--;
		leaf = curr;
	}
	else // 리프노드가 아니라면, 레코드와 바꿀 리프 레코드(leaf record) 찾음
	{
		leaf = curr->ptr[i + 1];	// 원래 노드의 오른쪽 자식 노드로 이동 후
		while (leaf->ptr[i])
		{
			leaf = leaf->ptr[0];
		}	// 리프노드일 때까지, 가장 왼쪽 자식 노드로 이동

		curr->ele[i] = leaf->ele[0]; // 지우려는 레코드와 리프 레코드를 바꿈

		for (a = 0; a < leaf->fill_cnt - 1; a++)
		{
			leaf->ele[a] = leaf->ele[a + 1];
		}
		(leaf->fill_cnt)--;
	} // 지우려는 레코드와 리프 레코드와 바꾼 후 삭제

	if (leaf->fill_cnt >= d)
	{
		printf("삭제 완료.\n");
		return 0;
	}	// 리프노드 삭제한 후 레코드 개수가 d개 이상이면 삭제 완료.

	// 리프노드 삭제한 후 레코드 개수가 d개 미만일 때
	// left : curr의 왼쪽 노드, right : curr의 오른쪽 노드
	do
	{
		if (parent == leaf)
		{
			return;
		}	// curr이 리프노드면 종료.

		if (i == 0)
		{
			left = NULL;
			right = parent->ptr[i + 1];
		}
		else if (i == (parent->fill_cnt - 1))
		{
			left = parent->ptr[i - 1];
			right = NULL;
		}
		else
		{
			left = parent->ptr[i - 1];
			right = parent->ptr[i + 1];
		}

		if (right->fill_cnt > d) // right의 레코드 수가 d 이상이면 분배
		{
			leaf->ele[d - 1] = parent->ele[i];
			parent->ele[i] = right->ele[0];
			for (a = 0; a < (right->fill_cnt - 1); a++)
			{
				right->ele[a] = right->ele[a + 1];
			}
			(leaf->fill_cnt)++;
			(right->fill_cnt)--;
			printf("삭제 완료.\n");
			return 0;
		}
		else if (left->fill_cnt > d) // right의 레코드 수가 d개이고, left의 레코드 수가 d 이상이면 분배
		{
			for (a = d - 1; 0 < a; a--)
			{
				leaf->ele[a] = leaf->ele[a - 1];
			}
			leaf->ele[0] = parent->ele[i - 1];
			parent->ele[i - 1] = left->ele[left->fill_cnt - 1];
			(leaf->fill_cnt)++;
			(left->fill_cnt)--;
			printf("삭제 완료.\n");
			return 0;
		}

		// left와 right의 레코드 수가 d개일 때
		if (right) // right가 존재할 때
		{
			leaf->ele[d - 1] = parent->ele[i];
			for (a = d; a < 2 * d; a++)
			{
				leaf->ele[a] = right->ele[a - d];
			}
			for (a = i; a < parent->fill_cnt; a++)
			{
				parent->ele[a] = parent->ele[a + 1];
				parent->ptr[a + 1] = parent->ptr[a + 2];
			}
			parent->ptr[a + 1] = NULL;
			(leaf->fill_cnt) = 2 * d;
			(parent->fill_cnt)--;

			if (parent->fill_cnt >= d)
			{
				printf("삭제 완료.\n");
				return 0;
			}
		}
		else if (left) // 맨 오른쪽 노드일 때 (right가 존재하지 않을 때)
		{
			left->ele[d] = parent->ele[i - 1];
			for (a = d + 1; a < 2 * d; a++)
			{
				left->ele[a] = leaf->ele[a - d - 1];
			}
			parent->ptr[i] = NULL;
			(left->fill_cnt) = 2 * d;
			(parent->fill_cnt)--;
			if (parent->fill_cnt >= d)	// 부모노드의 레코드 수가 d개 이상이면 삭제 완료.
			{
				printf("삭제 완료.\n");
				return 0;
			}
		}

		// 부모노드의 레코드 수가 d개 미만일 때
		leaf = parent;
		curr = *root;
		parent = curr;
		found = 0;

		do
		{
			for (i = 0; i < curr->fill_cnt; i++)
			{
				if (strcmp(leaf->ele[0].name, curr->ele[i].name) < 0) break;
				else if (strcmp(leaf->ele[0].name, curr->ele[i].name) == 0)
				{
					found = 1; break; // 찾았으면 for 반복문 종료
				}
			}
			if (found == 1) break; // 찾았으면 do 반복문 종료
			parent = curr;
			curr = curr->ptr[i];
		} while (1); // curr(원래 부모노드)과 그의 parent를 찾을 때까지 반복
		leaf = curr; // leaf = curr(원래 부모노드)로 두고 반복
	} while (1);
}

int B_tree_Sequential_print(nodeptr root)
{
	FILE *fq;
	errno_t errno;
	int i;

	errno = fopen_s(&fq, "SeqData.txt", "a");
	if (errno != 0)
	{
		printf("File Error!");
		return 0;
	}	// 파일 에러 나게 될 시 출력

	if (root->ptr[0])
	{
		for (i = 0; i < root->fill_cnt; i++)
		{
			fclose(fq);
			B_tree_Sequential_print(root->ptr[i]);

			errno = fopen_s(&fq, "SeqData.txt", "a");
			if (errno != 0)
			{
				printf("File Error!");
				return 0;
			}	// 파일 에러 나게 될 시 출력

			fputs(root->ele[i].name, fq);
			fputs(" ", fq);
			fputs(root->ele[i].pos, fq);
			fputs("\n", fq);
		}
		fclose(fq);
		B_tree_Sequential_print(root->ptr[i]);
	}
	else
	{
		for (i = 0; i < root->fill_cnt; i++)
		{
			fputs(root->ele[i].name, fq);
			fputs(" ", fq);
			fputs(root->ele[i].pos, fq);
			fputs("\n", fq);
		}
		fclose(fq);
	}
	return 0;
}
