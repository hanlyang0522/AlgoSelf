#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int D, W, K;
int mat[14][21];
int min_depth;


typedef pair<int, int> coord;
coord dirs[4] = {
	{-1,0}, {0,1}, {1,0}, {0,-1}
};


void init()
{
	cin >> D >> W >> K;

	for (int y = 0;y < D;++y)
		for (int x = 0;x < W;++x)
			cin >> mat[y][x];

	min_depth = D + 1;
}

bool isValid()
{
	for (int x = 0;x < W;++x)
	{
		bool b = false;
		int cnt = 1;

		for (int y = 1;y < D;++y)
		{
			if (mat[y][x] == mat[y - 1][x])
				cnt += 1;
			else
				cnt = 1;

			if (cnt == K)
			{
				b = true;
				break;
			}
		}

		if (!b)
			return false;
	}

	return true;
}

void dfs(int cur_depth, int cur_idx)
{
	if (cur_depth > min_depth)
		return;

	if (cur_depth == K) 
	{
		min_depth = min(min_depth, K);
		return;
	}

	if (isValid())
	{
		min_depth = min(min_depth, cur_depth);
		return;
	}


	for (int i = cur_idx+1; i < D;++i)
	{
		int tmp[21];
		memcpy(&tmp, &mat[i], sizeof(mat[i]));

		// a
		//memset(mat[i], 0, sizeof(mat[i]));
		fill(mat[i], mat[i] + W, 0);
		dfs(cur_depth + 1, i);

		// b
		//memset(mat[i], 1, sizeof(mat[i]));
		fill(mat[i], mat[i] + W, 1);
		dfs(cur_depth + 1, i);

		memcpy(&mat[i], &tmp, sizeof(mat[i]));
	}
}


int solve()
{
	init();

	if (isValid())
		return 0;

	//for (int y = 0;y < D;++y)
	//	dfs(0, y);
	dfs(0, -1);

	return min_depth;
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