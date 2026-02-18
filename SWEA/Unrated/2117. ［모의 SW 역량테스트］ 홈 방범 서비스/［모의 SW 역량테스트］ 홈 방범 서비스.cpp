#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int N, M;
int mat[21][21];
int visit[21][21];

typedef pair<int, int> coord;
coord dirs[4] = {
	{-1,0}, {0,1}, {1,0}, {0,-1}
};


void init()
{
	cin >> N >> M;
	memset(mat, 0, sizeof(mat));

	for (int y = 0;y < N;++y)
		for (int x = 0;x < N;++x)
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
	int home_cnt = 0;
	int home_max = 0;
	int cost = 0;
	int rds = -1;

	queue<coord> q;
	q.push({ y,x });

	memset(visit, 0, sizeof(visit));
	visit[y][x] = 1;

	//if (mat[y][x])
	//	home_cnt += 1;

	while (!q.empty())
	{
		rds += 1;
		cost = rds * rds + (rds - 1) * (rds - 1);

		if (home_cnt * M >= cost)
			home_max = home_cnt;
		
		int it = q.size();
		//cout << "rds: " << rds << " cost: " << cost <<"home_cnt: "<<home_cnt<< " it: " << it<<"\n";

		for (int i = 0;i < it;++i)
		{
			coord curr = q.front();q.pop();
			int cy = curr.first;
			int cx = curr.second;

			if (mat[cy][cx]) {
				home_cnt += 1;
				//cout << "DEBUG: " << cy << " " << cx << " \n";
			}

			for (const auto& d : dirs)
			{
				int ny = cy + d.first;
				int nx = cx + d.second;

				if (!isValid(ny, nx)) continue;
				if (visit[ny][nx]) continue;

				visit[ny][nx] = 1;
				q.push({ ny,nx });
			}
		}
	}

	rds += 1;
	cost = rds * rds + (rds - 1) * (rds - 1);

	if (home_cnt * M >= cost)
		home_max = home_cnt;

	return home_max;
}

int solve()
{
	init();

	int ans = -1;

	for (int y = 0;y < N;++y)
		for (int x = 0;x < N;++x) {
			//y = 10, x = 10;
			ans = max(ans, bfs(y, x));
		}

	return ans;
}

int main()
{
	int tc;
	cin >> tc;

	for (int i = 1;i <= tc;++i)
		cout << "#" << i << " " << solve() << "\n";

	return 0;
}