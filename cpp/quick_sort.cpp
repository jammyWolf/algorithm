#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int a[10] = {72, 6, 57, 88, 60, 42, 83, 73, 48, 85};

void quickSort(int arr[], int left, int right){
	int i = left, j = right, k=left, pivot = arr[k];
	while(i<j){
		while(i<k && arr[i]<pivot) ++i;
		if(i<k){
			arr[k] = arr[i];
			k = i;
		}//if
		while(j>k && arr[j]>pivot) --j;
		if(j>k){
			arr[k] = arr[j];
			k = j;
		}//if
	}//while
	arr[k] = pivot;
	if(k-left > 1)	quickSort(arr, left, k-1); //left area exist
	if(right-k > 1)	quickSort(arr, k+1, right);
}//quickSort

int main(){
	quickSort(a, 0, 9);
	for(int i=0;i<10;i++)
		cout<<a[i]<<" ";
	return 0;
}
