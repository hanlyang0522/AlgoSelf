#include <iostream>
#include <vector>

using namespace std;



int N;

vector<int> vi;


int fibo(int N)
{
    if (N == 0)
    {
        return 0;
    }
    else if(N==1)
    {
        return 1;
    }

    return fibo(N - 1) + fibo(N - 2);
}


int solve()
{
    cin >> N;
    vi.assign(N + 1, -1);

    return fibo(N);
}


int main() {
    cout << solve();
    return 0;
}