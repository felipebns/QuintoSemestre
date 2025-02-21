#include <stdio.h>


int mmc(int a, int b){
    if (b % a == 0 && a != b){
        return a;
    }

    mmc(a+1, b);

}


int main(){
    int r = mmc(2, 19);
    printf("r: %d \n", r);
    return 0;
}
