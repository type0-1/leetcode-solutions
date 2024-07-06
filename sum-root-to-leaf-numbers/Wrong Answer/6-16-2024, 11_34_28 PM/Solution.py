// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, s=""):
            total = 0
            if root is None:
                total += int(s)
                return total
            s += str(root.val)
            total += traverse(root.left, s)
            total += traverse(root.right, s)
            return total
        return traverse(root, "") // 2