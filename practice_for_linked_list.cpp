/**
 * @Author: JayY <JeeYz>
 * @Date:   2018-05-23T10:08:31+09:00
 * @Filename: practice_for_linked_list.cpp
 * @Last modified by:   JeeYz
 * @Last modified time: 2018-11-02T14:00:02+09:00
 * @Copyright: JayY
 */



#include<stdio.h>
#include <stdlib.h>
typedef struct listNode *listPointer;				// ������ �ּҰ��� ������ listPointer ����
typedef struct listNode {							// int�� �����Ϳ� link�� ������ ���� ����
	int data;
	listPointer link;
}listNode;


listPointer create3() {								// ���� 3���� ������ ���� 10,20,30�� �Է��� ���� ����
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

//				�� ��  �� ��

listPointer search_last_node(listPointer ptr)		// ù ���带 �Է¹ް� ptr�̳� ptr->link�� NULL�̸� �� data�� ���¹� ����Ʈ�� ������ �ּҰ��� ��ȯ
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
//              �� ��  �� ��

int main()								//�����Լ�, ���� 3���� ����, ������ ���带 ã�Ƽ� listPointer�� ����
{
	listPointer start;
	listPointer last;
	start = create3();
	last = search_last_node(start);
	printf("%p", last);
}
