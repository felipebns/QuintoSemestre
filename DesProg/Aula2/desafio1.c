#include <stdio.h>

int somaAux(int v[], int inicio, int fim){

    if (inicio == fim){
        return v[inicio];
    }

    int meio = (int) (inicio + fim)/2;

    int esquerda = somaAux(v, inicio, meio);
    int direita = somaAux(v, meio + 1, fim);

    return direita + esquerda;
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