#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int N;
int mat[21][21];
int visit[21][21];

typedef pair<int, int> coord;
coord dirs[4] = {	// rb부터 시계방향
	{1,1}, {1,-1}, {-1,-1}, {-1,1}
};

int max_path;
int path[101];
int turn_cnt;
int ty, tx;

void init()
{
	cin >> N;

	memset(mat, 0, sizeof(mat));

	for (int y = 0;y < N;++y)
		for (int x = 0;x < N;++x)
			cin >> mat[y][x];

	max_path = -1;
}

bool isValid(int y, int x)
{
	if (y < 0 || y >= N) return false;
	if (x < 0 || x >= N) return false;
	return true;
}


void dfs(int y, int x)
{
	if (y == ty && x == tx && turn_cnt == 3)
	{
		int tmp = 0;
		for (const auto& t : path)
			tmp += t;
		max_path = max(max_path, tmp);

		//cout << ty << " " << tx << " \n";

		//for (int i = 0;i < N;++i) {
		//	for (int j = 0;j < N;++j) {
		//		cout << visit[i][j] << " ";
		//	}
		//	cout << "\n";
		//}

		return;
	}

	for (int i = 0;i < 2;++i)
	{
		int turn_next = turn_cnt + i;

		if (turn_next == 4)
		{
			continue;
		}

		int ny = y + dirs[turn_next].first;
		int nx = x + dirs[turn_next].second;

		if (!isValid(ny, nx)) continue;
		if (visit[ny][nx] == 1) continue;
		if (path[mat[ny][nx]] == 1) continue; // 이미 방문

		visit[ny][nx] = 1;
		path[mat[ny][nx]] = 1;
		turn_cnt += i;

		dfs(ny, nx);

		turn_cnt -= i;
		path[mat[ny][nx]] = 0;
		visit[ny][nx] = 0;
	}
}


int solve()
{
	init();

	for (int y = 0;y < N;++y)
	{
		for (int x = 0;x < N;++x)
		{
			//y = 0, x = 2;
			//y = 1, x = 4;
			memset(visit, 0, sizeof(visit));
			memset(path, 0, sizeof(path));
			ty = y, tx = x;
			turn_cnt = 0;

			dfs(y, x);
		}
	}

	return max_path;
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