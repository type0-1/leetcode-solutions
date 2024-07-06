// https://leetcode.com/problems/merge-in-between-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = node2 = list1
        
        for _ in range(a-1):
            node = node.next
        
        for _ in range(b+1):
            node2 = node2.next
        
        node.next = list2

        temp = list2

        while temp.next:
            temp = temp.next
        temp.next = node2

        return list1