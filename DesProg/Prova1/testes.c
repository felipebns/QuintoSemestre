#include <stdio.h>

int lawrence(int n) {
    if (n == 256) {
        printf("b: %d\n", n);
        return n;
    }
    printf("%d {\n", n);
    int r = lawrence(4 * n) / 2;
    printf("} %d\n", r);
    return r;
}

int bellini(int n) {
    if (n == 1) {
        printf("b: %d\n", n);
        return n;
    }
    printf("%d {\n", n);
    int r = bellini(n - 2) + bellini(n - 2);
    printf("} %d\n", r);
    return r;
}

int trembley(int n) {
    if (n >= 5) {
        printf("b: %d\n", n);
        return n;
    }
    printf("%d {\n", n);
    int r = trembley(2 * n) / 3 + trembley(3 * n) / 2;
    printf("} %d\n", r);
    return r;
}

int main(){
    // lawrence(1);
    // bellini(7);
    trembley(1);
    return 0;
}