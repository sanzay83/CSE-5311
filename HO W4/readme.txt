<=== PROBLEM 0 ===>

Call Stack Breakdown

fib(5)
    fib(4)
        fib(3)
            fib(2)
                fib(1) returns 1
                fib(0) returns 0
                return 1 + 0 = 1  (Return of fib(2) = fib(1) + fib(0))
            fib(1) returns 1
            returns 1 + 1 = 2 (Return of fib(3) = fib(2) + fib(1))
        fib(2)
            fib(1) returns 1
            fib(0) returns 0
            return 1 + 0 = 1  (Return of fib(2) = fib(1) + fib(0))
        returns 2 + 1 = 3   (Return of fib(4) = fib(3) + fib(2))
    fib(3)
        fib(2)
            fib(1) returns 1
            fib(0) returns 0
            return 1 + 0 = 1  (Return of fib(2) = fib(1) + fib(0))
        fib(1) returns 1
        returns 1 + 1 = 2   (Return of fib(3) = fib(2) + fib(1))
    returns 3 + 2 = 5   (Return of fib(5) = fib(4) + fib(3))

The final fib(5) return is 5


<=== PROBLEM 1 ===>
Implemented Solution on P1 merge.py

Time Complexity
The merge function takes two lists and merge. Each of the element of the two list is compared and added into new list which takes a total time complexity of n + n as both the list has equal number of element.
So it is O(2n) which is O(n) ignoring the constant.

Since the iteration goes up to the k'th list we can get the time complexity of 
O(n) + O(2n) + O(3n) + ...... + O(kn)
or, (O(1 + 2 + 3 + .... + k))
taking sum formula
1 + 2 + 3 + .... + k = k(k+1)/2

Total time complexity will be 
O(n*(k(k+1)/2)) = O(nk^2)

Improvement
The time complexity of this implementation is O(nk^2) which is not very efficient for large value. Alteratively it would be better of using min-heap which can improve the time complexity to O(nk log k) for large value of k.

<=== PROBLEM 2 ===>
Implemented Solution on P2 dup.py

Time Complexity
Initalization:
new = [arr[0]] takes O(1) time.

Loop Iteration:
for loop iterates over arr with total of n elements which is O(n).
inside the loop operations,
new[-1] != i 
new.append(i)
each takes O(1) time to execute.

Complexity:
The loop takes total of O(n) where as each operation takes O(1) time complexity. So dominant time complexity is O(n).
There for the time complexity for the algorithm is O(n).

Improvement
This implementation is already on O(n) which is looping once for each element to compare. So, there are no possible improvement.