// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def traverse(root, n=0):
            if root is None:
                return n
            n += 1
            return traverse(root.left, n)

        level = traverse(root)
        return 2*level