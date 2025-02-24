import random
import time

from matplotlib import pyplot as plt

def partition(array, low, high):
    pivot = array[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]

def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot)
        quicksort(array, pivot + 1, high)

def randomized_partition(array, low, high):
    i = random.randint(low, high)
    array[i], array[low] = array[low], array[i]
    return partition(array, low, high)

def randomized_quicksort(array, low, high):
    if low < high:
        pivot = randomized_partition(array, low, high)
        randomized_quicksort(array, low, pivot)
        randomized_quicksort(array, pivot + 1, high)

def worst_case(n):
    return list(range(0, n))

def average_case(n):
    lists = random.sample(list(range(0, n)), n)
    return lists

def best_case(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    mid = n // 2
    return best_case(mid) + best_case(n - mid)

if __name__ == '__main__':
    array = [3, 8, 2, 5, 1, 4, 7, 6]
    print('Non-randomized quicksort')
    print('Before:', array)
    quicksort(array, 0, len(array) - 1)
    print('After:', array)
    print('\nRandomized quicksort')
    array = [3, 8, 2, 5, 1, 4, 7, 6]
    print('Before:', array)
    randomized_quicksort(array, 0, len(array) - 1)
    print('After:', array)

    bestcase, averagecase, worstcase = [], [], []
    sizes = []
    for size in range(100, 1000, 100):
        sizes.append(size)
        array = worst_case(size)
        start_time = time.time()
        quicksort(array, 0, len(array) - 1)
        end_time = time.time()
        worstcase.append(end_time - start_time)

        array = average_case(size)
        start_time = time.time()
        quicksort(array, 0, len(array) - 1)
        end_time = time.time()
        averagecase.append(end_time - start_time)

        array = best_case(size)
        start_time = time.time()
        quicksort(array, 0, len(array) - 1)
        end_time = time.time()
        bestcase.append(end_time - start_time)

    plt.plot(sizes, worstcase, label='Worst case')
    plt.plot(sizes, averagecase, label='Average case')
    plt.plot(sizes, bestcase, label='Best case')
    plt.xlabel('Input size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()