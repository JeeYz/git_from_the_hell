/**
 * @Author: JayY <JeeYz>
 * @Date:   2018-06-21T19:53:53+09:00
 * @Filename: generate_random_number_00.cpp
 * @Last modified by:   JeeYz
 * @Last modified time: 2018-11-02T13:59:57+09:00
 * @Copyright: JayY
 */



// generate random number using C/C++


#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main (){
	srand(time(NULL));

	int i;
	double tmp;
	double tmp1;



	for (i=0; i<10; i++){
		tmp1 = (double)rand()/RAND_MAX;
		tmp = (double)1/(1+exp((-1)*tmp1));
		cout << tmp << endl;
	}

	return 0;
}
