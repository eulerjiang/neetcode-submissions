# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0 -> 1 -> 2
        1 -> 3 -> 5 

        0, 1, 2, 3

        2 -> 4
        4 -> 8
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        # reverse half2

        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            second.next = first.next
            first.next = second
            first = tmp1
            second = tmp2


        
