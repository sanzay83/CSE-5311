import random
import time
import matplotlib.pyplot as plt
def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    sizes = [200, 2000, 20000]
    insertion_sort_time = []
    bubble_sort_time = []
    selection_sort_time = []
    for size in sizes:
        test_list = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        insertion_sort(test_list.copy())
        elapsed_time = time.time() - start_time
        insertion_sort_time.append(elapsed_time)
        start_time = time.time()
        bubble_sort(test_list.copy())
        elapsed_time = time.time() - start_time
        bubble_sort_time.append(elapsed_time)
        start_time = time.time()
        selection_sort(test_list.copy())
        elapsed_time = time.time() - start_time
        selection_sort_time.append(elapsed_time)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertion_sort_time, marker='o', linestyle='-', color='b', label='Insertion Sort Time')
    plt.plot(sizes, bubble_sort_time, marker='o', linestyle='-', color='r', label='Bubble Sort Time')
    plt.plot(sizes, selection_sort_time, marker='o', linestyle='-', color='g', label='Selection Sort Time')
    plt.title('Insertion Sort vs Bubble Sort vs Selection Sort Time Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.grid(True)
    plt.legend()
    plt.show()
