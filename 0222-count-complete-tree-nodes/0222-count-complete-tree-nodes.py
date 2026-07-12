# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l, r = root, root
        left_height, right_height =0,0
        while l:
            l = l.left
            left_height += 1

        while r:
            r = r.right
            right_height += 1
        if left_height == right_height:
            return (1<<left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)