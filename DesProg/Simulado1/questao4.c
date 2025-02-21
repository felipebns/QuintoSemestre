int mdc(a, b){
    if (a == 0){
        return b;
    }
    if (b == 0){
        return a;
    }


    if (a > b){
        mdc(a-b, b);
    } else if (b > a){
        mdc(a, b-a);
    } else if (b == a){
        return a;
    }
}

int main (){
    printf("%d \n", mdc(7,11));
    return 0;
}