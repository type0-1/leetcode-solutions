// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        nums = []
        self.count = 0

        def traverse(root):
            if root is None:
                return 0
            
            if root:
                if root.left is None and root.right is None:
                    self.count += 1
                    nums.append(root.val)
        
            traverse(root.left)
            traverse(root.right)

        traverse(root1)
        num = self.count
        traverse(root2)

        if self.count//2 != num:
            return False

        return nums[:self.count//2] == nums[self.count//2:]