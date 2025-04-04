class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity
    
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1
    
    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.size - 1]
        self.size -= 1
        return value
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return str([self.array[i] for i in range(self.size)])
    
if __name__ == "__main__":
    dynamicArray = DynamicArray()
    dynamicArray.append(1)
    dynamicArray.append(2)
    dynamicArray.append(3)
    dynamicArray.append(4)
    dynamicArray.append(5)
    print(dynamicArray)
    dynamicArray.set(1, 5)
    print(dynamicArray)
    print(dynamicArray.get(1))
    dynamicArray.pop()
    dynamicArray.pop()
    print(dynamicArray)
