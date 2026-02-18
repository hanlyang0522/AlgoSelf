#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int N, K;
string s;

void init()
{
	cin >> N >> K;
	cin >> s;
}


int solve()
{
	init();

	const int div = N / 4;

	vector<string> res;

	for (int i = 0;i < N;++i)
	{
		for (int j = 0;j < N;j += div)
		{
			string tmp = s.substr(j, div);

			auto it = find(res.begin(), res.end(), tmp);
			if (it == res.end())
			{
				res.push_back(tmp);
			}
		}

		rotate(s.begin(), s.begin() + 1, s.end());
	}


	sort(res.begin(), res.end(), [](auto &a, auto&b){
		if (a > b) return true;
		else return false;
	});


	string fin = res[K - 1];

	int res_to_num = 0;

	for (int i = 0;i < div;++i)
	{
		char c = fin[div - 1 - i];
		int tmp;

		if (c >= 'A' && c <= 'F')
			tmp = c - 'A' + 10;
		else
			tmp = c - '0';

		res_to_num += tmp * pow(16, i);
	}


	return res_to_num;
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int tc;
	cin >> tc;

	for (int i = 1;i <= tc;++i)
		cout << "#" << i << " " << solve() << "\n";

	return 0;
}