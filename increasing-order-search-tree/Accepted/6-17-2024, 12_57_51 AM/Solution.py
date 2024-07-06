// https://leetcode.com/problems/increasing-order-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node_val = []
        
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            node_val.append(root.val)
            traverse(root.right)

        traverse(root)
        
        new_root = TreeNode(node_val[0])
        curr = new_root
        for i in range(1, len(node_val)):
            node = TreeNode(node_val[i])
            curr.right = node
            curr = curr.right
        return new_root

