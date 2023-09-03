#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int tree[2001];
vector<int> vec[2001];
long long ans = 0;

int N, M, a, b;
	
void update(int i) {
	while(i <= N) {
		tree[i] += 1;
		i += (i & -i);
	}
}

int query(int i) {
	int res = 0;
	
	while(i) {
		res += tree[i];
		i -= (i & -i);
	}
	return res;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	// 간선 입력
	while(M--){
		cin >> a >> b;
		vec[a].push_back(b);
	}

	// 펜윅
	for(int i=0;i<N+1;i++){
	    sort(vec[i].begin(), vec[i].end());
	    
	    for(vector<int>::iterator j = vec[i].begin(); j != vec[i].end(); ++j){
    		update(*j);
	    	ans += (query(N) - query(*j));
	    }
	}

	cout << ans;
}