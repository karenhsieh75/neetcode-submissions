class Node:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: Node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        # insert to right most
        prev, next_ = self.right.prev, self.right
        prev.next = next_.prev = node
        node.prev = prev
        node.next = next_
    
    def remove(self, node: Node):
        prev, next_ = node.prev, node.next
        prev.next = next_
        next_.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update to right most
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
            
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
