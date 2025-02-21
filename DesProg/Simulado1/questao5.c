int equilibrio(int v[], int l, int r){
    if (l >= r){
        return 1;
    }
    return v[l] == v[r] && equilibrio(v, l+1, r-1); //Ele olha primeiro da esquerda para a direita, tem que ser sem +/-
}