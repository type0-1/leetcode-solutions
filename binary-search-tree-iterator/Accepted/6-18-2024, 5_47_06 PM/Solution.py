// https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nums = []
        self.traverse(self.root)

    def next(self) -> int:
        return self.nums.pop(0).val
        

    def hasNext(self) -> bool:
        return len(self.nums) >= 1
        
    def traverse(self, root):
        if root is None:
            return
        
        self.traverse(root.left)
        self.nums.append(root)
        self.traverse(root.right)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()