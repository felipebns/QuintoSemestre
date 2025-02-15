#include <stdio.h>

double pot(float b, int e){
    if (e == 0){
        return 1;
    } else if (e < 0){
        return pot(b, e + 1) / b;
    } else {
        return b * pot(b, e - 1);
    }
}

int main(){
    double r = pot(2, -3);
    printf("r: %f \n", r);
    return 0;
}