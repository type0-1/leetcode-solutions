// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nums = []
        self.count = 0
        def traverse(root):
            if root is None:
                nums.append("null")
                self.count += 1
                return
            
            nums.append(root.val)
            self.count += 1
            traverse(root.left)
            traverse(root.right)
        
        traverse(p)
        m = self.count
        traverse(q)

        if self.count//2 != m:
            return False
            
        return nums[:self.count//2] == nums[self.count//2:]
