class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        dq = deque()
        dq.append([root, -(2**32), 2**32])

        while dq:
            curr, min_l, max_l = dq.popleft()

            if curr.val <= min_l:
                return False
            
            if curr.val >= max_l:
                return False

            if curr.left is not None:
                if curr.left.val > curr.val:
                    return False
                dq.append([curr.left, min_l, min(max_l, curr.val)])

            if curr.right is not None:
                if curr.right.val < curr.val:
                    return False
                dq.append([curr.right, max(min_l, curr.val), max_l])

        return True