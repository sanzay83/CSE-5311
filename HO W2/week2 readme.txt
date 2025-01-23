Selection Sort Argue

Selection Sort is a simple sorting algorithm that works by continuous selection of small or large element and adding it at the beginning of the sorted elements.

Initialization
Initially, on single instance the element could be sorted or has single element or none, no sorting is needed.

Maintenance
Assuming in ascending, moving forward in each iteration, the minimum element is selected and then swapped with the position of unsorted. Now the iteration keeps moving the small element starts filling in the correct position expanding the sorted side and shrinking the unsorted side untill all the unsorted elements are gone and all the elements are sorted.

Termination
Now the algorithm ends or terminates as all the elements are sorted as there are no more unsorted elements. All the elements should be in their correct position from small to large element in case of ascending or large to small element in case of descending.

Hence, with this we show the correctness of selection sort. eventhough its correct and simple algorithm it has the time commplexity of O(n^2) which is not great as time to run the algorithm grows with the square of input size. If the size is very less it wont matter much but if there are thousands to million or more then process time cant be handled.