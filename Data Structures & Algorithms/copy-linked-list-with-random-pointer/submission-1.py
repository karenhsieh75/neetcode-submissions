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

        curr = head
        while curr:
            copy_node = Node(curr.val)
            old_new_map[curr] = copy_node
            curr = curr.next 
        
        curr = head
        while curr:
            copy_node = old_new_map[curr]
            copy_node.next = old_new_map.get(curr.next, None)
            copy_node.random = old_new_map.get(curr.random, None)
            curr = curr.next
        
        return old_new_map.get(head, None)

            
        

