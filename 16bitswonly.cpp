#include <stdio.h>

int main(){
    int n, a, b, c;
    
    scanf("%d", &n);
    
    for (int x = 0; x<n; x++){
        scanf("%d %d %d", &a, &b, &c);
        if (a*b == c){
            printf("POSSIBLE DOUBLE SIGMA\n");
        } else {
            printf("16 BIT S/W ONLY\n");
            
        }
    }
    return 0;
}