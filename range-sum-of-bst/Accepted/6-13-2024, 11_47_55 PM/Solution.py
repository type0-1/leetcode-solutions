// https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = self.traverse(root, low, high, 0)
        return total

    def traverse(self, root, low, high, total):
        
        total = 0
        if root is None:
            return total
        
        if root.val >= low and root.val <= high:
            total += root.val
        
        total += self.traverse(root.left, low, high, total)
        total += self.traverse(root.right, low, high, total)

        return total