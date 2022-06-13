#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){

    unsigned short arr[100];
    unsigned short n;

    scanf("%hu", &n);

    for (unsigned short i = 0; i<n; i++){
        scanf("%hu", &arr[i]);
    }
    
    sort(arr, arr+n);

    for (unsigned short i = 0; i<n; i++){
        printf("%hu\n", arr[i]);
    }

    return 0;
}