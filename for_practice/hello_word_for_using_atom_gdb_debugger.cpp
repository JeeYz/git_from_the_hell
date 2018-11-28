/**
 * @Author: JayY
 * @Date:   2018-11-28T10:59:27+09:00
 * @Filename: hello_word_atom.cpp
 * @Last modified by:   JayY
 * @Last modified time: 2018-11-28T11:45:44+09:00
 * @Copyright: JayY
 */


/* FAILURE */
// have to use GDB Debugger. :)

#include <iostream>

void swap(int *, int *);

void swap (int * a, int * b){
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
  return;
}

int main (void){

  int a;
  int b;

  a = 100;
  b = 200;

  printf("hello, world\n");

  printf("a : %d  b : %d\n", a, b);
  swap(&a, &b);
  printf("a : %d  b : %d\n", a, b);

  return 0;
}
