import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, next=self.head)
        if not self.head:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return None
        value = self.head.value
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if not self.head:
            self.head = self.tail = ListNode(value)
        else:
            self.tail = ListNode(value, prev=self.tail)
            self.tail.prev.next = self.tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        if self.head == self.tail:
            self.tail.delete()
            self.head = None
            self.tail = None
        self.length -= 1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.add_to_head(node.value)
        node.delete()
        self.length -= 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            return
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        current_node = self.head.next
        max_node = self.head.value
        while current_node:
            if current_node.value > max_node:
                max_node = current_node.value
            current_node = current_node.next
        return max_node


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        value = self.storage.remove_from_head()
        if value:
            self.size -= 1
        return value

    def len(self):
        return self.size


class Stack:
    def __init__(self):
        self.size = 0
        self.data = DoublyLinkedList()

    def push(self, value):
        self.data.add_to_head(value)
        self.size += 1

    def pop(self):
        value = self.data.remove_from_head()
        if value:
            self.size -= 1
        return value

    def len(self):
        return self.size


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # is there is no self.left value
            if not self.left:
                # set the new left child to be new value
                self.left = BinarySearchTree(value)
            else:
                # recursion
                self.left.insert(value)
        # the new value is greater than the current node
        # go rigth
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True
        # target is smaller, go left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        # recursive solution
        if not self.right:
            return self.value
        return self.right.get_max()


duplicates = []
# Grabbing first value in name
bst = BinarySearchTree(names_1[0])
# Looping through names_1 and inserting each name
for name in names_1:
    bst.insert(name)
# Looping trhough names_2 and seeing if any match what was inserted
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
