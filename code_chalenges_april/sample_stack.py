class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

stack = Stack()

print("Stack created. Is it empty?", stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushing 1, 2, 3:", stack)
print("Top of the stack:", stack.peek())
print("Popped item:", stack.pop())
print("Stack after popping an item:", stack)
print("Is stack empty?", stack.is_empty())
print("Size of the stack:", stack.size())
