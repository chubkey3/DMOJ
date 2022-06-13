#include <iostream>
#include <algorithm>

using namespace std;

int a, n;

int main(){
    cin >> n;
    int b[n];
    for (int i = 0; i<n; i++){
        cin >> a;
        b[i] = a;
    }
    
    cout << *min_element(b, b+n) << "\n" << *max_element(b, b+n) << "\n";

    return 0;
}