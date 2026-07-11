# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        prev -> 2 -> 3 -> 4
        """
        prev = None
        while head:
            temp = prev
            prev = head
            head = head.next
            prev.next = temp

        return prev
        

            