#include <bits/stdc++.h>

using namespace std;

int p, n, r;

int main(){
	//inputs
	cin >> p;
	cin >> n;
	cin >> r;

	int t = n;
	int d = 0;

	while (true){
		t = t*r;
		n += t;
		d++;
		if (n > p){
			break;
		}
	}
	cout << d;
	return 0;
}