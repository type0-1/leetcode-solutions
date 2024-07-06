// https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        
        num = root.val

        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            if node.val != num:
                return False
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        
        return True
        