#include <stdio.h>
#include	<iostream>
#include	<stdlib.h>
#include	<string.h>
#include	<time.h>
#include	<math.h>
using namespace std;
//////////////define value
#define	INPUT	784
#define	MAX_TRIAN 	60000
#define	MAX_TEST	10000
#define	HIDDEN_01	300
#define	HIDDEN_02	300

/////////////global values    
float	weighted_sum_01[HIDDEN_01];
float	weighted_sum_02[HIDDEN_02];
float	weighted_sum_03[10];
float	weight_01[INPUT][HIDDEN_01];
float	weight_02[HIDDEN_01][HIDDEN_02];
float	weight_03[HIDDEN_02][10];
float	bias_01[HIDDEN_01];
float	bias_02[HIDDEN_02];
float	bias_03[10];
float	sigmoid_output_01[HIDDEN_01];
float	sigmoid_output_02[HIDDEN_02];
float	delta_output[10];
float	delta_hidden_01[HIDDEN_01];
float	delta_hidden_02[HIDDEN_02];
float	softmax_output[10];
int	target[10];
int	input_data[INPUT];
//////////////list of functions
int	forward_pro();
int	random_number();
int	backward_pro();
//////////////list of variables
int 	target_value;
float	learning_rate;
int		answer_number;

int		main(){
	int	para_i;
	int	para_j;
	int	i,k;
	int	epoch; 
	answer_number = 0;
	learning_rate = 0.001;
	epoch = 1000;
	
	FILE*	trainfp;
	FILE*	testfp;
	FILE*	writefp;
	
	writefp=fopen("result_data_01.txt","a+");
	fprintf(writefp,"\n\n\nTest Start!!!\n\n");
	
	para_i = para_j = 0;
	random_number();
	
	for (k = 0; k < epoch; k++){
		trainfp = fopen("train.txt", "r");
		testfp = fopen("test.txt", "r");
		while (1){
	
			fscanf(trainfp, "%d", &target_value);
			//printf("%d ",target_value);
			for (i = 0; i < INPUT;i++){
				fscanf(trainfp, "%d", &input_data[i]);
			}
			forward_pro();
			backward_pro();
			para_i++;
//			if (para_i % 6000 == 0){
//				//printf("training answer rate : %f %%\n", (float)answer_number/6000*100);
//				answer_number = 0;
//			}
			if (para_i == MAX_TRIAN)
				break;
		}
		answer_number=0;
		while (1){
			
			fscanf(testfp, "%d", &target_value);
			for (i = 0; i < INPUT; i++){
				fscanf(testfp, "%d", &input_data[i]);
			}
			forward_pro();
			para_j++;
			if (para_j == MAX_TEST){
				printf("test answer rate : %f %%\n", (float)answer_number/MAX_TEST*100);
				fprintf(writefp,"#%dth epoch test accuracy rate : %f %%\n",k+1,(float)answer_number/MAX_TEST*100);
				answer_number = 0;
				break;
			}
		}
		printf("complete!!!\n");
		fclose(trainfp);
		fclose(testfp);
		para_j=para_i=0;
		
	}

	return 0;
}

int		random_number(){
	int		i, k, j;
	srand(time(NULL));

	for (i = 0; i<INPUT; i++){
		for (j = 0; j<HIDDEN_01; j++){
			if (0.5<rand() / (float)RAND_MAX){
				weight_01[i][j] = rand() / (float)RAND_MAX*(-1); // set up the number
			} else {
				weight_01[i][j] = rand() / (float)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_01; i++){
		for (j = 0; j<HIDDEN_02; j++){
			if (0.5<rand() / (float)RAND_MAX){
				weight_02[i][j] = rand() / (float)RAND_MAX*(-1) ; // set up the number
			} else {
				weight_02[i][j] = rand() / (float)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_02; i++){
		for (j = 0; j<10; j++){
			if (0.5<rand() / (float)RAND_MAX){
				weight_03[i][j] = rand() / (float)RAND_MAX*(-1); // set up the number
			} else {
				weight_03[i][j] = rand() / (float)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_01; i++){
		if (0.5<rand() / (float)RAND_MAX){
			bias_01[i] = rand() / (float)RAND_MAX*(-1); // set up the number
		} else {
			bias_01[i] = rand() / (float)RAND_MAX; // set up the number
		}
	}
	for (i = 0; i<HIDDEN_02; i++){
		if (0.5<rand() / (float)RAND_MAX){
			bias_02[i] = rand() / (float)RAND_MAX*(-1); // set up the number
		} else {
			bias_02[i] = rand() / (float)RAND_MAX; // set up the number
		}
	}
	for (i = 0; i<10; i++){
		if (0.5<rand() / (float)RAND_MAX){
			bias_03[i] = rand() / (float)RAND_MAX*(-1); // set up the number
		} else {
			bias_03[i] = rand() / (float)RAND_MAX; // set up the number
		}
	}
	
	//printf("%f  ",weight_04[0][0]);
	
	return 0;
}

int		forward_pro(){
	int		i, j;
	float	temp;
	float	answer_temp;
	int	answer_num;
	temp = 0;
  
	////////////////////1st weighted sum
	for (i = 0; i<HIDDEN_01; i++){
		for (j = 0; j<INPUT; j++){
			temp = temp + weight_01[j][i] * (float)input_data[j];
		}
		//printf("%f ",temp);
		weighted_sum_01[i] = temp + bias_01[i];
		sigmoid_output_01[i] = 1 / (1 + exp(weighted_sum_01[i] * (-1)));
		//printf("  %f   :   %f\n",weighted_sum_01[i],sigmoid_output_01[i]);
		temp = 0;
	}
	//printf("  %f   :   %f\n",weighted_sum_01[i],sigmoid_output_01[i]);
	////////////////////2nd weighted sum
	for (i = 0; i<HIDDEN_02; i++){
		for (j = 0; j<HIDDEN_01; j++){
			temp = temp + weight_02[j][i] * sigmoid_output_01[j];
		}
		weighted_sum_02[i] = temp + bias_02[i];
		sigmoid_output_02[i] = 1 / (1 + exp(weighted_sum_02[i] * (-1)));
		temp = 0;
	}
	//printf("%f ",sigmoid_output_02[0]);
	////////////////////3rd  weighted sum
	for (i = 0; i<10; i++){
		for (j = 0; j<HIDDEN_02; j++){
			temp = temp + weight_03[j][i] * sigmoid_output_02[j];
		}
		weighted_sum_03[i] = temp + bias_03[i];
		temp = 0;
	}
	temp=0;	
	for (i = 0; i<10; i++){
		temp = temp + exp(weighted_sum_03[i]);
	}

	for (i = 0; i<10; i++){
		softmax_output[i] = exp(weighted_sum_03[i]) / temp;
		//printf("      %f\n",softmax_output[i]);
	}

	for (i = 0; i<10; i++){
		target[i] = 0;
	}
	target[target_value] = 1;
	
	answer_temp=softmax_output[0];
	answer_num = 0;
	
	for (i = 1; i<10; i++){
		if (answer_temp<=softmax_output[i]){
			answer_temp=softmax_output[i];
			answer_num = i;
		 }
	}
	//printf("%d  ",answer_num);
	//printf("%d ",target_value);
	if (target_value == answer_num){
		answer_number++;
		//printf("%d : %d : %d \n",target_value,answer_num,answer_number);
	}

	return 0;
}

int		backward_pro(){
	int	i, j;
	float	temp;
	////////////////	final layer delta	//////////////
	for (i = 0; i<10; i++){
		delta_output[i] = softmax_output[i] - target[i];
	}
	////////////////	hidden2 layer delta 	//////////////	
	for (i = 0; i<HIDDEN_02; i++){
		temp = 0;
		for (j = 0; j<10; j++){
			temp = temp + delta_output[j] * weight_03[i][j];
		}
		delta_hidden_02[i] = sigmoid_output_02[i] * (1 - sigmoid_output_02[i])*temp;
		//printf("delta_hidden_02[i] : %f\n",delta_hidden_02[i]);
	}
	////////////////	hidden1 layer delta 	//////////////	
	for (i = 0; i<HIDDEN_01; i++){
		temp = 0;
		for (j = 0; j<HIDDEN_02; j++){
			temp = temp + delta_hidden_02[j] * weight_02[i][j];
		}
		delta_hidden_01[i] = sigmoid_output_01[i] * (1 - sigmoid_output_01[i])*temp;
	}
	////////////////	weight03 update 	//////////////
	for (i = 0; i<HIDDEN_02; i++){
		for (j = 0; j<10; j++){
			weight_03[i][j] = weight_03[i][j] - learning_rate*delta_output[j] * sigmoid_output_02[i];
		}
	}
	for (i = 0; i<10; i++){
		bias_03[i] = bias_03[i] - learning_rate*delta_output[i];
   	}
	////////////////	weight02 update 	//////////////
	for (i = 0; i<HIDDEN_01; i++){
  		for (j = 0; j<HIDDEN_02; j++){
			weight_02[i][j] = weight_02[i][j] - learning_rate*delta_hidden_02[j] * sigmoid_output_01[i];
		}
	}
	for (i = 0; i<HIDDEN_02; i++){
		bias_02[i] = bias_02[i] - learning_rate*delta_hidden_02[i];
	}
	////////////////	weight01 update		//////////////
	for (i = 0; i<INPUT; i++){
		for (j = 0; j<HIDDEN_01; j++){
			weight_01[i][j] = weight_01[i][j] - learning_rate*delta_hidden_01[j] * input_data[i];
		}
	}
	for (i = 0; i<HIDDEN_01; i++){
		bias_01[i] = bias_01[i] - learning_rate*delta_hidden_01[i];
	}
	//printf("%f  ",weight_02[0][5]);
	
	return 0;
}


