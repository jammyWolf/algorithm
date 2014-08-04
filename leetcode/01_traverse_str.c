#include "stdio.h"
#include "stdlib.h"
#include "string.h"

char * reverse_part(char *start, char *end){
	char tmp, *ptmp=start;
	while(start<end && start!=NULL && end!=NULL){
		tmp = *start;
		*start = *end;
		*end = tmp;
		start++;
		end--;
	}//while
	return ptmp;
}//reverse_part

char * reverse(char *arr, int st){

	int N = strlen(arr);
	int step = st % N;
	if(arr == NULL){
		return "";
	}
	reverse_part(arr, arr+step-1);
	reverse_part(arr+step, arr+N-1);
	reverse_part(arr, arr+N-1);
	return arr;
	
}//reverse_part

int main(void){
	char str[] = "abcdeft";
	reverse(str, 3);
	printf("%s\n", str);
	return 0;
}

