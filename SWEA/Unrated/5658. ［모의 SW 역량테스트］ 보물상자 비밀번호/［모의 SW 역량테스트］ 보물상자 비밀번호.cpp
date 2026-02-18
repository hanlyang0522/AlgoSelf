#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>

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

	set<string, greater<string>> res;

	for (int i = 0;i < div;++i)
	{
		for (int j = 0;j < N;j += div)
		{
			string tmp = s.substr(j, div);
			res.insert(tmp);
		}

		rotate(s.begin(), s.begin() + 1, s.end());
	}

	auto it = res.begin();
	advance(it, K - 1);

	return stoll(*it, nullptr, 16);
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