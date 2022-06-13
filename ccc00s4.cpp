#include <iostream>

using namespace std;

int n, d, g, c;

int * clubs;

int * k;

int main(){
    cin >> d;
    cin >> g;
    k = new int [d+1];
    for (int x = 0; x<d+1; x++){
        k[x] = 0;
    }
    clubs = new int [g];
    for (int x = 0; x<g; x++){
        cin >> c;
        clubs[x] = c;
    }
    for (int x = 1; x<d+1; x++){
        for (int y = 0; y<g; y++){
            if (x-clubs[y] >= 0 and k[x-clubs[y]] != -1) {
                int outcome = k[x-clubs[y]]+1;
                if (outcome < k[x] or k[x] == 0){
                    k[x] = outcome;
                }
            }
        }
        if (k[x] == 0){
            k[x] = -1;
        }
    }
    if (k[d] == -1){
        cout << "Roberta acknowledges defeat.";
    } else {
        cout << "Roberta wins in " << k[d] << " strokes.";
    }
    return 0;
}