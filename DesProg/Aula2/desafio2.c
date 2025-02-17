#include <stdio.h>

void hanoi(int n, char orig, char aux, char dest){
    if (n == 1){
        printf("mova o disco %d da torre %c para a torre %c \n", n, orig, dest);
        return;
    }
    
    hanoi(n-1, orig, dest, aux);
    
    printf("mova o disco %d da torre %c para a torre %c \n", n, orig, dest);
    
    hanoi(n-1, aux, orig, dest);
}

int main(){
    hanoi(3, 'A', 'B', 'C');
    return 0;
}