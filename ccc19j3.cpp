#include<iostream>
#include<string>
using namespace std;

string i;

int n;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int x = 0; x < n; x++){
        cin >> i;
        char temp = i[0];
        int seen = 0;
        //cout << sizeof(i);
        for (long long unsigned int k = 0; k<=i.length(); k++){
            if (i[k] == temp){
                seen += 1;
            }else {
                cout << seen << " " << temp << " ";
                seen = 1;
                temp = i[k];
            }
        }
        cout << "\n";
    }
    return 0;
}