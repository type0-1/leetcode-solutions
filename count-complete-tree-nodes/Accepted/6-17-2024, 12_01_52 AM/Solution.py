// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = Queue()
        q.put(root)
        total = 1

        while not q.empty():
            root = q.get()
            if root.left:
                q.put(root.left)
                total += 1
            if root.right:
                q.put(root.right)
                total += 1
        
        return total
