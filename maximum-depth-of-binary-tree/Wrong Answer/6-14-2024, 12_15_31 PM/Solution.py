// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        LD = 1
        RD = 1
        
        q = Queue()
        q.put(root)

        while not q.empty():
            root = q.get()
            if root.left is not None:
                q.put(root.left)
                LD += 1
            if root.right is not None:
                q.put(root.right)
                RD += 1
        
        return max(LD, RD)