class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
    
    def find(self, key: int):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = {}

    def hash(self, key: int) -> int:
        A = 0.6180339887
        return int(self.capacity * (key * A % 1))
    
    def insert(self, key: int, value: int):
        index = self.hash(key)
        if index not in self.table:
            self.table[index] = DoubleLinkedList()
        node = self.table[index].find(key)
        if node:
            node.value = value
        else:
            self.table[index].append(key, value)
            self.size += 1
    
    def delete(self, key: int):
        index = self.hash(key)
        if index in self.table:
            node = self.table[index].find(key)
            if node:
                self.table[index].remove(node)
                self.size -= 1
    
    def search(self, key: int) -> int:
        index = self.hash(key)
        if index in self.table:
            node = self.table[index].find(key)
            if node:
                return node.value
        return -1
    
    def display(self):
        for index in self.table:
            current = self.table[index].head
            while current:
                print(f'Key: {current.key}, Value: {current.value}')
                current = current.next
    
if __name__=='__main__':
    hash_table = HashTable(10)
    hash_table.insert(1, 10)
    hash_table.insert(2, 20)
    hash_table.insert(3, 30)
    hash_table.insert(4, 40)
    hash_table.insert(5, 50)
    hash_table.insert(6, 60)
    hash_table.insert(7, 70)
    print(hash_table.search(2))
    hash_table.delete(2)
    print(hash_table.search(2))
    hash_table.display()