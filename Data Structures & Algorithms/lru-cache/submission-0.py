class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # hashmap
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0) # pointers: dummy nodes
        self.left.next, self.right.prev = self.right, self.left # connect left & right nodes

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # cache[key] is a node, get node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # value in hashmap is a pointer to node
        self.insert(self.cache[key]) # insert whole node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def insert(self, node):
        prev_node = self.right.prev
        right_node = self.right
        prev_node.next = node
        right_node.prev = node
        node.next = right_node
        node.prev = prev_node