// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original.val == cloned.val and original.val == target.val:
            return cloned
        
        q = Queue()
        q.put(cloned)

        while not q.empty():
            root = q.get()
            if root.val == target.val:
                return root
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)
        
        return None 