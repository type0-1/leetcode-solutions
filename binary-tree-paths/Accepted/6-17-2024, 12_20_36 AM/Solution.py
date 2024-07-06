// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def traverse(root, s=""):
            if root:
                s += f'{root.val}'
            if root.left is None and root.right is None:
                result.append(s)
                return 
            else:
                s += f'->'
                if root.left:
                    traverse(root.left, s)
                if root.right:
                    traverse(root.right, s)
        
        traverse(root, "")
        return result