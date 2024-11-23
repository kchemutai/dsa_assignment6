class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def insert(self, index, value):
        """
        Insert an element at a specific index.
        Time Complexity: O(n) in the worst case (due to shifting).
        """
        if self.size == self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        """
        Delete an element at a specific index.
        Time Complexity: O(n) in the worst case (due to shifting).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def access(self, index):
        """
        Access an element at a specific index.
        Time Complexity: O(1).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        """
        Push an element onto the stack.
        Time Complexity: O(1).
        """
        self.data.append(value)

    def pop(self):
        """
        Pop the top element from the stack.
        Time Complexity: O(1).
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()

    def peek(self):
        """
        Peek at the top element of the stack.
        Time Complexity: O(1).
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        """
        Add an element to the rear of the queue.
        Time Complexity: O(1).
        """
        self.data.append(value)

    def dequeue(self):
        """
        Remove an element from the front of the queue.
        Time Complexity: O(n) due to shifting elements.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0
    


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Insert a node at the beginning of the list.
        Time Complexity: O(1).
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """
        Delete a node with the given value.
        Time Complexity: O(n).
        """
        if not self.head:
            raise Exception("List is empty")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            raise ValueError("Value not found in the list")

        current.next = current.next.next

    def traverse(self):
        """
        Traverse the linked list and return elements.
        Time Complexity: O(n).
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

