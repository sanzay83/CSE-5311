class Stack:
    def __init__(self, max_size=10):
        self.items = []
        self.top = 0
        self.max_size = max_size
    
    def is_empty(self):
        return self.top == 0
    
    def push(self, item):
        if self.top == self.max_size:
            raise OverflowError("Stack overflow")
        self.items.append(item)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        else:
            self.top -= 1
            return self.items[self.top]
        
class Queue:
    def __init__(self, max_size=10):
        self.items = []
        self.head = 0
        self.tail = 0
        self.max_size = max_size
    
    def is_empty(self):
        return self.head == self.tail
    
    def enqueue(self, item):
        if self.tail == self.max_size:
            raise OverflowError("Queue overflow")
        self.items.append(item)
        if self.tail == self.max_size -1:
            self.tail = 0
        else:
            self.tail += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        item = self.items[self.head]
        if self.head == self.max_size - 1:
            self.head = 0
        else:
            self.head += 1
        return item
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def list_search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def list_insert(self, x):
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def list_delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    
    linked_list = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list.list_insert(node1)
    linked_list.list_insert(node2)
    linked_list.list_insert(node3)
    linked_list.list_delete(node2)
    print(linked_list.list_search(1).data)