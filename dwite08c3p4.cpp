#include <iostream>
#include <vector>

using namespace std;

int main(){
  int m, n, t;
  for (int x = 0; x < 5; x++){
    vector<int> k(101, 100);
    k[1] = 0;
    vector<int> currencies;
    cin >> m;
    cin >> n;

    for (int y = 0; y<n; y++){
      cin >> t;
      currencies.push_back(t);
    }

    for (int i = 1; i<k.size(); i++){
      if (k[i] == 100){
        continue;
      }
      for (int l : currencies){
        if (i+l < k.size()){
          k[i+l] = min(k[i]+1, k[i+l]);
        }
      }
    }
    cout << k[m+1] << endl;
  }

  return 0;
}