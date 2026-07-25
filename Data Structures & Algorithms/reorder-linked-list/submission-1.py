# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            pass
        
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
        new_head = l1
        l1 = l1.next
        curr = new_head

        while l1:
            curr.next = l2
            l2 = l2.next
            curr.next.next = l1
            l1 = l1.next
            curr = curr.next.next
        
        if l2:
            curr.next = l2
        