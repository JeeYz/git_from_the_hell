#include 	<stdio.h>
#include 	<stdlib.h>
#include 	<string.h>
#include 	<time.h>
#include 	<math.h>

#include 	<iostream>
using namespace std;

#define 	INPUT		
#define 	HIDDEN01	100
#define 	HIDDEN02	100
#define 	OUTPUT	

#define	Learning_Rate
#define	Epoch

#define	Sigmoid
#define 	Hyper_Tangent

#define 	Cross_Entropy
#define 	Sum_of_Square

int	target_prob[OUTPUT];
int	target_value[OUTPUT];
int	input_data[INPUT];

double	weight_01[INPUT][HIDDEN01];
double	weight_02[HIDDEN01][HIDDEN02];
double	weight_03[HIDDEN02][OUTPUT];

double	output_h01[HIDDEN01];
double	output_h02[HIDDEN02];
double	output_final[OUTPUT];

double	final_prob[OUTPUT];

double	bias_H01[HIDDEN01];
double	bias_H02[HIDDEN02];
double	bias_out[OUTPUT];

double	delta_H01[HIDDEN01];
double	delta_H02[HIDDEN02];
double	delta_out[OUTPUT];

double	weighted_sum_H01[HIDDEN01];
double	weighted_sum_H02[HIDDEN02];
double	weighted_sum_out[OUTPUT];

void	fileinput();
void	forward_comp();
void	backward_comp();
void	weight_update();
void	random_num();

double	softmax_output(double,double);
double	error_function(double,double);
double	activation_function(double);

main(){	
	int i;
	
	fileinput();
	random_num();
	
	forward_comp();
	
	backward_comp();
	
	return 0;
}


void	random_num(){
	int i;
	int j;
	srand(time(NULL));
		
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			weight_01[i][j]=(double)rand()/RANDMAX-0.5;
		}
	}
	
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			weight_02[i][j]=(double)rand()/RANDMAX-0.5;
		}
	}
	
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<OUTPUT;j++){
			weight_03[i][j]=(double)rand()/RANDMAX-0.5;
		}
	}
	
	for(i=0;i<HIDDEN01;i++){
		bias_H01[i]=(double)rand()/RANDMAX-0.5;
	}
	
	for(i=0;i<HIDDEN02;i++){
		bias_H02[i]=(double)rand()/RANDMAX-0.5;
	}
	
	for(i=0;i<OUTPUT;i++){
		bias_out[i]=(double)rand()/RANDMAX-0.5;
	}
	
	return;
}


void	fileinput(){
	return;
}


void	forward_comp(){
	int	i,j;
	double	temp;
	temp=0;
	
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<INPUT;j++){
			temp+=weight_01[j][i]*(double)input_data[j];
		}
		weighted_sum_H01[i]=temp+bias_H01[i];
		output_h01[i]=activation_function(weighted_sum_H01[i]);
		temp=0;
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<HIDDEN01;j++){
			temp+=weight_01[j][i]*(double)input_data[j];
		}
		weighted_sum_H02[i]=temp+bias_H02[i];
		output_h02[i]=activation_function(weighted_sum_H02[i]);
		temp=0;
	}
	for(i=0;i<OUTPUT;i++){
		for(j=0;j<HIDDEN02;j++){
			temp+=weight_01[j][i]*(double)input_data[j];
		}
		weighted_sum_out[i]=temp+bias_out[i];
		temp=0;
	}
	for(i=0;i<OUTPUT;i++){
		temp+=exp(weighted_sum_out[i]);
	}
	
	for(i=0;i<OUTPUT;i++){
		final_prob[i]=softmax_output(weighted_sum_out[i],temp);
	}
	
	return;
}

double	activation_function(double t_value){
	
	double result;
	
#ifdef 	Sigmoid
	result=(double)1/(1+exp(-t_value));
	return (result);
#endif

#ifdef 	Hyper_Tangent
	result=(exp(t_value)-exp(-t_value))/(exp(t_value)+exp(-t_value));
	return (result);
#endif
}

#ifdef 	Sum_of_Square

void	backward_comp(){
	int i,j;
	double temp;
	temp=0;
	for(i=0;i<OUTPUT;i++){
		delta_out[i]=sum_of_square[i]-target_value[i];
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<OUTPUT;j++){
			temp+=delta_out[j]*weight_03[i][j]; 
		}
		delta_H02[i]=output_h02[i]*(1-output_h02[i])*temp;
		temp=0;
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			temp+=delta_H02[j]*weight_02[i][j]; 
		}
		delta_H01[i]=output_h01[i]*(1-output_h01[i])*temp;
		temp=0;
	}
	return;
}

void	weight_update(){
	int i,j;
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			weight_01[i][j]=weight_01[i][j]-(double)Learning_Rate*delta_H01[j]*(double)input_data[i];
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			weight_02[i][j]=weight_02[i][j]-(double)Learning_Rate*delta_H02[j]*output_h01[i];
		}
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<OUTPUT;j++){
			weight_03[i][j]=weight_03[i][j]-(double)Learning_Rate*delta_out[j]*output_h02[i];
		}
	}
	for(i=0;i<HIDDEN01;i++){
		bias_H01[i]=bias_H01[i]-(double)Learning_Rate*delta_H01[i];
	}
	for(i=0;i<HIDDEN02;i++){
		bias_H02[i]=bias_H02[i]-(double)Learning_Rate*delta_H02[i];
	}
	for(i=0;i<OUTPUT;i++){
		bias_out[i]=bias_out[i]-(double)Learning_Rate*delta_out[i];
	}
	return;
}

double	error_function(double target,double output){
	double error_value;
	error_value=(target-output)*(target-output)/2;
	return (error_value);
}
#endif

#ifdef 	Cross_Entropy
void	backward_comp(){
	int i,j;
	double temp;
	temp=0;
	for(i=0;i<;i++){
		delta_out[i]=final_prob[i]-target_prob[i;]
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<OUTPUT;j++){
			temp+=delta_out[j]*weight_03[i][j]; 
		}
		delta_H02[i]=output_h02[i]*(1-output_h02[i])*temp;
		temp=0;
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			temp+=delta_H02[j]*weight_02[i][j]; 
		}
		delta_H01[i]=output_h01[i]*(1-output_h01[i])*temp;
		temp=0;
	}
	return;
}

void	weight_update(){
	int i,j;
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			weight_01[i][j]=weight_01[i][j]-(double)Learning_Rate*delta_H01[j]*(double)input_data[i];
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			weight_02[i][j]=weight_02[i][j]-(double)Learning_Rate*delta_H02[j]*output_h01[i];
		}
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<OUTPUT;j++){
			weight_03[i][j]=weight_03[i][j]-(double)Learning_Rate*delta_out[j]*output_h02[i];
		}
	}
	for(i=0;i<HIDDEN01;i++){
		bias_H01[i]=bias_H01[i]-(double)Learning_Rate*delta_H01[i];
	}
	for(i=0;i<HIDDEN02;i++){
		bias_H02[i]=bias_H02[i]-(double)Learning_Rate*delta_H02[i];
	}
	for(i=0;i<OUTPUT;i++){
		bias_out[i]=bias_out[i]-(double)Learning_Rate*delta_out[i];
	}
	return;
}

double	error_function(double target,double output){
	double error_value;
	return;
}
#endif

double	softmax_output(double w_sum,double sum){
	double result;
	result=exp(w_sum)/temp;
	return (result);
}













