#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> cities;
vector<signed int> temps;

int main(){
    string city;
    string end = "Waterloo";
    signed int temp;
    while (true){
        cin >> city >> temp;
        cities.push_back(city);
        temps.push_back(temp);
        if (city.compare(end) == 0){
            break;
        }
    }

    //cout << *min_element(temps.begin(), temps.end()) << endl;
    signed int highest = *min_element(temps.begin(), temps.end());
    //cout << highest << typeid(highest).name() << endl;
    vector<int>::iterator it = find(temps.begin(), temps.end(), highest);
    int index = distance(temps.begin(), it);
    cout << cities[index];
    
    return 0;
}