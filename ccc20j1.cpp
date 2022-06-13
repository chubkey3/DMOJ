#include <bits/stdc++.h>

using namespace std;
int s, m, l;
int main() {
    cin >> s;
    cin >> m;
    cin >> l;
    if (s+2*m+3*l >= 10){
        cout << "happy";
    } else {
        cout << "sad";
    }
    return 0;
}