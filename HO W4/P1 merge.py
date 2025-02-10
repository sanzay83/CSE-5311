def merge(a, b):
    i, j, c = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    c.extend(a[i:])
    c.extend(b[j:])
    return c

list = [[1,3,5,7],[2,4,6,8],[0,9,10,11]]
result = list[0]
for i in range(1, len(list)):
    result = merge(result, list[i])
print(result)