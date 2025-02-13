#include <stdio.h>

void incrementa(int n) {
    printf("comecou %d\n", n);
    if (n < 3){
        incrementa(n + 1);
    }
    printf("terminou %d\n", n);
}

void decrementa(int n) {
    printf("comecou %d\n", n);
    if (n > 0){
        decrementa(n - 1);
    }
    printf("terminou %d\n", n);
}


int main(){
    // incrementa(1);
    decrementa(2);

    return 0;
}