// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            total = 0
            if node.left is not None:
                total += node.left.val
                q.put(node.left)
            if node.right is not None:
                total += node.right.val
                q.put(node.right)
            if total == k:
                return True
        return False