#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define d 4 // d = capacity order

typedef struct rec
{
	char name[100];  // ���⿡�� �� ���� ù �ܾ�
	char pos[10];    // �� �ܾ��� ������ ǰ�� �� ù��° ǰ��.
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
	}	// ���� ���� ���� �� �� ���

	while ((fgets(input, sizeof(input), fp) != NULL))
	{
		fgets(input, sizeof(input), fp);

		// ����ִ� ���̳� ���ڷ� �������� �ʴ� ���� ���� �ٷ� �ѱ��.
		if (input[0] < 65 || (90 < input[0] && input[0] < 97) || 122 < input[0])
		{
			continue;
		}

		// name�� �ް�, name�� ������ ������ ã�� ����
		for (i = 0; input[i] != ' '; i++)
		{
			rec.name[i] = input[i];
		}
		rec.name[i] = NULL;

		// ���� �����ϴ� ������ ã�� ���� ���ϴ� ����, ���� i : name ������ ����
		for (input_ch = input[i]; !(atoi(&input_ch) != 0 || input_ch == '0'); ++i, input_ch = input[i]) {}

		// pos�� �����ϴ� ������ ã�� ����, ���� i : ���� �����ϴ� ����
		for (input_ch = input[i]; input_ch < 65 || (90 < input_ch && input_ch < 97) || 122 < input_ch; ++i, input_ch = input[i]) {}

		// pos�� �޴� ����, ���� i : pos �����ϴ� ����
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
			in_rec.pos[0] = NULL; // �ȵǸ� ��ġ��
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
			}	// ���� ���� ���� �� �� ���
			fclose(fp);
			// seqprint ����� ������ �ݺ����� �� ���ϳ����� ��� �ݺ����� �ʰ� ��
			B_tree_Sequential_print(root);
		}
		else if (strcmp(command, "exit") == 0)
		{
			return;
		}
		else
		{
			printf("�߸��� ��ɾ� �Է�.\n");
		}
	} while (1);

	scanf_s("%d", &i, sizeof(i));	// �ܼ�â�� �ٷ� ������ ���� ���� ����
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
			else if (strcmp(in_key, curr->ele[i].name) == 0) // �ߺ��� ���ڵ尡 �ִٸ� ����
			{
				return 0;
			}
		}
		child = curr->ptr[i];
		if (child)	// �ڽ��� �ִٸ� (������尡 �ƴ϶��) �ݺ�
		{
			parent = curr;
			curr = child;
		}
		else	// �ڽ��� ���ٸ� (���������) �ݺ� ��
		{
			finished = 1;
		}
	} while (!finished);	// ���ڵ尡 �� �ڸ� ã�� (curr : �������)

	do
	{
		strcpy_s(in_key, sizeof(in_key), in_rec.name);

		if (curr->fill_cnt < 2 * d)	// curr�� ���ڵ� ���� 2d �̸��̸� ���⿡ ����
		{
			for (i = 0; i < curr->fill_cnt; i++)
			{
				if (strcmp(in_key, curr->ele[i].name) < 0) break;	// i : ���ڵ尡 �� �ڸ�
			}
			for (a = curr->fill_cnt; i < a; a--)
			{
				curr->ele[a] = curr->ele[a - 1];
				curr->ptr[a + 1] = curr->ptr[a];
			}
			curr->ele[i] = in_rec;	// �� �ڸ��� ���ڵ� ����
			curr->ptr[i + 1] = child; // �� ��ġ�� ����Ʈ ����
			(curr->fill_cnt)++;
			return 0;
		}

		for (i = 0; i < 2 * d; i++)	// curr�� ���ڵ� ���� 2d�� bnode ���� ����
		{
			if (strcmp(in_key, curr->ele[i].name) < 0) break;	// i : ���ڵ尡 �� �ڸ�
		}

		bnode.ptr[0] = curr->ptr[0];
		for (a = 0; a < i; a++)
		{
			bnode.ele[a] = curr->ele[a];
			bnode.ptr[a + 1] = curr->ptr[a + 1];
		}	// bnode�� i �պκ� ����

		bnode.ele[i] = in_rec;	// bnode�� i�� ���ڵ� ����
		bnode.ptr[i + 1] = child;	// bnode�� i+1�� ������ ����

		for (a = i + 1; a <= 2 * d; a++)
		{
			bnode.ele[a] = curr->ele[a - 1];
			bnode.ptr[a + 1] = curr->ptr[a];
		}	// bnode�� i �޺κ� ����

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
		// curr�� bnode�� �պκ� ���� (��� ���ڵ��� �պκ�)

		new_ptr = (nodeptr)malloc(sizeof(node));

		for (i = 0; i < d; i++)
		{
			new_ptr->ele[i] = bnode.ele[i + d + 1];
			new_ptr->ptr[i] = bnode.ptr[i + d + 1];
		}
		new_ptr->ptr[i] = bnode.ptr[2 * d + 1];
		new_ptr->fill_cnt = d;
		// new_ptr�� bnode�� �޺κ� ���� (��� ���ڵ��� �޺κ�)

		in_rec = bnode.ele[d];	// bnode�� �߰� ���ڵ带 in_rec�� ��
		child = new_ptr;	// new_ptr�� child�� ��

		if (curr == *root)	// curr�� root�� ��, tptr�� ���ο� root ���� �� ����
		{
			tptr = (nodeptr)malloc(sizeof(node));
			tptr->ele[0] = in_rec; // tptr->ele[0] = bnode.ele[d];
			tptr->ptr[0] = curr; 
			tptr->ptr[1] = child;
			tptr->fill_cnt = 1;
			*root = tptr;

			return 0;
		}

		find = parent;	// find(ã�� ���) = �θ���
		now = *root;	// now�� root�� �ΰ� ã�� ����
		parent = now;
		found = 0;

		do
		{
			for (i = 0; i < now->fill_cnt; i++)
			{
				if (strcmp(find->ele[0].name, now->ele[i].name) < 0) break;
				else if (strcmp(find->ele[0].name, now->ele[i].name) == 0)	// find �� ã���� found=1
				{
					found = 1;
				}
			}
			if (found == 0)	// find ���� ã�� ������ ��, now_child �� ���� �� �ݺ�
			{
				now_child = now->ptr[i];
				parent = now;
				now = now_child;
			}
		} while (!found);
		curr = now;	// curr = now(���� �θ���)�� �ΰ� �ݺ�

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
				found = 1; break; // ã������ for �ݺ��� ���� (i : ��� �ȿ��� ���ڵ��� ��ġ)
			}
		}
		if (found == 1) break; // ã������ do �ݺ��� ����
		else // �� ã������
		{
			if (curr->ptr[i])	// �ڽ� ��尡 �ִٸ�, level ���� �� �ݺ�
			{
				level++;
				curr = curr->ptr[i];
			}
			else
			{
				printf("���� ���ڵ��Դϴ�.\n");
				return 0;
			}
		}
	} while (1); // ���ڵ��� ��ġ ã�� (curr->ele[i])

	printf("���ڵ��� ���� : %d, ��� �ȿ��� ���ڵ��� ��ġ : %d\n", level, (i+1));
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
				found = 1; break; // ã������ for �ݺ��� ����
			}
		}
		if (found == 1) break; // ã������ do �ݺ��� ����
		else // �� ã���� ��
		{
			if (curr->ptr[i]) // �ڽ��� �ִٸ� �ݺ�
			{
				parent = curr;
				curr = curr->ptr[i];
			}
			else // �ڽ��� ���ٸ� ���� ���ڵ�
			{
				printf("���� ���ڵ��Դϴ�.\n");
				return 0;
			}
		}
	} while (1); // ��� ��ġ ã�� (curr->ele[i])

	if (!(curr->ptr[i]))	// curr�� ��������� ��� �ٷ� ���� �Ϸ�.
	{
		for (a = i; a < (curr->fill_cnt - 1); a++)
		{
			curr->ele[a] = curr->ele[a + 1];
		}
		(curr->fill_cnt)--;
		leaf = curr;
	}
	else // ������尡 �ƴ϶��, ���ڵ�� �ٲ� ���� ���ڵ�(leaf record) ã��
	{
		leaf = curr->ptr[i + 1];	// ���� ����� ������ �ڽ� ���� �̵� ��
		while (leaf->ptr[i])
		{
			leaf = leaf->ptr[0];
		}	// ��������� ������, ���� ���� �ڽ� ���� �̵�

		curr->ele[i] = leaf->ele[0]; // ������� ���ڵ�� ���� ���ڵ带 �ٲ�

		for (a = 0; a < leaf->fill_cnt - 1; a++)
		{
			leaf->ele[a] = leaf->ele[a + 1];
		}
		(leaf->fill_cnt)--;
	} // ������� ���ڵ�� ���� ���ڵ�� �ٲ� �� ����

	if (leaf->fill_cnt >= d)
	{
		printf("���� �Ϸ�.\n");
		return 0;
	}	// ������� ������ �� ���ڵ� ������ d�� �̻��̸� ���� �Ϸ�.

	// ������� ������ �� ���ڵ� ������ d�� �̸��� ��
	// left : curr�� ���� ���, right : curr�� ������ ���
	do
	{
		if (parent == leaf)
		{
			return;
		}	// curr�� �������� ����.

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

		if (right->fill_cnt > d) // right�� ���ڵ� ���� d �̻��̸� �й�
		{
			leaf->ele[d - 1] = parent->ele[i];
			parent->ele[i] = right->ele[0];
			for (a = 0; a < (right->fill_cnt - 1); a++)
			{
				right->ele[a] = right->ele[a + 1];
			}
			(leaf->fill_cnt)++;
			(right->fill_cnt)--;
			printf("���� �Ϸ�.\n");
			return 0;
		}
		else if (left->fill_cnt > d) // right�� ���ڵ� ���� d���̰�, left�� ���ڵ� ���� d �̻��̸� �й�
		{
			for (a = d - 1; 0 < a; a--)
			{
				leaf->ele[a] = leaf->ele[a - 1];
			}
			leaf->ele[0] = parent->ele[i - 1];
			parent->ele[i - 1] = left->ele[left->fill_cnt - 1];
			(leaf->fill_cnt)++;
			(left->fill_cnt)--;
			printf("���� �Ϸ�.\n");
			return 0;
		}

		// left�� right�� ���ڵ� ���� d���� ��
		if (right) // right�� ������ ��
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
				printf("���� �Ϸ�.\n");
				return 0;
			}
		}
		else if (left) // �� ������ ����� �� (right�� �������� ���� ��)
		{
			left->ele[d] = parent->ele[i - 1];
			for (a = d + 1; a < 2 * d; a++)
			{
				left->ele[a] = leaf->ele[a - d - 1];
			}
			parent->ptr[i] = NULL;
			(left->fill_cnt) = 2 * d;
			(parent->fill_cnt)--;
			if (parent->fill_cnt >= d)	// �θ����� ���ڵ� ���� d�� �̻��̸� ���� �Ϸ�.
			{
				printf("���� �Ϸ�.\n");
				return 0;
			}
		}

		// �θ����� ���ڵ� ���� d�� �̸��� ��
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
					found = 1; break; // ã������ for �ݺ��� ����
				}
			}
			if (found == 1) break; // ã������ do �ݺ��� ����
			parent = curr;
			curr = curr->ptr[i];
		} while (1); // curr(���� �θ���)�� ���� parent�� ã�� ������ �ݺ�
		leaf = curr; // leaf = curr(���� �θ���)�� �ΰ� �ݺ�
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
	}	// ���� ���� ���� �� �� ���

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
			}	// ���� ���� ���� �� �� ���

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
