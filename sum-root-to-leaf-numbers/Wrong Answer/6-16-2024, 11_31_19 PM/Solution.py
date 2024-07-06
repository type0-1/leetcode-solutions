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
            if root is None:
                nums.append(int(s))
                return 
            s += str(root.val)
            traverse(root.left, s)
            traverse(root.right, s)

        nums = []
        traverse(root, "")
        return sum(set(nums))