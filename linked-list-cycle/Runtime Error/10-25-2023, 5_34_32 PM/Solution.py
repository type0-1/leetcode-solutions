// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head.next is None:
            return False
        else:
            curr = head
            nodes = []
            while curr.next != None:
                if curr.val in nodes:
                    return True
                nodes.append(curr.val)
                curr = curr.next

        