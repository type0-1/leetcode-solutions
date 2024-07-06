// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = 0
        right = 0

        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            if node.left:
                left += 1
                q.put(node.left)
            if node.right:
                right += 1
                q.put(node.right)
        
        if root.left and root.right:
            return left+right-1
        elif root.right is None:
            return left
        elif root.left is None:
            return right
