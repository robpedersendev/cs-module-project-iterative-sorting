# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    """
    Start with current index = 0

    For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side of current index and find the smallest element

    b. Swap the element at current index with the smallest element found in above loop


    """
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
             if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Set incoming array to a variable for DRY code
    init = range(len(arr) - 1)
    # Tells second loop where to start at, runs for each value in the list
    for i in init:
        # Starts at 0
        #
        for j in init:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
