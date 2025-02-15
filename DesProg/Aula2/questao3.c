#include <stdio.h>

void cumulativo(int v[], int n){
    if (n == 1){
        return;
    }
    cumulativo(v, n-1);
    v[n-1] += v[n-2];
}

int main(){
    cumulativo({1,2,3}, 3);
    return 0;
}