#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using  namespace std;

vector<vector<int>> mat;
int N;
vector<pair<int, int>> dirs = {
	{-1,-1}, {-1,1}, {1,1},{1,-1}
};
int ty, tx;
int maxCnt;
vector<bool> visitNum;
//vector<vector<bool>> visitMat;

void init()
{
	cin >> N;

	mat.assign(N, vector<int>(N, 0));

	for (int y = 0; y < N; ++y)
		for (int x = 0; x < N; ++x)
			cin >> mat[y][x];

	visitNum.assign(101, false);
	//visitMat.assign(N, vector<bool>(N, false));

	maxCnt = -1;
}


bool isValid(int y, int x) {
	if (y < 0 || y >= N) return false;
	if (x < 0 || x >= N) return false;
	return true;
}

void dfs(int y, int x, int cnt, int dirCnt)
{
	if (y == ty && x == tx && dirCnt > 1) {
		maxCnt = max(maxCnt, cnt);
		return;
	}

	for (int dirCntCur = dirCnt; dirCntCur < dirCnt + 2; ++dirCntCur) {	// 한쪽 방향으로만 돌아도 ㄱㅊ
		if (dirCntCur >= 4)
			break;

		auto d = dirs[dirCntCur];
		int cy = y + d.first;
		int cx = x + d.second;

		// 예외 처리
		if (!isValid(cy, cx))
			continue;

		if (!visitNum[mat[cy][cx]] /* && !visitMat[cy][cx]*/) {
			// 탐색
			visitNum[mat[cy][cx]] = true;
			//visitMat[cy][cx] = true;

			dfs(cy, cx, cnt + 1, dirCntCur);

			//visitMat[cy][cx] = false;
			visitNum[mat[cy][cx]] = false;
		}
		else if (cy == ty && cx == tx) {
			dfs(cy, cx, cnt + 1, dirCnt + 1);	// 실질적인 종료 조건
		}
	}
}


int solve()
{
	init();

	for (int y = 0; y < N; ++y)
		for (int x = 1; x < N - 1; ++x) {
			//y = 2, x = 1;
			ty = y;
			tx = x;

			visitNum[mat[y][x]] = true;
			dfs(y, x, 0, 0);
			visitNum[mat[y][x]] = false;
		}

	return maxCnt;
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