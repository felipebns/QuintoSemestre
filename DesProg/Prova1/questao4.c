int num_bits(int n) {
    if (n <= 1){
        return 1;
    }

    return num_bits((int) n/2) + 1;
}