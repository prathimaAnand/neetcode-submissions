# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # 1. Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # middle

        # 2. Reverse second half list
        slow.next = None
        tmp2 = None
        while second:
            tmp1 = second.next
            second.next = tmp2 # end of 2nd half
            tmp2 = second
            second = tmp1

        # 3. Reorder
        first = head 
        second = tmp2
        while second:
            tmp3 = first.next
            tmp4 = second.next
            first.next = second
            second.next = tmp3
            
            first = tmp3
            second = tmp4

