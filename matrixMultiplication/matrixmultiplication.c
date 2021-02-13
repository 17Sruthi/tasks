//Matrix Multiplication

#include<stdio.h>

int inputmat(int c1, int r1, int c2, int r2){
	int A[r1][c1],B[r2][c2],i,j;
	printf("\nEnter the elements for the first matrix:\n");
	for(i=0;i<r1;i++){
		for(j=0;j<c1;j++){
			scanf("%d", &A[i][j]);
		}
	}
	printf("\nEnter the elements for the second matrix:\n");
	for(i=0;i<r2;i++){
		for(j=0;j<c2;j++){
			scanf("%d", &B[i][j]);
		}
	}
	printmat(r1,c1,A,r2,c2,B);
	return 0;	
}

int printmat(int r1, int c1, int A[][c1],int r2, int c2, int B[][c2]){
	int i,j;
	printf("\nFirst Matrix\n");
	for(i=0;i<r1;i++){
		for(j=0;j<c1;j++){
			printf("%d\t", A[i][j]);
		}
		printf("\n");
	}
	printf("\nSecond Matrix\n");
	for(i=0;i<r2;i++){
		for(j=0;j<c2;j++){
			printf("%d\t", B[i][j]);
		}
		printf("\n");
	}
	matmulti(r1,c1,A,r2,c2,B);
	return 0;
}

int matmulti(int r1,int c1,int A[][c1], int r2, int c2, int B[][c2]){
	int i,j=0,C[r1][c2],k=0;
	printf("\nResultant Matrix\n");
	for(i=0;i<r1;i++){
		for(j=0;j<c2;j++){
			C[i][j]=0;
		}
	}

	for(i=0;i<r1;i++){
		for(j=0;j<c2;j++){
			for(k=0;k<c1;k++){
				C[i][j] = C[i][j]+(A[i][k]*B[k][j]);
			}
			printf("%d\t", C[i][j]);
		}
		printf("\n");
	}
	return 0;
}

int inputrowscols(int r1,int c1,int r2,int c2){
	if(c1<1){
		printf("\nEnter valid number of columns for first matrix!");
	}
	else if(r1<1){
		printf("\nEnter valid number of columns for first matrix!");
	}
	else if(c2<1){
	   printf("\nEnter valid number of columns for first matrix!");
	}
	else if(r2<1){
		printf("\nEnter valid number of columns for first matrix!");
	}
	else if(c1!=r2){
		printf("\nThe cols of first matrix should be equal to the rows of second matrix");
	}
	else{
		inputmat(c1,r1,c2,r2);
	}
	return 0;
}

int main(){
    int r1,c1,r2,c2;
    printf("\n\nUNIT-TESTING CASE 1: NEGATIVE INPUT");
    inputrowscols(3,4,5,-3);
    printf("\n\nUNIT-TESTING CASE 2: 0 AS INPUT");
    inputrowscols(3,4,0,3);
    printf("\n\nUNIT-TESTING CASE 3: INPUT WITH C1!=R2");
    inputrowscols(3,4,2,2);
    printf("\n\nUNIT-TESTING CASE 4: VALID INPUT(USER CHOICE)");
    printf("\nEnter the number of cols for first matrix:");
	scanf("%d", &c1);
	printf("\nEnter the number of rows for first matrix:");
	scanf("%d", &r1);
	printf("\nEnter the number of cols for second matrix:");
	scanf("%d", &c2);
	printf("\nEnter the number of rows for second matrix:");
	scanf("%d", &r2);
	inputrowscols(r1,c1,r2,c2);
    return 0;
}