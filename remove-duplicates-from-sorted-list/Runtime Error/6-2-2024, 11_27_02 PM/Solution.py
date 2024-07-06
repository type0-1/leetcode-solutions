// https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        curr = head
        seen = [curr.val]

        while curr.next:
            if curr.next.value not in seen:
                seen.append(curr.next.val)
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head