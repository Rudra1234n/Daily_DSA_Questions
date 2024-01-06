class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = Node()  # Dummy head node
        self.tail = Node()  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)  # Move the accessed node to the front
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)  # Move the updated node to the front
        else:
            if len(self.cache) == self.capacity:
                self._evict_last()  # Remove the least recently used node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)  # Add the new node to the front

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _evict_last(self):
        last_node = self.tail.prev
        self._remove_node(last_node)
        del self.cache[last_node.key]
