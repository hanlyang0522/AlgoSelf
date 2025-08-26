# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque()
        dq.append([root, 0])
        li = [[]]

        # 1. while loop
        # 2. stack? dq? --> bfs = dq
        while dq:
            # 순서는 간단한데... lv는 어떻게 처리?? --> push할때 level을 입력!!
            node, lv = dq.popleft()

            if node is None:
                continue

            if len(li) <= lv:
                li.append([])

            li[lv].append(node.val)

            dq.append([node.left, lv + 1])
            dq.append([node.right, lv + 1])

        return li