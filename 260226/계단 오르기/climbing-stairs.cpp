#include <iostream>
#include <vector>

using namespace std;


int N;
vector<int> vi;

void init()
{
    cin >> N;
    vi.assign(N + 1, -1);

    vi[0] = 1e9;
    vi[1] = 1e9;
    vi[2] = 1;
    vi[3] = 1;
}


int step(int n)
{
    if (vi[n] != -1)
        return vi[n];

	vi[n] = min(step(n - 2) + 1, step(n - 3) + 1);

    return  vi[n];
}


int solve()
{
    init();

    if (N == 0 || N == 1)
        return 0;

    return step(N)%10007;
}


int main() {
    cout << solve();
    int k = 3;
    return 0;
}