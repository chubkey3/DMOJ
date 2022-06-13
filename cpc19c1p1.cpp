#include <iostream>

using namespace std;

int main(){
    int n, a = 1;
    cin >> n;
    while (n > a) {
        cout << a << " " << n << " ";
        a += 1;
        n -= 1;
    }
    if (n == a){
        cout << n << endl;
    } else {
        cout << endl;
    }
    return 0;
}