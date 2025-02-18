class MinHeap():
  def __init__(self):
    self.heap = []

  def parent(self, i):
    return (i -1) >> 1
  
  def left(self, i):
    return (i << 1) + 1
  
  def right(self, i):
    return (i << 1) + 2
  
  def build_min_heap(self, A):
    self.heap = A
    for i in range(len(A) // 2, -1, -1):
      self.min_heapify(i)
  
  def min_heapify(self, i):
    l = self.left(i)
    r = self.right(i)
    if l < len(self.heap) and self.heap[l] < self.heap[i]:
      smallest = l
    else:
      smallest = i
    if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
      smallest = r
    if smallest != i:
      self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
      self.min_heapify(smallest)

  def pop(self):
    if len(self.heap) < 1:
      return None
    min = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    self.min_heapify(0)
    return min
  
  def push(self, value):
    self.heap.append(value)
    i = len(self.heap) - 1
    while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
      self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
      i = self.parent(i)

  def __repr__(self):
    return str(self.heap)
  
if __name__ == '__main__':
  A = [12, 14, 8, 5, 3, 9, 7, 1, 6]
  min_heap1 = MinHeap()
  min_heap1.build_min_heap(A)
  print("Initial: ", min_heap1)
  min_heap1.push(0)
  print("Push 0: ", min_heap1)
  print("Pop: ", min_heap1.pop())
  print("After Pop: ", min_heap1)
  

  print("\n")
  B = [3.4, 6.2, 8.1, 9.3, 2.1, 5.7, 7.8, 1.2, 4.5]
  min_heap2 = MinHeap()
  min_heap2.build_min_heap(B)
  print("Initial: ", min_heap2)
  print("Pop: ", min_heap2.pop())
  print("After Pop: ", min_heap2)
  min_heap2.push(0.5)
  print("Push 0.5: ", min_heap2)