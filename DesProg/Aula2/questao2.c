#include <stdio.h>

int digitos(int n){
    if (n == 0){
        return 0;
    }
    return 1 + digitos((int) (n/10));
}

int main(){
    int r = digitos(20022);
    printf("r: %d \n", r);
    return 0;
}