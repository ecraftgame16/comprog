class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def find(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)
        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Linked List: [1, 2, 3]

ll.prepend(0)
ll.display()  # Linked List: [0, 1, 2, 3]

ll.delete(2)
ll.display()  # Linked List: [0, 1, 3]

print("Find 3:", ll.find(3))  # Find 3: <__main__.Node object at 0x...>
print("Find 4:", ll.find(4))  # Find 4: None
