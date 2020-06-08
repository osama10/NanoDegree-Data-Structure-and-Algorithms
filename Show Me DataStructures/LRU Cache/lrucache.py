class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        key = self.head.key
        self.head = self.head.next
        self.head.prev = None
        return key, value

    def make_tail(self, node):
        if node == self.tail:
            return
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.enqueue(node.key, node.value)
        node = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = Queue()
        self.cache = dict()
        self.total_elements = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.queue.make_tail(node)
        self.cache[key] = self.queue.tail
        return self.queue.tail.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            if node.prev is None:
                self.queue.head = node.next
                self.queue.head.prev = None
            elif node.next is None:
                self.queue.tail = node.prev
                self.queue.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = None
        elif self.total_elements >= self.capacity:
            del_key, del_value = self.queue.dequeue()
            del self.cache[del_key]
        else:
            self.total_elements += 1

        self.queue.enqueue(key, value)
        self.cache[key] = self.queue.tail


our_cache = LRU_Cache(5)

print(our_cache.get('a'))  # print -1

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # print 1
print(our_cache.get(2))  # print 2
print(our_cache.get(3))  # print 3
print(our_cache.get(4))  # print 4
print(our_cache.get(9))  # print -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(1))  # print -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(5))  # print 5
print(our_cache.get(6))  # print 6

our_cache.set('a', 'a')
print(our_cache.get(2))  # print -1
print(our_cache.get('a'))  # print a


our_cache = LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)

print(our_cache.get(4))  # Expected Value = 4
print(our_cache.get(1))  # Expected Value = -1
our_cache.set(2,4)
print(our_cache.get(2))  # Expected Value = 4
our_cache.set(5,5)
print(our_cache.get(3))  # Expected Value = -1
print(our_cache.get(5))  # Expected Value = 5
our_cache.set(2,6)
print(our_cache.get(2))  # Expected Value = 6
our_cache.set(6,6)

our_cache = LRU_Cache(2)

our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)

print(our_cache.get(1))  # Expected Value = -1
print(our_cache.get(2))  # Expected Value = -1
print(our_cache.get(3))  # Expected Value = 3
print(our_cache.get(4))  # Expected Value = 4

our_cache.set(3,1)
print(our_cache.get(3))  # Expected Value = 1
our_cache.set(5,2)
print(our_cache.get(4))  # Expected Value = -1
print(our_cache.get(5))  # Expected Value = 2
our_cache.set(6,6)
print(our_cache.get(3))  # Expected Value = -1
