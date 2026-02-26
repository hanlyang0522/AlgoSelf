#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


int N;
vector<int> vi;

void init()
{
    cin >> N;
    vi.assign(N + 1, -1);

    vi[0] = 0;
    vi[1] = 1;
    vi[2] = 2;
}

int dp(int n)
{
    if (vi[n] != -1)
        return vi[n];

    vi[n] = (dp(n - 1) + dp(n - 2)) % 10007;

    return vi[n];
}

int solve()
{
    init();

    return dp(N);
}


int main() {
    cout << solve();
    int k = 3;
    return 0;
}