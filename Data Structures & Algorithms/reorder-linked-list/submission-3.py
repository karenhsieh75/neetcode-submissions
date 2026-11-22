# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # cut to half
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_start = slow.next
        slow.next = None

        # reverse second half
        prev = None
        cur = second_start

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # merge
        cur1 = head
        cur2 = prev

        while cur1 and cur2:
            nxt1 = cur1.next
            cur1.next = cur2
            nxt2 = cur2.next
            cur2.next = nxt1
            cur1, cur2 = nxt1, nxt2