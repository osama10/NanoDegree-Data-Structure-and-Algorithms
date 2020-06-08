class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string[0:len(out_string)-3]


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def unique_elements(llist_1, llist_2):
    unique_set1 = set()
    unique_set2 = set()

    current = llist_1.head
    while current is not None:
        unique_set1.add(current.value)
        current = current.next

    current = llist_2.head

    while current is not None:
        unique_set2.add(current.value)
        current = current.next

    return unique_set1, unique_set2


def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None:
        return llist_2
    if llist_2 .head is None:
        return llist_1

    result = unique_elements(llist_1, llist_2)
    union_res = result[0].union(result[1])

    resultll = LinkedList()

    for val in union_res:
        resultll.append(val)

    return resultll


def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 is None or llist_2 is None:
        return []

    result = unique_elements(llist_1, llist_2)
    intersection_res = result[0].intersection(result[1])

    resultll = LinkedList()

    for val in intersection_res:
        resultll.append(val)

    return resultll


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,7,8,9,11,21,1]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 5

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
print(intersection(linked_list_3,linked_list_4))

