# 범위에 따라 T/F 나뉨 -> binary search?, 최솟값 찾기라 X
# 한 node 기준으로 subtree & 전체-subtree
# 각 node의 son이 몇갠지 세서 차이가 가장 적게
import sys

f = sys.stdin.readline


def solution(n, wires):
    parent = [-1 for i in range(n + 1)]  # parent 설정
    parent[0], parent[1] = 0, 0
    num_son = [0 for i in range(n + 1)]  # 하위 node의 수
    od_list = {i: 0 for i in range(n + 1)}  # out-degree가 남아있는 node list
    od_list.pop(0)

    # parent, out-degree 계산
    for v1, v2 in wires:
        if parent[v1] == -1:
            parent[v1] = v2
            od_list[v2] += 1
        else:
            parent[v2] = v1
            od_list[v1] += 1

    # out-degree가 0인 node부터 son 계산
    while od_list:
        node2del = []
        for node, od in od_list.items():
            if od == 0:  # 자식이 없는 node
                if node == 1:
                    node2del.append(node)
                else:
                    node2del.append(node)
                    num_son[parent[node]] += num_son[node] + 1  # parent의 son 갯수 update
                    od_list[parent[node]] -= 1  # parent의 od - 1

        for node in node2del:
            od_list.pop(node)

    # print(parent)
    # print(num_son)

    min_dif = sys.maxsize
    for son in num_son:
        min_dif = min(abs(son + 1 - (n - son - 1)), min_dif)
    # print(min_dif)
    return min_dif


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
solution(4, [[1, 2], [2, 3], [3, 4]])
solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])
