#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int N, M, R, C, L;
int mat[51][51];
int visit[51][51];

typedef pair<int, int> coord;
coord dirs[4] = {
	{-1,0}, {0,1}, {1,0}, {0,-1}
};


void init()
{
	cin >> N >> M >> R >> C >> L;
	memset(mat, 0, sizeof(mat));
	memset(visit, 0, sizeof(visit));

	for (int y = 0;y < N;++y)
		for (int x = 0;x < M;++x)
			cin >> mat[y][x];
}


bool isValid(int y, int x)
{
	if (y < 0 || y >= N) return false;
	if (x < 0 || x >= M) return false;
	return true;
}

bool isConnect(int cy, int cx, int ny, int nx, int dir)
{
	int c = mat[cy][cx];
	int n = mat[ny][nx];

	if (n == 0) return false; // 없음

	bool b = false;

	switch (dir)
	{
	case 0:	// top
		if ((c == 1 || c == 2 || c == 4 || c == 7)
			&& (n == 1 || n == 2 || n == 5 || n == 6))
			b = true;
		break;
	case 1:	// right
		if ((c == 1 || c == 3 || c == 4 || c == 5)
			&& (n == 1 || n == 3 || n == 6 || n == 7))
			b = true;
		break;
	case 2:	// bot
		if ((c == 1 || c == 2 || c == 5 || c == 6)
			&& (n == 1 || n == 2 || n == 4 || n == 7))
			b = true;
		break;
	case 3:	// left
		if ((c == 1 || c == 3 || c == 6 || c == 7)
			&& (n == 1 || n == 3 || n == 4 || n == 5))
			b = true;
		break;
	}

	return b;
}


int bfs(int y, int x)
{
	int v_cnt = 1;	// 방문
	int time = 0;	// 시간

	queue<coord> q;
	q.push({ y,x });
	visit[y][x] = 1;

	while (!q.empty())
	{
		if (++time == L)
			break;

		int it = q.size();

		for (int i = 0;i < it;++i)
		{
			coord curr = q.front(); q.pop();
			int cy = curr.first;
			int cx = curr.second;

			//for (const auto& d : dirs)
			for (int d_it = 0;d_it < 4;++d_it)
			{
				coord d = dirs[d_it];
				int ny = cy + d.first;
				int nx = cx + d.second;

				if (!isValid(ny, nx)) continue;
				if (visit[ny][nx]) continue;
				if (!isConnect(cy, cx, ny, nx, d_it)) continue;

				visit[ny][nx] = 1;
				v_cnt += 1;
				q.push({ ny,nx });
			}
		}
	}

	//cout << "\n";
	//for (int i = 0;i < N;++i)
	//{
	//	for (int j = 0;j < M;++j) {
	//		cout << visit[i][j] << " ";
	//	}
	//	cout << "\n";
	//}

	return v_cnt;
}

int solve()
{
	init();

	return bfs(R, C);
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