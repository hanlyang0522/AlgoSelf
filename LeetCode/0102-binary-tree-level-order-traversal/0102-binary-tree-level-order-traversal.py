class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque()
        dq.append(root)
        li = []

        # 1. while loop
        # 2. stack? dq? --> bfs = dq
        while dq:
            lv = []

            for _ in range(len(dq)):    # loop 시작시 dq에 있는건 모두 같은 lv
                node = dq.popleft()

                lv.append(node.val)

                # leaf 아닐 경우에만 push
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            li.append(lv)
            
        return li