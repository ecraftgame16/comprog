class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

queue = Queue()

print("Queue created. Is it empty?", queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueueing 1, 2, 3:", queue)
print("Front of the queue:", queue.peek())
print("Dequeued item:", queue.dequeue())
print("Queue after dequeuing an item:", queue)
print("Is queue empty?", queue.is_empty())
print("Size of the queue:", queue.size())
