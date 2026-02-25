#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

int N;
int popul[11];
int graph[11][11];
bool visit[11];
int ans;


bool init()
{
	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		cin >> popul[i];
	}

	int zero_cnt = 0;

	for (int y = 0; y < N; ++y)
	{
		int t;
		cin >> t;

		if (t == 0)
			zero_cnt += 1;

		for (int x = 0; x < t; ++x)
		{
			int k;
			cin >> k;

			graph[y][k-1] = 1;
		}
	}

	ans = 1e9;

	if (N > 2 && zero_cnt > 2)
		return false;
	return true;
}

bool isConnected(vector<int> vi)
{
	if (vi.size() == 0)
		return false;

	queue<int> q;
	bool visit_tmp[11] = { false, };


	// 첫번째 node부터 bfs
	q.push(vi[0]);
	visit_tmp[vi[0]] = true;

	while(!q.empty())
	{
		int t = q.front(); q.pop();

		for (int i = 0; i < N; ++i)
		{
			if (visit_tmp[i] == true)
				continue;

			if (find(vi.begin(), vi.end(), i) == vi.end())
				continue;

			if (graph[t][i] == 1)
			{
				visit_tmp[i] = true;
				q.push(i);
			}
		}
	}

	for (const auto& e : vi)
	{
		if (visit_tmp[e] == false)	// 방문하지 못함
			return false;
	}

	return true;
}



void dfs(int depth)
{
	if (depth == N)
	{
		vector<int> vi1, vi2;
		for (int i = 0; i < N; ++i)
		{
			if (visit[i])
				vi1.push_back(i);
			else
				vi2.push_back(i);
		}


		if (!isConnected(vi1) || !isConnected(vi2))
			return;

		//cout << "q1: ";
		//for (const auto& e : vi1)
		//	cout << e << " ";
		//cout << "                  q2: ";
		//for (const auto& e : vi2)
		//	cout << e << " ";

		int total = 0;
		for (const auto& e : vi1)
			total += popul[e];
		for (const auto& e : vi2)
			total -= popul[e];

		ans = min(ans, abs(total));
		//cout <<  total << " \n";

		return;
	}

	// 탐색
	visit[depth] = false;
	dfs(depth + 1);

	visit[depth] = true;
	dfs(depth + 1);
}


int solve()
{
	bool b = init();

	if (b == false)
		return -1;

	visit[0] = false;
	dfs(1);
	//dfs(1); // 어차피 반전돼서 할 필요 x	

	return ans == 1e9 ? -1 : ans;
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cout << solve();

	return 0;
}