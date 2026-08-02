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
        visited = set()

        while q:
            old_node = q.popleft()
            new_node = old_to_new[old_node]
            visited.add(old_node)

            for neighbor in old_node.neighbors:
                if neighbor not in visited:

                    if neighbor not in old_to_new:  # not created yet
                        new_neighbor = Node(neighbor.val)
                        old_to_new[neighbor] = new_neighbor
                    else:
                        new_neighbor = old_to_new[neighbor]
                    
                    new_node.neighbors.append(new_neighbor)
                    new_neighbor.neighbors.append(new_node)
                    
                    q.append(neighbor)
        
        return root


        