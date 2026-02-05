#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using  namespace std;
int D, W, K;
int mat[50][50];
int min_k;
vector<bool> levels;
bool is_found;

void init()
{
	cin >> D >> W >> K;

	for (int y = 0; y < D; y++)
		for (int x = 0; x < W; ++x)
			cin >> mat[y][x];

	min_k = D;
	levels.assign(D, false);
	is_found = false;
}

// K개 되는지 검사
void test()
{
	bool tmp_found;
	int tmp_cnt;

	for (int x = 0; x < W; ++x) {
		tmp_found = false;
		tmp_cnt = 1;

		for (int y = 1; y < D; ++y) {
			if (mat[y][x] == mat[y - 1][x])
				tmp_cnt++;
			else
				tmp_cnt = 1;

			if (tmp_cnt == K) {
				tmp_found = true;
				break;
			}
		}

		if (!tmp_found)
			return;
	}

	is_found = true;
	return;
}


void dfs(int cur, int tar, int prev_level)
{
	if (cur == tar) {
		test();
		return;
	}

	for (int y = prev_level; y < D; ++y) {	// 각 row마다. 이전보다 아래 row만 해야됨
		if (levels[y])	// 이전이랑 같은 row는 skip
			continue;

		// 현재 col에 투약
		int backup[50];
		levels[y] = true;
		copy(begin(mat[y]), end(mat[y]), begin(backup));

		// 다음 투약할 row로 dfs 진행
		fill(begin(mat[y]), end(mat[y]), 0);
		dfs(cur + 1, tar, y + 1);

		fill(begin(mat[y]), end(mat[y]), 1);
		dfs(cur + 1, tar, y + 1);

		// 복구
		copy(begin(backup), end(backup), begin(mat[y]));
		levels[y] = false;
	}
}


int solve()
{
	init();

	int cnt = 0;

	// 순정일때 검사
	test();

	if (is_found or K == 1)
		return cnt;

	// 1씩 증가시키며 검사
	while (++cnt <= K) {
		dfs(0, cnt, 0);

		if (is_found)
			break;
	}

	return cnt;
}


int main()
{
	int tc;
	cin >> tc;

	for (int i = 1; i < tc + 1; ++i) {
		cout << "#" << i << " " << solve() << endl;
	}
	return 0;
}