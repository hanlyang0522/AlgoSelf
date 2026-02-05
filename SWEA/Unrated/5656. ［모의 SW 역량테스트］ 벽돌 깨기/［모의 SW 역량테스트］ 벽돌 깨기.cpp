#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using  namespace std;


vector<vector<int>> mat_orig;
int N, W, H;
vector<int> path;
//int cnt = 0;
int min_block;

pair<int, int> dirs[] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };


void init()
{
	cin >> N >> W >> H;

	mat_orig.assign(W, vector<int>(H, 0));

	// 90도 회전
	for (int y = 0; y < H; ++y)
		for (int x = 0; x < W; ++x)
			cin >> mat_orig[x][H - 1 - y];

	//// 검증
	//cout << endl;
	//for (int y = 0; y < W; ++y) {
	//	for (int x = 0; x < H; ++x)
	//		cout << mat_orig[y][x] << " ";
	//	cout << endl;
	//}

	path.clear();
	min_block = N * H * W;
}

void bfs()
{
	vector < vector<int>> mat = mat_orig;

	//path = { 5,3,0 };

	for (const auto& w : path) { // w: 떨어트릴 y coord
		if (mat[w][0] == 0)	// 빈 곳 있으면 skip
			break;

		vector<pair<int, int>> q;
		int idx = H;

		// 첫번째 폭탄
		while (--idx >= 0) {
			if (mat[w][idx] != 0) {
				q.emplace_back(w, idx);
				break;
			}
		}

		// 연쇄
		while (q.size() > 0) {
			// pop
			pair<int, int> pop = q.back();
			q.pop_back();
			//cout << pop.first << " " << pop.second << endl;
			int y = pop.first, x = pop.second;

			int length = mat[y][x];
			mat[y][x] = 0;

			// 주변 폭탄 담기
			for (int n = 0; n < length; ++n) {
				for (auto d : dirs) {
					int dy = d.first;
					int dx = d.second;
					int ny = y + n * dy;
					int nx = x + n * dx;

					if (ny < 0 || ny >= W || nx < 0 || nx >= H)
						continue;

					//cout << ny << " " << nx << " ";

					if (mat[ny][nx] > 0) {
						q.emplace_back(ny, nx);
						//cout << "ADD!";
					}
					//cout << endl;
				}
				//cout << endl;
			}

			// 폭발
		}

		// 정렬
		for (vector<int>& row : mat) {
			row.erase(remove(row.begin(), row.end(), 0), row.end());
			row.resize(H);
		}

		//cout << endl;
		//for (int y = 0; y < W; ++y) {
		//	for (int x = 0; x < H; ++x)
		//		cout << mat[y][x] << " ";
		//	cout << endl;
		//}
	}

	int block_cnt = 0;

	for (int y = 0; y < W; ++y)
		for (int x = 0; x < H; ++x)
			if (mat[y][x] != 0)
				++block_cnt;

	min_block = min(min_block, block_cnt);

	//cout << endl;
}

void dfs()
{
	if (path.size() == N) {	// 길이 N 도달하면 폭탄 실험
		bfs();

		return;
	}

	for (int x = 0; x < W; ++x) {
		path.push_back(x);
		dfs();
		path.pop_back();

		if (min_block == 0)
			return;
	}
}


int solve()
{
	init();

	dfs();

	return min_block;
}


int main()
{
	int tc;
	cin >> tc;

	for (int i = 1; i < tc + 1; ++i) {
		cout << "#" << i << " " << (solve()) << endl;
	}


	//cout << cnt;
	return 0;
}