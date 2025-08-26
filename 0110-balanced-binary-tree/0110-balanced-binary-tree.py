class Solution:
    def isLevel(self, node: TreeNode):
        if node is None:
            return 0

        lvLeft = self.isLevel(node.left)
        lvRight = self.isLevel(node.right)

        if lvLeft == -1 or lvRight == -1:
            return -1
        if abs(lvLeft - lvRight) > 1:
            return -1
        else:
            return max(lvLeft, lvRight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isLevel(root) != -1