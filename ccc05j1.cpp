#include<iostream>
using namespace std;

int d, e, w;



int solve(int d, int e, int w, int dm, int em, int wm){
    return (d*dm)+(e*em)+(w*wm);
}

int main(){
    cin.tie(NULL);
    cin >> d >> e >> w;
    float a, b;
    if (d >= 100)
        a = solve(25, 15, 20, d-100, e, w)/100.0;
    
    else 
        a = solve(25, 15, 20, 0, e, w)/100.0;

    if (d >= 250)
        b = solve(45, 35, 25, d-250, e, w)/100.0;
    
    else 
        b = solve(45, 35, 25, 0, e, w)/100.0;

    cout << "Plan A costs " << a << endl << "Plan B costs " << b << endl; if (a > b){ cout << "Plan B is cheapest.";} else if (b > a){ cout << "Plan A is cheapest.";}else{ cout << "Plan A and B are the same price."; }

    return 0;
}