#include <iostream>
#include <vector>

using namespace std;



int N;

vector<int> vi;


int fibo(int n)
{
    if (vi[n] != -1)
        return vi[n];

    vi[n] = fibo(n - 1) + fibo(n - 2);

    return  vi[n];
}


int solve()
{
    cin >> N;
    vi.assign(N + 1, -1);
    vi[0] = 0;
    vi[1] = 1;

    return fibo(N);
}


int main() {
    cout << solve();
    return 0;
}