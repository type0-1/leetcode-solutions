// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)
        val = root.val
        nums = []
        while not q.empty():
            node = q.get()
            if val < node.val:
                nums.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        if nums == []:
            return -1
        return sorted(nums)[0]
