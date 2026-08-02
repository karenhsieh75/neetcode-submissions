"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        old_to_new = {}
        root = Node(node.val)
        old_to_new[node] = root
        q = deque()
        q.append(node)

        while q:
            old_node = q.popleft()
            new_node = old_to_new[old_node]

            for neighbor in old_node.neighbors:

                if neighbor not in old_to_new:  # not created yet
                    new_neighbor = Node(neighbor.val)
                    old_to_new[neighbor] = new_neighbor
                    q.append(neighbor)
                else:
                    new_neighbor = old_to_new[neighbor]
                
                new_node.neighbors.append(new_neighbor)
        
        return root


        