// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        q = Queue()
        q.put(root)
        nums = [[root.val]]

        while not q.empty():
            node = q.get()
            pairs = []
            if node.left:
                pairs.append(node.left.val)
                q.put(node.left)
            if node.right:
                pairs.append(node.right.val)
                q.put(node.right)
            if pairs != []:
                nums.append(pairs)

        return nums