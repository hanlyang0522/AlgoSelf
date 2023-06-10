#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void update(vector<int>& tree, int i) {
	int tsize = tree.size();

	while(i < tsize) {
		tree[i] += 1;
		i += (i & -i);
	}
}

int sum(vector<int>& tree, int i) {
	long long res = 0;
	while(i > 0) {
		res += tree[i];
		i -= (i & -i);
	}
	return res;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	// 간선 입력
	vector<pair<int, int>> vec;
	vec.reserve(M + 1);

	int a, b;
	for(register unsigned int i = 0; i < M; i++) {
		cin >> a >> b;
		vec.push_back(pair<int, int>(a, b));
	}
	sort(vec.begin(), vec.end());


	// 펜윅
	int tree_size = N + 1;
	vector<int> tree(tree_size);

	long long ans = 0;

	for(vector<pair<int, int>>::iterator i = vec.begin(); i != vec.end(); ++i) {
		update(tree, i->second);
		ans += (sum(tree, N) - sum(tree, i->second));
	}

	cout << ans << '\n';
}