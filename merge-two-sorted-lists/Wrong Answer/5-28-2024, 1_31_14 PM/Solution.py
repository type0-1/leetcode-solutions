// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        while curr1 and curr1.next and curr2 and curr2.next:
            if curr1.val <= curr2.val:
                temp = curr1.next
                curr1.next = curr2.next
                curr2.next = temp
            else:
                temp = curr2.next
                curr2.next = curr1.next
                curr1.next = temp
            curr1 = curr1.next
            curr2 = curr2.next
        return list1
                
                    
        