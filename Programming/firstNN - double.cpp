#include 	<stdio.h>
#include	<iostream>
#include	<stdlib.h>
#include	<string.h>
#include	<time.h>
#include	<math.h>
using namespace std;
//////////////define value_comp
#define	TRUE	1
#define FALSE	0
#define	INPUT	784
#define	MAX_TRIAN	60000
#define	MAX_TEST	10000
#define	HIDDEN_01	120
#define	HIDDEN_02	100
#define	HIDDEN_03	70

/////////////global values    
double	weighted_sum_01[HIDDEN_01];
double	weighted_sum_02[HIDDEN_02];
double	weighted_sum_03[HIDDEN_03];
double	weighted_sum_04[10];
double	weight_01[INPUT][HIDDEN_01];
double	weight_02[HIDDEN_01][HIDDEN_02];
double	weight_03[HIDDEN_02][HIDDEN_03];
double	weight_04[HIDDEN_03][10];
double	bias_01[HIDDEN_01];
double	bias_02[HIDDEN_02];
double	bias_03[HIDDEN_03];
double	bias_04[10];
double	sigmoid_output_01[HIDDEN_01];
double	sigmoid_output_02[HIDDEN_02];
double	sigmoid_output_03[HIDDEN_03];
double	delta_output[10];
double	delta_hidden_01[HIDDEN_01];
double	delta_hidden_02[HIDDEN_02];
double	delta_hidden_03[HIDDEN_03];
//float	output[10];
double	softmax_output[10];
int		target[10];
int		input_data[INPUT];
//////////////list of functions
int	forward_pro();
int	random_number();
int	backward_pro();
int	forward_pro_test();
//////////////list of variables
int 	target_value;
double	learning_rate;
int		answer_number;

int		main(){
	int	para_i;
	int	para_j;
	int	i,k;
	int	epoch; 
	double	change_rate_LR;
	change_rate_LR=0.99;
	answer_number = 0;
	learning_rate = 0.001;
	epoch = 30;
	
	FILE*	trainfp;
	FILE*	testfp;	
	
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
			if (para_i % 6000 == 0){
				//printf("training answer rate : %f %%\n", (float)answer_number/6000*100);
				answer_number = 0;
			}
			if (para_i == MAX_TRIAN)
				break;
		}

		while (1){
			
			fscanf(testfp, "%d", &target_value);
			//printf("%d ",target_value);
			for (i = 0; i < INPUT; i++){
				fscanf(testfp, "%d", &input_data[i]);
			}
			forward_pro();
			para_j++;
			if (para_j == MAX_TEST){
				printf("test answer rate : %f %%\n", (double)answer_number/MAX_TEST*100);
				answer_number = 0;
				break;
			}
		}
		printf("complete!!!\n");
		fclose(trainfp);
		fclose(testfp);
		para_j=para_i=0;
		//learning_rate=learning_rate*change_rate_LR;
	}

	return 0;
}

int		random_number(){
	int		i, k, j;
	srand(time(NULL));

	for (i = 0; i<INPUT; i++){
		for (j = 0; j<HIDDEN_01; j++){
			if (0.5<rand() / (double)RAND_MAX){
				weight_01[i][j] = rand() / (double)RAND_MAX*(-1); // set up the number
			} else {
				weight_01[i][j] = rand() / (double)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_01; i++){
		for (j = 0; j<HIDDEN_02; j++){
			if (0.5<rand() / (double)RAND_MAX){
				weight_02[i][j] = rand() / (double)RAND_MAX*(-1); // set up the number
			} else {
				weight_02[i][j] = rand() / (double)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_02; i++){
		for (j = 0; j<HIDDEN_03; j++){
			if (0.5<rand() / (double)RAND_MAX){
				weight_03[i][j] = rand() / (double)RAND_MAX*(-1); // set up the number
			} else {
				weight_03[i][j] = rand() / (double)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_03; i++){
		for (j = 0; j<10; j++){
			if (0.5<rand() / (double)RAND_MAX){
				weight_04[i][j] = rand() / (double)RAND_MAX*(-1); // set up the number
			} else {
				weight_04[i][j] = rand() / (double)RAND_MAX; // set up the number
			}
		}
	}

	for (i = 0; i<HIDDEN_01; i++){
		if (0.5<rand() / (double)RAND_MAX){
			bias_01[i] = rand() / (double)RAND_MAX*(-1); // set up the number
		} else {
			bias_01[i] = rand() / (double)RAND_MAX; // set up the number
		}
	}
	for (i = 0; i<HIDDEN_02; i++){
		if (0.5<rand() / (double)RAND_MAX){
			bias_02[i] = rand() / (double)RAND_MAX*(-1); // set up the number
		} else {
			bias_02[i] = rand() / (double)RAND_MAX; // set up the number
		}
	}
	for (i = 0; i<HIDDEN_03; i++){
		if (0.5<rand() / (double)RAND_MAX){
			bias_03[i] = rand() / (double)RAND_MAX*(-1); // set up the number
		} else {
			bias_03[i] = rand() / (double)RAND_MAX; // set up the number
		}
	}
	for (i = 0; i<10; i++){
		if (0.5<rand() / (double)RAND_MAX){
			bias_04[i] = rand() / (double)RAND_MAX*(-1); // set up the number
		} else {
			bias_04[i] = rand() / (double)RAND_MAX; // set up the number
		}
	}
	
	//printf("%f  ",weight_04[0][0]);
	
	return 0;
}

int		forward_pro(){
	int		i, j;
	double	temp;
	double	answer_temp;
	int	answer_num;
	i = 0;
	j = 0;
	temp = 0;

	////////////////////1st weighted sum
	for (i = 0; i<HIDDEN_01; i++){
		for (j = 0; j<INPUT; j++){
			temp = temp + weight_01[j][i] * (double)input_data[j];
		}
		//printf("%f ",temp);
		weighted_sum_01[i] = temp + bias_01[i];
		sigmoid_output_01[i] = 1 / (1 + exp(-weighted_sum_01[i]));
		temp = 0;
	}
	//printf("%f ",sigmoid_output_01[0]);
	////////////////////2nd weighted sum
	for (i = 0; i<HIDDEN_02; i++){
		for (j = 0; j<HIDDEN_01; j++){
			temp = temp + weight_02[j][i] * sigmoid_output_01[j];
		}
		weighted_sum_02[i] = temp + bias_02[i];
		sigmoid_output_02[i] = 1 / (1 + exp(-weighted_sum_02[i]));
		temp = 0;
	}
	//printf("%f ",sigmoid_output_02[0]);
	////////////////////3rd  weighted sum
	for (i = 0; i<HIDDEN_03; i++){
		for (j = 0; j<HIDDEN_02; j++){
			temp = temp + weight_03[j][i] * sigmoid_output_02[j];
		}
		weighted_sum_03[i] = temp + bias_03[i];
		sigmoid_output_03[i] = 1 / (1 + exp(-weighted_sum_03[i]));
		temp = 0;
	}

	////////////////////4th weighted sum
	for (i = 0; i<10; i++){
		temp = 0;
		for (j = 0; j<HIDDEN_03; j++){
			temp = temp + weight_04[j][i] * sigmoid_output_03[j];
		}
		weighted_sum_04[i] = temp + bias_04[i];
//		output[i] = weighted_sum_04[i];
		
	}

	temp = 0;
	for (i = 0; i<10; i++){
		temp = temp + exp(weighted_sum_04[i]);
	}

	for (i = 0; i<10; i++){
		softmax_output[i] = exp(weighted_sum_04[i]) / temp;
		//printf("%f  ",softmax_output[i]);
	}

	for (i = 0; i<10; i++){
		target[i] = 0;
	}
	target[target_value] = 1;
	
	answer_temp=0;
	for (i = 0; i<10; i++){
		if (i == 0){
			answer_temp=softmax_output[i];
			answer_num = i;
		} else {
			if (answer_temp<softmax_output[i]){
				answer_temp=softmax_output[i];
				answer_num = i;
			}
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
	double	temp;
	////////////////	final layer delta	//////////////
	for (i = 0; i<10; i++){
		delta_output[i] = softmax_output[i] - (double)target[i];
	}
	////////////////	hidden3 layer delta 	//////////////
	
	for (i = 0; i<HIDDEN_03; i++){
		temp = 0;
		for (j = 0; j<10; j++){
			temp = temp + delta_output[j] * weight_04[i][j];
		}
		//printf("%f ",temp);
		delta_hidden_03[i] = sigmoid_output_03[i] * (1 - sigmoid_output_03[i])*temp;
		//printf("delta_hidden_03[i] : %f\n",delta_hidden_03[i]);
	}
	////////////////	hidden2 layer delta 	//////////////
	
	for (i = 0; i<HIDDEN_02; i++){
		temp = 0;
		for (j = 0; j<HIDDEN_03; j++){
			temp = temp + delta_hidden_03[j] * weight_03[i][j];
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
	////////////////	weight04 update		//////////////
	for (i = 0; i<HIDDEN_03; i++){
		for (j = 0; j<10; j++){
			weight_04[i][j] = weight_04[i][j] - learning_rate*delta_output[j] * sigmoid_output_03[i];
		}
	}
	for (i = 0; i<10; i++){
		bias_04[i] = bias_04[i] - learning_rate*delta_output[i];
	}
	////////////////	weight03 update 	//////////////
	for (i = 0; i<HIDDEN_02; i++){
		for (j = 0; j<HIDDEN_03; j++){
			weight_03[i][j] = weight_03[i][j] - learning_rate*delta_hidden_03[j] * sigmoid_output_02[i];
		}
	}
	for (i = 0; i<HIDDEN_03; i++){
		bias_03[i] = bias_03[i] - learning_rate*delta_hidden_03[i];
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
			weight_01[i][j] = weight_01[i][j] - learning_rate*delta_hidden_01[j] * (double)input_data[i];
		}
	}
	for (i = 0; i<HIDDEN_01; i++){
		bias_01[i] = bias_01[i] - learning_rate*delta_hidden_01[i];
	}

	//printf("%f  ",weight_02[0][5]);
	
	return 0;
}

