class FullQueueError(Exception):
    pass

class EmptyQueueError(Exception):
    pass

class _Node:
    __slots__ = ('_value', '_next')
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

class ArrayQueue:
    def __init__(self, capacity=5):
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, value):
        if self.is_full():
            raise FullQueueError("Enqueue failed: queue is full")
        pos = (self._front + self._size) % self._capacity
        self._data[pos] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Dequeue failed: queue is empty")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return val

    def peek_front(self):
        if self.is_empty():
            raise EmptyQueueError("Nothing to peek: queue is empty")
        return self._data[self._front]

    def __str__(self):
        items = []
        for i in range(self._size):
            idx = (self._front + i) % self._capacity
            items.append(str(self._data[idx]))
        return "[" + ", ".join(items) + "]"

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._head is None

    def enqueue(self, value):
        new_node = _Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Dequeue failed: queue is empty")
        val = self._head._value
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return val

    def peek_front(self):
        if self.is_empty():
            raise EmptyQueueError("Nothing to peek: queue is empty")
        return self._head._value

    def __str__(self):
        items = []
        curr = self._head
        while curr:
            items.append(str(curr._value))
            curr = curr._next
        return " -> ".join(items)