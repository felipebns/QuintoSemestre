#include <stdio.h>


int simetrico(int v[], int l, int r){
    if (l >= r){
        return 1;
    }

    return v[l] == v[r] && simetrico(v, l+1, r-1);
}


int main(){
    int v[6] = {6,5,4,3,4,5,6};
    int r = simetrico(v, 0, 6);
    printf("r: %d \n", r);
    return 0;
}
