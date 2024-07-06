// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag = [-1001]
        def traverse(root, total=0):
            if root:
                total += root.val
                if root.left is None and root.right is None:
                    if total == targetSum:
                        flag[0] = total
                    return
                else:
                    if root.left:
                        traverse(root.left, total)
                    if root.right:
                        traverse(root.right, total)
        traverse(root, 0)
        return flag[0] > -1001
            