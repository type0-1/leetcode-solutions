// https://leetcode.com/problems/add-two-numbers-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1 and l2:
            num1 += f'{l1.val}'
            num2 += f'{l2.val}'

            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                num1 += f'{l1.val}'
                l1 = l1.next
        else:
            while l2:
                num2 += f'{l2.val}'
                l2 = l2.next
        
        dummy = ListNode()
        curr = dummy
        total = f'{int(num1) + int(num2)}'
        
        for n in total:
            curr.next = ListNode(int(n))
            curr = curr.next
        return dummy.next