#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

#define VL 784
#define VLL 10

float vt[VLL+VL];

int choose_and_fill(int);

int choose_and_fill(int num){
	int i;
	
	for (i=0; i < 10; i++){
		if (i == num){
			vt[i] = 1;
			continue;
		}
		vt[i] = 0; 
	}
	return 1;
}


int main (){
	int temp;
	int lable;
	int i, j;
	int k;
	
	fstream fp;
	
	fp.open("train.txt");
	
	while(!fp.eof()){
		j = 0;
		for (i=0; i<=VL; i++){
			fp >> temp;
			
			if (i == 0)	{
				choose_and_fill(temp);
				j += 10;
				continue;	
			}
			vt[j] = temp;
			j += 1;
		}
		
		for (k=0; k < (VL+VLL); k++){
			if (k==10) cout<<endl;
			if((k-10)%28 == 0) cout << endl;
			cout << vt[k];
		}
		cout << endl << endl << endl;
	}
	
	return 1;
}
