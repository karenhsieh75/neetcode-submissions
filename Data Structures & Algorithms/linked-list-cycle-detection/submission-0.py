# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode()
        curr = head

        while curr:
            if curr.next == dummy:
                return True
            next_ = curr.next
            curr.next = dummy
            curr = next_
        
        return False

        