#include<stdio.h>
#include <stdlib.h>
typedef struct listNode *listPointer;				// 노드의 주소값을 가지는 listPointer 정의
typedef struct listNode {							// int형 데이터와 link를 가지는 노드 정의
	int data;
	listPointer link;
}listNode;


listPointer create3() {								// 노드 3개를 만들고 각각 10,20,30값 입력후 서로 연결
	listPointer first, second, third;
	first = (listPointer)malloc(sizeof(listNode));
	second = (listPointer)malloc(sizeof(listNode));
	third = (listPointer)malloc(sizeof(listNode));
	third->data = 30;
	third->link = NULL;
	second->link = third;
	second->data = 20;
	first->data = 10;
	first->link = second;
	printf("%p\n%p\n%p\n", first, second, third);
	return first;
}

//				숙 제  부 분 

listPointer search_last_node(listPointer ptr)		// 첫 노드를 입력받고 ptr이나 ptr->link가 NULL이면 각 data를 출력밑 리스트의 마지막 주소값을 반환
{
	if (ptr == NULL) {
		return NULL;
	}
	else {
		//***************************
		if (ptr->link == NULL) {
			return ptr;
		}
		else {
			ptr = (ptr->link);
			search_last_node(ptr);
		}
	}	//****************************
}
//              숙 제  부 분

int main()								//메인함수, 노드 3개를 생성, 마지막 노드를 찾아서 listPointer에 저장
{
	listPointer start;
	listPointer last;
	start = create3();
	last = search_last_node(start);
	printf("%p", last);
}
