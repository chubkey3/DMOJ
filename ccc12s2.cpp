#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

string input;

int convert(char x){
    char conversion[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    char *test = find(begin(conversion), end(conversion), x);
    int d = distance(conversion, test);
    int i = floor(d/2);
    int base = pow(10, i);
    if (d%2 == 1){
        base *= 5;
    }
    return base;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> input;
    vector<signed int> sumnums;
    int highest = 0;
    int sum = 0;

    for (long int x = input.length()-1; x>-1; x -= 2){
        int val = input[x-1]-48;
        int base = convert(input[x]);
        if (base >= highest){
            highest = base;
            sumnums.insert(sumnums.begin(), val*base);
            //cout << val*base << "+" << endl;
        } else if (base < highest){
            sumnums.insert(sumnums.begin(), -val*base);
            //cout << val*base << "-" << endl;   
        }
        
    }

    for (long unsigned int x = 0; x<sumnums.size(); x++){
        sum += sumnums[x];
    }
    
    cout << sum << endl;
    return 0;
}