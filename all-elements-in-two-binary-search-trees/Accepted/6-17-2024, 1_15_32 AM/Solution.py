// https://leetcode.com/problems/all-elements-in-two-binary-search-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []

        def traverse(root):
            if root is None:
                return
            result.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root1)
        traverse(root2)
        return sorted(result)