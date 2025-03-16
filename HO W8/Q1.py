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

def quicksort(array, low, high, k):
    if low <= high:
        pivot = partition(array, low, high)
        if pivot == k:
            return array[pivot]
        elif pivot > k:
            return quicksort(array, low, pivot, k)
        else:
            return quicksort(array, pivot + 1, high, k)
    return None

if __name__ == '__main__':
    arr = [5, 4, 7, 2, 3, 1, 6, 8]
    i = 4
    result = quicksort(arr, 0, len(arr) - 1, i)
    print("The ith smallest element is:", result)