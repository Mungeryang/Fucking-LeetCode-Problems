#include<stdio.h>

//最大值函数
float max(float a , float b){
	if(a > b){
		return a;
	}
	else{
		return b;
	}
}

int main(void){
	
	//先去把有边界确定好
	float Max = 0.0;
	float nums[13] = {1.5,-12.3,3.2,-5.5,23.2,3.2,-1.4,-12.2,34.2,5.4,-7.8,1.1,-4.9};//题目中已知的数组
	int left,right = 0;//有边界确定指针
	float ans = 0.0;
	float anw[13];
	
	//求正向累加序列
	for(int i = 0;i < 13;i++){
		float sum = 0.0;
		for(int j = 0;j <= i;j++){
			sum += nums[j];	
		}
		anw[i] = sum;	
	}
	//确定右边界
	for(int i = 0;i < 13;i++){
		ans = max(ans,anw[i]);
	}
	for(int i = 0;i < 13;i++){
		if(anw[i] == ans){
			right = i;
		}
	}
	//注意右边界为区间右端+1
	for(int i = 0;i < right + 1;i++){
		float sum = 0.0;
		for(left = i;left < right + 1;left++){
			sum += nums[left];
		}
		Max = max(sum,Max);
	}
	printf("%d\n",right);
	printf("%f",Max);
	return 0;
}
