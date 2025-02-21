#include <stdio.h>

int diferenca(int v[], int l, int r) {
    if (r < l) {
        return 0;
    }
    
    if (v[r] < 0){
        return diferenca(v, l, r-1) - 1;
    } else if (v[r] > 0){
        return diferenca(v, l, r-1) + 1;
    } else if (v[r] == 0){
        return diferenca(v, l, r-1);
    }
}

int main(){
    int v[] = {1,2,-3};
    printf("%d \n", diferenca(v, 0, 2));
    return 0;
}