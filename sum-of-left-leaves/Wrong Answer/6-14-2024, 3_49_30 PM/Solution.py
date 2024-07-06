// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        total = 0
        if root.left is not None:
            total += root.left.val
            total += self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            total += self.sumOfLeftLeaves(root.right)
        return total