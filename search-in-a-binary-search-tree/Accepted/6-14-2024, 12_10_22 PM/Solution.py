// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        
        q = Queue()
        q.put(root)

        while not q.empty():
            root = q.get()
            if root.val == val:
                return root
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)
        
        return None
