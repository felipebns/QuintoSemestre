void cumulativo(int v[], int n){
    if (n == 1){
        return;
    }

    cumulativo(v, n-1);
    if (v[n-1] < v[n-2]){
        v[n-1] = v[n-2];
    }
}