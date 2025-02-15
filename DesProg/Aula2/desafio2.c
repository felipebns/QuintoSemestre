#include <stdio.h>

void hanoi(int n, char orig, char aux, char dest){
    if (n == 0){
        return;
    }
    printf("mova o disco %d da torre %s para a torre %s", n, )
    hanoi(n-1, orig, aux, dest);
}

int main(){
    hanoi(3, 'A', 'B', 'C');
    return 0;
}