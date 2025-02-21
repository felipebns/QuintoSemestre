#include <stdio.h>

int multAux(int v[], int inicio, int fim){
    int meio = (int) (inicio+fim)/2;

    if (inicio == fim){
        return v[inicio];
    }

    return multAux(v, inicio, meio) * multAux(v, meio+1, fim);
}

int mult (int v[], int n){
    return multAux(v, 0, n-1);
}


int main(){
    int arr[] = {1,2,3,4,5,6};
    int r = mult(arr, 6);
    printf("r: %d \n", r);
    return 0;
}