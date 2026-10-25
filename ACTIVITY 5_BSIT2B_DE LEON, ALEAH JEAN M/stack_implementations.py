class OverflowError(Exception):
    pass

class UnderflowError(Exception):
    pass

class _Node:
    __slots__ = ('_value', '_next')
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._data = [None] * capacity
        self._top = -1

    def __len__(self):
        return self._top + 1

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Cannot push: stack is full")
        self._top += 1
        self._data[self._top] = value

    def pop(self):
        if self.is_empty():
            raise UnderflowError("Cannot pop: stack is empty")
        val = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise UnderflowError("Cannot peek: stack is empty")
        return self._data[self._top]

    def __str__(self):
        return str(self._data[:self._top + 1])

class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._head is None

    def push(self, value):
        new_node = _Node(value, self._head)
        self._head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise UnderflowError("Cannot pop: stack is empty")
        val = self._head._value
        self._head = self._head._next
        self._size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise UnderflowError("Cannot peek: stack is empty")
        return self._head._value

    def __str__(self):
        items = []
        curr = self._head
        while curr:
            items.append(str(curr._value))
            curr = curr._next
        return " -> ".join(items)