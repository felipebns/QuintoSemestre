#include <stdio.h>


void acumulo(int v[], int n){
    if (n == 1){
        return;
    }
    
    acumulo(v, n-1);
    v[n-1] += v[n-2];
}


int main(){
    int v[6] = {1,2,3,4,5,6};
    acumulo(v, 6);
    printf("r: %d \n", r);
    return 0;
}
