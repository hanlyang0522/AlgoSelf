#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


int N;
vector<int> dp;

void init()
{
    cin >> N;
    dp.assign(N + 1, -1);

    //vi[0] = 1;
    //vi[1] = 2;
    //vi[2] = 7;
}

int doDP(int n)
{
 //   if (vi[n] != -1)
 //       return vi[n];

 //   //vi[n] = (dp(n - 1) + dp(n - 2)) % 1000000007;
	//vi[n] = (2 + dp(n - 2) * 3 + dp(n - 1) * 2) % 1000000007;

 //   return vi[n];

    dp[0] = 1;
    dp[1] = 2;

    for (int i = 2; i <= N; ++i)
    {
		dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % 1000000007;

        for (int j = i - 3; j >= 0; --j)
            dp[i] = (dp[i] +  dp[j] * 2) % 1000000007;
	}

    return dp[N];
}

int solve()
{
    init();

    return doDP(N);
}


int main() {
    cout << solve();
    int k = 3;
    return 0;
}