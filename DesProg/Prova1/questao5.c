void derivada(int v[], int n) {
    if (n == 1){
        return;
    }
    derivada(v, n-1);
    v[n-2] = v[n-2] - v[n-1];
}