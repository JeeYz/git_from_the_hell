
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <fstream>

using namespace std;

#define NoVL 28*28+10 ///Number of Visible Layer
#define NoHL 100 ///Number of Hidden Layer
#define Val_size 100
#define Train_mass 400

#define learningrate 0.01 ///learning rate
#define times 10
#define valueofk 20

#define INIT_zero_bias 1
#define INIT_random_bias 0


///local functions
float sigmoid_function01(int);
float sigmoid_function02(int);
float sigmoid_function03(int, int);
float sigmoid_function04(int);

float generator_random(int);
void initializer_weight();
void initializer_bias();

int rbm_mcmc();
int rbm_weight_update();
int rbm_h_bias_update();
int rbm_v_bias_update();

float sampling_mcmc(float);

int choose_and_fill(int);

int test_MNIST();
void validation_test();
int determine_validation();

int val_mcmc(int);
void test_mcmc(int);

int val_fill_array(int, int);

///variables
float weight[NoVL][NoHL];

float visible_zero[NoVL];
float bias_h_zero[NoHL];
float bias_v_zero[NoVL];

float visiblevalues[NoVL];
float hiddenvalues[NoHL];

///float vali_vis_values[Val_size][NoVL];
///float vali_vis_values[100][NoVL];
float * vali_vis_values[Val_size];

float visiblebias[NoVL];
float hiddenbias[NoHL];

float sigmoid_zero[NoHL];

float visible_generate[NoVL];



///activation function -> sigmoid
/// visible layer -> hidden layer
float sigmoid_function03(int i, int m){
    float result=0;
    float temp_sum=0;
    int j;

    for(j=0; j<NoVL; j++){
        temp_sum += (float)(weight[j][i]*vali_vis_values[m][j]);
    }

    temp_sum += hiddenbias[i]; /// hidden layer bias

    ///sigmoid
    result = (float)1 / (1+exp((-1)*temp_sum));

    return result;
}// complete

/// hidden layer -> visible layer
float sigmoid_function04(int j){
    float result=0;
    float temp_sum=0;
    int i;

    for(i=0; i<NoHL; i++){
        temp_sum += (float)(weight[j][i]*hiddenvalues[i]);
    }

    temp_sum += visiblebias[j]; /// visible layer's bias

    result = (float)1 / (1+exp((-1)*temp_sum));

    return result;
}// complete


int val_mcmc(int m){

    int i, j, k;
    float p; // visible to hidden
    int res;
    float temp;

    for (k=0; k<valueofk; k++){

        for (i=0; i<NoHL; i++){
            hiddenvalues[i] = sigmoid_function03(i, m); // when h == 1
        }
        for (j=0; j<10; j++){
            visiblevalues[j] = sigmoid_function04(j);
        }

        if (k == (valueofk-1)){
            for (j=0; j<10; j++){

                if (j == 0){
                    temp = visiblevalues[j];
                    res = 0;
                    continue;
                }
                if (visiblevalues[j] > temp){
                    temp = visiblevalues[j];
                    res = j;
                }
            }
            return res;
        }
    }
}


void initializer_bias(){
    int i, j;

#if INIT_random_bias
    for (i=0; i<NoHL; i++){
        hiddenbias[i] = generator_random(1);
        bias_h_zero[i] = hiddenbias[i];
    }
    for (j=0; j<NoVL; j++){
        visiblebias[j] = generator_random(1);
        bias_v_zero[j] = visiblebias[j];
    }
#endif // INIT_random_bias

#if INIT_zero_bias
    for (i=0; i<NoHL; i++){
        hiddenbias[i] = 0;
        bias_h_zero[i] = hiddenbias[i];
    }
    for (j=0; j<NoVL; j++){
        visiblebias[j] = 0;
        bias_v_zero[j] = visiblebias[j];
    }
#endif // INIT_zero_bias

    return;
}


float generator_random(int para){
    float tm;
    tm = (float)rand()/RAND_MAX;
    if (para == 0){
        /// generating random weight
        if (tm > 0.5){
            return ((float)rand()/RAND_MAX);
        } else {
            return ((-1)*(float)rand()/RAND_MAX);
        }
    } else if (para == 1){
        /// generating random bias
        return ((float)rand()/RAND_MAX);
    }
} // complete


void initializer_weight(){
    int i;
    int j;

    for(j=0; j<NoVL; j++){
        for(i=0; i<NoHL; i++){
            //weight[j][i] = generator_random(0);
            weight[j][i] = 0;
        }
    }

    return;
} // complete


///activation function -> sigmoid
/// visible layer -> hidden layer
float sigmoid_function01(int i){
    float result=0;
    float temp_sum;
    int j;

    temp_sum = 0;
    for(j=0; j<NoVL; j++){
        temp_sum += (float)(weight[j][i]*visiblevalues[j]);
    }

    temp_sum += hiddenbias[i]; /// hidden layer bias
    //cout << hiddenbias[i] <<endl;

    ///sigmoid
    result = (float)1 / (1+exp((-1)*temp_sum));
    //cout << result << endl;
    return result;
}// complete

/// hidden layer -> visible layer
float sigmoid_function02(int j){
    float result=0;
    float temp_sum=0;
    int i;

    for(i=0; i<NoHL; i++){
        temp_sum += (float)(weight[j][i]*hiddenvalues[i]);
    }

    temp_sum += visiblebias[j]; /// visible layer's bias

    result = (float)1 / (1+exp((-1)*temp_sum));

    return result;
}// complete


float sampling_mcmc(float p){
    float temp;

    temp = (float)rand() / RAND_MAX;

    if (temp >= (1 - p)){
    //if (temp <= p){
        return 1;
    } else {
        return 0;
    }
}

int rbm_mcmc(){

    int i, j, k;
    float res;

    float p; // visible to hidden

    for (k=0; k<valueofk; k++){
        for (i=0; i<NoHL; i++){
            p = sigmoid_function01(i); // when h == 1
            hiddenvalues[i] = sampling_mcmc(p);
            if (k==0){
                sigmoid_zero[i] = p;
            }
        }

        for (j=0; j<NoVL; j++){
            p = sigmoid_function02(j);
            visiblevalues[j] = sampling_mcmc(p);
        }
    }

    return 1;
}


int rbm_weight_update(){
    int i, j;
    float tmp;

    for (j=0; j<NoVL; j++){
        for (i=0; i<NoHL; i++){
            //weight[j][i] += learningrate*(sigmoid_zero[i]*visible_zero[j] - sigmoid_function01(i)*visiblevalues[j]);
            tmp = sigmoid_function01(i);
            weight[j][i] += (float)sigmoid_zero[i]*visible_zero[j] - (float)tmp*visiblevalues[j];
        }
    }

    return 1;
}

int rbm_h_bias_update(){
    int i;
    float tmp;

    for (i=0; i<NoHL; i++){
        //hiddenbias[i] += learningrate*(sigmoid_zero[i] - sigmoid_function01(i));
        tmp = sigmoid_function01(i);
        hiddenbias[i] += sigmoid_zero[i] - tmp;

    }

    return 1;
}

int rbm_v_bias_update(){
    int j;

    for (j=0; j<NoVL; j++){
        //visiblebias[j] += learningrate*(bias_v_zero[j] - visiblebias[j]);
        visiblebias[j] += visible_zero[j] - visiblevalues[j];
        //cout << visible_zero[j] << " : " << visiblevalues[j] << "  ";
    }

    return 1;
}

int choose_and_fill(int num){
    int i;

    for (i=0; i<10; i++){
        if (i == num){
            visiblevalues[i] = 1;
            visible_zero[i] = visiblevalues[i];
            continue;
        }
        visiblevalues[i] = 0;
        visible_zero[i] = visiblevalues[i];
    }
    return 1;
}

int val_fill_array(int num, int j){
    int i;

    for (i=0; i<10; i++){
        if (i == num){
            vali_vis_values[j][i] = 0.5;
            continue;
        }
        vali_vis_values[j][i] = 0.5;
    }
    return 1;
}

///main function
int main(){

    int h, k, i, j, ep, co;
    int para, m, n, val_res;
    //int val_ans[Val_size];
    int * val_ans;
    int val_acc;

    int print_para;

    float val_acc_rate;

    val_acc = 0;
    co = 0;

    srand(time(NULL));

    ///string temp;
    int temp;
    fstream fp;

    initializer_bias();
    initializer_weight();

    ///val_ans = (int*) malloc (sizeof(int)*100);
    val_ans = (int*) malloc (sizeof(int)*Val_size);
    for (i=0; i<Val_size; i++){
        vali_vis_values[i] = (float *) malloc (sizeof(float)*NoVL);
    }

    fp.open("train.txt"); /// change from BAS to MNIST
    for (ep=0; ep<times; ep++){
        //fp.open("train01.txt"); /// change from BAS to MNIST
        cout << (ep+1) << "th times : " << endl;
        print_para = 0;
        m = 0;
        n = 0;

        for (i=0; i<Val_size; i++){
            for (j=0; j<NoVL; j++){
                fp >> temp;
                if (j < 10){
                    val_ans[i] = temp;
                    ///cout << temp << endl;
                    val_fill_array(temp, i);
                    j = 9;
                    continue;
                }
                vali_vis_values[i][j+9] = (float)temp/255;
            }
        }
        while(!fp.eof()){
            for (j=0; j<NoVL; j++){
                fp >> temp;
                if (j == 0){
                    choose_and_fill(temp);
                    j = 9;
                    continue;
                }
                visiblevalues[j+9] = (float)temp/255;
            }

            rbm_mcmc();


            rbm_weight_update();
            rbm_h_bias_update();
            rbm_v_bias_update();
            print_para += 1;

            if (print_para%100 == 0){
                cout << print_para << "th looping"<< endl;
            }
            if (print_para == Train_mass) break;
        }

        for (i=0; i<Val_size; i++){

            val_res = val_mcmc(i);

            ///cout << val_res << "  :  " << val_ans[i] << endl;
            if (val_res == val_ans[i]){
                //cout << val_res << "  :  " << val_ans[i] << endl;
                val_acc += 1;
                ///cout << val_acc << endl;
            }
        }
        cout << val_acc << endl;
        val_acc_rate = (float)val_acc/Val_size;
        cout << "accuracy : " << val_acc_rate*100 << "%" << endl;
        val_acc = 0;
        cout << endl;
        cout << endl;
        //fp.close();
    }/// for : times

    fp.close();

    return 0;
}
