#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> mul_odd(vector<int>src) {
	vector<int> dst;
	int sum = 0, carry = 0;

	sum = src[0] * 2 + carry - 1;
	carry = sum / 10;
	dst.push_back(sum % 10);

	for(int i = 1; i < src.size(); i++) {
		sum = src[i] * 2 + carry;
		carry = sum / 10;
		dst.push_back(sum % 10);
	}
	if(carry == 1)
		dst.push_back(1);

	return dst;
}

vector<int> mul_even(vector<int>src) {
	vector<int> dst;
	int sum = 0, carry = 0;

	sum = src[0] * 2 + carry+1;
	carry = sum / 10;
	dst.push_back(sum % 10);

	for(int i = 1; i < src.size(); i++) {
		sum = src[i] * 2 + carry;
		carry = sum / 10;
		dst.push_back(sum % 10);
	}
	if(carry == 1)
		dst.push_back(1);

	return dst;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int a;
	vector<vector<int>> arr(1001, vector<int>());
	vector<int> ans;
	string ansstr;

	arr[0].push_back(0);
	arr[1].push_back(0);

	for(a = 2; a < 1001; a++) {
		if(a & 1)
			arr[a] = mul_odd(arr[a - 1]);
		else
			arr[a] = mul_even(arr[a - 1]);
	}

	while(cin >> a) {
		ans = arr[a];
		ansstr = "";
		for(int i = ans.size()-1; i > -1; i--)
			ansstr += to_string(ans[i]);
		cout << ansstr << endl;
	}

}