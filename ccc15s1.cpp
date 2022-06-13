#include<iostream>
#include<vector>
using namespace std;

int main(){
	cin.tie(NULL);
	int k;
	int sum = 0;
	cin >> k;
	vector<int> boo;
	for (int i = 0; i<k; i++){
		int a;
		cin >> a;
		boo.push_back(a);
	}
	for (long unsigned int x = 0; x<boo.size(); x++){
		if (boo[x]==0){
			boo.erase(boo.begin() + x-1);
			boo.erase(boo.begin() + x-1);
			x = 0;

		}
	}
	if (boo[boo.size()-1] == 0){
		boo.erase(boo.end()-1);
		boo.erase(boo.end()-1);
	}

	for (long unsigned int x = 0; x<boo.size(); x++){
		sum += boo[x];
	}
	cout << sum;
	return 0;
}