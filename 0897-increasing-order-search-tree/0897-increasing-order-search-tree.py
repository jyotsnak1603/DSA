# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dumm = TreeNode(0)
        self.curr = dumm

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            node.left = None
            self.curr.right = node
            self.curr = node

            inorder(node.right)

        inorder(root)
        return dumm.right