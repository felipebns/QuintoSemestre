#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

#define TAMANHO 5

void init_torres(int torres[3][TAMANHO]){

    for (int i =(TAMANHO-1); i>=0; i--){
        torres[0][i] = (TAMANHO-1)-i;
        torres[1][i] = 0;
        torres[2][i] = 0;
    }
    

}
void mover(int *t_origem, int *t_destino){
    int disco = 0;
    int placement = 100;
    int remover;
    for (int i = 0; i<TAMANHO; i++){
        if (t_origem[i] == 0 && disco == 0){
            disco = t_origem[i-1];
            remover = i-1;
            

        }
        if (t_destino[i] == 0 && placement==100){
            placement = i;
        }
    }

    if (t_destino[placement-1] < disco && placement!=0){
        printf("erro, o disco de baixo é menor\n");
        sleep(2);
    }
    else{
        t_origem[remover] = 0;
        t_destino[placement] = disco;
    }   
}



// void solve_torre(int *t1, int *torres[1], int *torres[2]){

// }
void print_torres(int torres[3][TAMANHO]){
    
    for (int i=(TAMANHO-1); i>=0; i--){
        printf("%d:             %d    %d    %d\n" , i, torres[0][i], torres[1][i], torres[2][i]);
    }
    printf("\n\n\n");
}

int main(){
    

    int torres[3][TAMANHO];

    init_torres(torres);

    print_torres(torres);

    

    while (1){
        system("clear");
        print_torres(torres);
        
        int origem;
        int destino; 

        printf("origem  ->");

        scanf(" %d", &origem);
        printf("destino  ->");
        scanf(" %d", &destino);

        mover(torres[origem-1], torres[destino-1]);
        
        
    }
    return 1;
}