#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cmath>

using namespace std;


vector<pair<int, int>> dirs{
	{-1,0},{0,1},{1,0},{0,-1},
};


int N, M;
vector<vector<int>> mat;

typedef pair<int, int> coord;
//const int INF = 1e9;

void init()
{
	cin >> N >> M;

	mat.assign(N, vector<int>(N, 0));

	for (int y = 0; y < N; ++y)
		for (int x = 0; x < N; ++x)
			cin >> mat[y][x];
}


bool isValid(int y, int x)
{
	if (y < 0 || y >= N) return false;
	if (x < 0 || x >= N) return false;
	return true;
}



int bfs(int y, int x)
{
	vector<vector<bool>> visit;
	visit.assign(N, vector<bool>(N, false));

	queue<coord> q;
	q.push({ y,x });
	visit[y][x] = true;

	int home_cnt = mat[y][x];
	int home_max = 0;
	int cost = 0;
	int r = 0;

	while (!q.empty()) {
		// 서비스 가능한지 계산
		r += 1;
		cost = r * r + (r - 1) * (r - 1);

		if (home_cnt * M >= cost)
			home_max = home_cnt;

		int q_size = q.size();

		for (int i = 0; i < q_size; ++i) {
			coord curr = q.front(); q.pop();
			int cy = curr.first;
			int cx = curr.second;

			for (const auto& d : dirs) {
				int ny = cy + d.first;
				int nx = cx + d.second;

				if (!isValid(ny, nx)) continue;
				if (visit[ny][nx]) continue;

				if (mat[ny][nx] == 1)	// home update
					home_cnt += 1;

				visit[ny][nx] = true;
				q.push({ ny,nx });
			}
		}
	}

	return home_max;
}




int solve()
{
	init();

	int ans = -1;

	for (int y = 0; y < N; ++y) {
		for (int x = 0; x < N; ++x) {

			//y = 3, x = 3;
			ans = max(ans, bfs(y, x));
		}
	}

	return ans;
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int tc;
	cin >> tc;

	for (int i = 1; i <= tc; ++i)
	{
		cout << "#" << i << " " << solve() << "\n";
	}
	return 0;
}