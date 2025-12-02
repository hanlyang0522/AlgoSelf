"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        dq = deque([node])
        di = {node.val: Node(node.val, [])}

        while dq:
            cur = dq.popleft()
            cur_clone = di[cur.val]

            for neigh in cur.neighbors:
                if neigh.val not in di:
                    di[neigh.val] = Node(neigh.val, [])
                    dq.append(neigh)
                
                cur_clone.neighbors.append(di[neigh.val])

        return di[node.val]
