#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

double a, b, c;

long double f(long double x) {
	return a * x + b * sin(x) - c;
}

long double df(long double x) {
	return a + b * cos(x);
}

int main()
{
	fastio;

	cin >> a >> b >> c;

	double n2, n1;
	n1 = c;

	while(abs(f(n1)) > 0.000000001) {
		n2 = n1 - f(n1)/df(n1);
		n1 = n2;
		
	}
	cout << setprecision(20) << n1;
}

