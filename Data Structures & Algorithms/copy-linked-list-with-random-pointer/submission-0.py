"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new_map = {}
        dummy = Node(0)

        curr_old = head
        curr_new = dummy
        while curr_old:
            node = Node(curr_old.val)
            old_new_map[curr_old] = node
            curr_new.next = node
    
            curr_old = curr_old.next
            curr_new = node
        
        curr_old = head
        curr_new = dummy.next
        while curr_old:
            curr_new.random = old_new_map.get(curr_old.random, None)
            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return dummy.next

            
        

