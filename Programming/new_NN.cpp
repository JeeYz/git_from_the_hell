#include	<stdio.h>
#include	<string.h>
#include	<Stdlib.h>
#include	<time.h>
#include	<math.h>
#include	<iostream>
using namespace std;
#define		INPUT		784
#define		HIDDEN01	300
#define		HIDDEN02	300
#define		MAX_TRAIN	60000
#define		MAX_TEST	10000
#define		LEARNING_RATE	0.001
#define		EPOCH	1000

//#define		RAND01
//#define		RAND02
#define		RAND03
//#define		RAND04
//#define		CHANGE_LR

int		input_data[INPUT];
int		target[10];
int		target_value;
float	accuracy;
int	answer_para;
float	learning_rate;
	
float	weight01[INPUT][HIDDEN01];
float	weight02[HIDDEN01][HIDDEN02];
float	weight03[HIDDEN02][10];

float	bias01[HIDDEN01];
float	bias02[HIDDEN02];
float	bias03[10];

float	delta_H01[HIDDEN01];
float	delta_H02[HIDDEN02];
float	delta_f[10];

float	wsum01[HIDDEN01];
float	wsum02[HIDDEN02];
float	wsum03[10];

float	sig01[HIDDEN01];
float	sig02[HIDDEN02];

float	softmax[10];

void	forward();
void	back_delta();
void	back_update();
void	random_num();
void	change_Learning_rate();

int		main(){
	int	i,j,k;
	int	para_i,para_j;
	int	epoch;
	float	pre_accuracy;
	para_i=para_j=0;
	epoch=EPOCH;
	answer_para=0;
	learning_rate=LEARNING_RATE;
	
	FILE	*trainfp;
	FILE	*testfp;
	FILE	*writefp;
	writefp=fopen("result_data_02.txt","a+");
	fprintf(writefp,"\n\n\nTest Start!!!\n\n");
	random_num();
	
	for(i=0;i<epoch;i++){
		trainfp=fopen("train.txt","r");
		testfp=fopen("test.txt","r");
		
		while(1){
			fscanf(trainfp,"%d",&target_value);
			for(j=0;j<INPUT;j++){
				fscanf(trainfp,"%d",&input_data[j]);	
			}
			forward();
			back_delta();
			back_update();
			para_i++;
			if(para_i==MAX_TRAIN)
				break;
		}
		para_i=0;
		answer_para=0;
		while(1){
			fscanf(testfp,"%d",&target_value);
			for(j=0;j<INPUT;j++){
				fscanf(testfp,"%d",&input_data[j]);	
			}
			forward();
			para_j++;
			if(para_j==MAX_TEST){
				accuracy=(float)answer_para/10000;
				printf("test accuracy rate : %f %%\t",accuracy*100);
				printf("learning rate : %f\n",learning_rate);
				fprintf(writefp,"%dth epoch test accuracy rate : %f %%\t",i+1,accuracy*100);
				fprintf(writefp,"learning rate : %f\n",learning_rate);
				#ifdef	CHANGE_LR
				if(i==0){
					pre_accuracy=accuracy;
				} else {
					if(pre_accuracy>=accuracy&&learning_rate>=0.0002){
						change_Learning_rate();
					}
					pre_accuracy=accuracy;
				}
				#endif
				break;
			}
		}
		cout<<"complete!!!"<<endl;
		para_j=0;
		answer_para=0;
		fclose(trainfp);
		fclose(testfp);
	}
	
	return 1;
}
#ifdef	RAND01
void	random_num(){
	srand(time(NULL));
	int	i,j;
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			weight01[i][j]=rand()/(float)RAND_MAX-0.5;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			weight02[i][j]=rand()/(float)RAND_MAX-0.5;
		}
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<10;j++){
			weight03[i][j]=rand()/(float)RAND_MAX-0.5;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		bias01[i]=rand()/(float)RAND_MAX-0.5;
	}
	for(i=0;i<HIDDEN02;i++){
		bias02[i]=rand()/(float)RAND_MAX-0.5;
	}
	for(i=0;i<10;i++){
		bias03[i]=rand()/(float)RAND_MAX-0.5;
	}
	return;
}
#endif
#ifdef	RAND02
void	random_num(){
	srand(time(NULL));
	int	i,j;
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			weight01[i][j]=rand()/(float)RAND_MAX*2-1.0;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			weight02[i][j]=rand()/(float)RAND_MAX*2-1.0;
		}
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<10;j++){
			weight03[i][j]=rand()/(float)RAND_MAX*2-1.0;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		bias01[i]=rand()/(float)RAND_MAX*2-1.0;
	}
	for(i=0;i<HIDDEN02;i++){
		bias02[i]=rand()/(float)RAND_MAX*2-1.0;
	}
	for(i=0;i<10;i++){
		bias03[i]=rand()/(float)RAND_MAX*2-1.0;
	}
	return;
}
#endif
#ifdef	RAND03
void	random_num(){
	srand(time(NULL));
	int	temp;
	int	temp_root;
	temp_root=1000;
	int	i,j;
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			temp=rand()%temp_root;
			weight01[i][j]=(float)temp/temp_root-0.5;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			temp=rand()%temp_root;
			weight02[i][j]=(float)temp/temp_root-0.5;
		}
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<10;j++){
			temp=rand()%temp_root;
			weight03[i][j]=(float)temp/temp_root-0.5;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		temp=rand()%temp_root;
		bias01[i]=(float)temp/temp_root-0.5;
	}
	for(i=0;i<HIDDEN02;i++){
		temp=rand()%temp_root;
		bias02[i]=(float)temp/temp_root-0.5;
	}
	for(i=0;i<10;i++){
		temp=rand()%temp_root;
		bias03[i]=(float)temp/temp_root-0.5;
	}
	return;
}
#endif
#ifdef	RAND04
void	random_num(){
	srand(time(NULL));
	int	temp;
	int	temp_root;
	temp_root=1000;
	int	i,j;
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			temp=rand()%temp_root;
			weight01[i][j]=(float)temp/temp_root*2-1.0;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			temp=rand()%temp_root;
			weight02[i][j]=(float)temp/temp_root*2-1.0;
		}
	}
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<10;j++){
			temp=rand()%temp_root;
			weight03[i][j]=(float)temp/temp_root*2-1.0;
		}
	}
	for(i=0;i<HIDDEN01;i++){
		temp=rand()%temp_root;
		bias01[i]=(float)temp/temp_root*2-1.0;
	}
	for(i=0;i<HIDDEN02;i++){
		temp=rand()%temp_root;
		bias02[i]=(float)temp/temp_root*2-1.0;
	}
	for(i=0;i<10;i++){
		temp=rand()%temp_root;
		bias03[i]=(float)temp/temp_root*2-1.0;
	}
	return;
}
#endif
void	forward(){
	int	i,j;
	float	temp;
	float	answer;
	int		answer_num;
	for(j=0;j<HIDDEN01;j++){
		temp=0.0;
		for(i=0;i<INPUT;i++){
			temp = temp + weight01[i][j]*(float)input_data[i];
		}
		wsum01[j]=temp+bias01[j];
		sig01[j]=1/(1+(float)exp(-(double)wsum01[j]));
		//printf("%f ",sig01[j]);
	}
	for(j=0;j<HIDDEN02;j++){
		temp=0.0;
		for(i=0;i<HIDDEN01;i++){
			temp = temp + weight02[i][j]*sig01[i];
		}
		wsum02[j]=temp+bias02[j];
		sig02[j]=1/(1+(float)exp(-(double)wsum02[j]));
		//printf("%f ",sig02[j]);
	}
	for(j=0;j<10;j++){
		temp=0.0;
		for(i=0;i<HIDDEN02;i++){
			temp = temp + weight03[i][j]*sig02[i];
		}
		wsum03[j]=temp+bias03[j];
	}
	temp=0.0;
	for(i=0;i<10;i++){
		temp = temp + (float)exp((double)wsum03[i]);
	}
	for(i=0;i<10;i++){
		softmax[i]=(float)exp((double)wsum03[i])/temp;
		//printf("%f ",softmax[i]);
	}
	for(i=0;i<10;i++){
		if(i==target_value){
			target[i]=1;
		} else {
			target[i]=0;
		}
	}
	answer=softmax[0];
	answer_num=0;
	for(i=1;i<10;i++){
		if(answer<softmax[i]){
			answer=softmax[i];
			answer_num=i;
		}
	}
	if(target_value==answer_num){
		answer_para++;
	}
	return;
}

void	back_delta(){
	int	i,j;
	float	temp;
	for(i=0;i<10;i++){
		delta_f[i]=softmax[i]-(float)target[i];
	}
	for(i=0;i<HIDDEN02;i++){
		temp=0.0;
		for(j=0;j<10;j++){
			temp = temp + delta_f[j]*weight03[i][j];
		}
		delta_H02[i]=sig02[i]*(1.0-sig02[i])*temp;
	}
	for(i=0;i<HIDDEN01;i++){
		temp=0.0;
		for(j=0;j<HIDDEN02;j++){
			temp = temp + delta_H02[j]*weight02[i][j];
		}
		delta_H01[i]=sig01[i]*(1.0-sig01[i])*temp;
	}
	return;
}

void	back_update(){
	int	i,j;
	for(i=0;i<HIDDEN02;i++){
		for(j=0;j<10;j++){
			weight03[i][j]=weight03[i][j]-learning_rate*delta_f[j]*sig02[i];
		}
	}
	for(i=0;i<HIDDEN01;i++){
		for(j=0;j<HIDDEN02;j++){
			weight02[i][j]=weight02[i][j]-learning_rate*delta_H02[j]*sig01[i];
		}
	}
	for(i=0;i<INPUT;i++){
		for(j=0;j<HIDDEN01;j++){
			weight01[i][j]=weight01[i][j]-learning_rate*delta_H01[j]*(float)input_data[i];
		}
	}
	for(i=0;i<10;i++){
		bias03[i]=bias03[i]-learning_rate*delta_f[i];
	}
	for(i=0;i<HIDDEN02;i++){
		bias02[i]=bias02[i]-learning_rate*delta_H02[i];
	}
	for(i=0;i<HIDDEN01;i++){
		bias01[i]=bias01[i]-learning_rate*delta_H01[i];
	}
	return;
}

void	change_Learning_rate(){
	float	change_rate;
	change_rate=0.97;
	learning_rate=learning_rate*change_rate;
	return;
}







