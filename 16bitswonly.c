#include <stdio.h>

int main(){
    short n;
    long int a, b, c;
    
    scanf("%hu", &n);
    
    for (short x = 0; x<n; x++){
        scanf("%li %li %li", &a, &b, &c);
        if (a*b != c){
            printf("16 BIT S/W ONLY\n");
        } else {
            printf("POSSIBLE DOUBLE SIGMA\n");
        }
    }
    return 0;
}