#include <stdio.h>

int soma_impares(int v[], int n){
    if (n-1 < 0){
        return 0;
    }
    if (v[n-1] % 2 != 0){
        return v[n-1] + soma_impares(v, n-1);
    } else {
        soma_impares(v, n-1);
    }
}

int soma_pares(int v[], int n){
    if (n-1 < 0){
        return soma_impares(v, 7);
    }
    if (v[n-1] % 2 == 0){
        return v[n-1] + soma_pares(v, n-1);
    } else {
        soma_pares(v, n-1);
    }
}

int main(){
    int arr[] = {1,2,3,4,5,6,7};
    int r = soma_pares(arr, 7);
    printf("r: %d \n", r);
    return 0;
}