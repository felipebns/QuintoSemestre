#include <stdio.h>

int somaAux(int v[], int i, int f){
    int media = (int) (f+i)/2;
    
    if (i == f){
        return v[i];
    }

    return somaAux(v, media+1, f) + somaAux(v, i, media);
}

int soma (int v[], int n){
    return somaAux(v, 0, n-1);
}

int main(){
    int arr[] = {1,2,3,4,5,6};
    int r = soma(arr, 6);
    printf("r: %d \n", r);
    return 0;
}