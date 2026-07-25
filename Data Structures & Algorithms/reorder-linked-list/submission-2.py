# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find l1, l2
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse l2
        prev = None
        while l2:
            next_ = l2.next
            l2.next = prev
            prev = l2
            l2 = next_
        l2 = prev
        
        # combine l1, l2
        while l2:
            next1 = l1.next
            next2 = l2.next

            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2
        