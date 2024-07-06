// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def traverse(root):
            if root is None:
                return

            if root:
                if root.left:
                    if root.left.left is None:
                        self.total += root.left.val
            
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.total

        