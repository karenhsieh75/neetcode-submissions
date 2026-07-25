# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:

            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
                
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            val = l1_val + l2_val + carry
            
            if val > 9:
                carry = 1
                val = val % 10
            else:
                carry = 0
            
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
        

            
            