// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        def traverse(root, s):
            if root is None:
                return 
            s += f'{root.val}'
            if root.left is None and root.right is None:
                nums.append(s)
            traverse(root.left,s)
            traverse(root.right, s)
        
        traverse(root, "")
        return sum([int(x) for x in nums])
        