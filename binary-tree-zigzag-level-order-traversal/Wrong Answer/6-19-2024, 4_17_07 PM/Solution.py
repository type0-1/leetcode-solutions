// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root

        flag = False
        q = Queue()
        q.put(root)
        res = [[root.val]]

        while not q.empty():
            node = q.get()
            arr = []
            if node.left:
                arr.append(node.left.val)
                q.put(node.left)
            if node.right:
                arr.append(node.right.val)
                q.put(node.right)
            if arr != []:
                if not flag:
                    flag = True
                    res.append(arr[::-1])
                else:
                    flag = False
                    res.append(arr)
        return res
