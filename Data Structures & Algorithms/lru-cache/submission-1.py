class Node:
    def __init__(self, key: int, val: int, prev: Node, next: Node):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    def __repr__(self):
        return f"{self.key}: {self.val}" 

class LRUCache:
    # To get constant time gets and puts we can utilize
    # a hashmap (python dict). But to keep both constant with
    # the LRU eviction we will need to use a doubly linked list to 
    # store the recency order. The value stored in the hashmap will
    # be a pointer to a node of the DLL. On every get and put we
    # we will move the touched node to the head of the DLL (most recent)
    # and on put if capacity is full we will remove the tail of the DLL (least recent)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = Node(0,0, None, None)
        self.tail = Node(0,0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, key: int):
        if key in self.mapping:
            self.capacity += 1
            node = self.mapping[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.mapping[key]
    
    def insertToHead(self, key: int, value: int):
        self.capacity -= 1
        node = Node(key, value, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self.mapping[key] = node
    
    # Time: O(1)
    # Space: O(n)
    def get(self, key: int) -> int:
        if key in self.mapping:
            val = self.mapping[key].val
            self.remove(key)
            self.insertToHead(key, val)
            return val
        return -1

    # Time: O(1)
    # Space: O(n)
    def put(self, key: int, value: int) -> None:
        if key not in self.mapping:
            # Remove LRU key
            if self.capacity == 0:
                self.remove(self.tail.prev.key)
            self.insertToHead(key, value)
        # Existing will not trigger LRU removal but it will
        # touch the node, so put it as MRU (head)
        else:
            self.remove(key)
            self.insertToHead(key, value)