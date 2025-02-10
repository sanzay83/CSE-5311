def dup(arr):
    new = [arr[0]]
    for i in arr:
        if new[-1] != i:
            new.append(i)
    return new

print(dup([1, 2, 2, 2, 3, 3, 4, 5]))