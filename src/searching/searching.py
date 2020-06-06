def linear_search(arr, target):
    # Your code here
    """
    for(start to end of array)
        if (current_element equals to 5)
                print (current_index);
    """
    # Create a for loop that goes through each index that has a value
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    while low <= high:
        # go to the middle
        middle = low + (high - low)  # 2
        mid = arr[middle]

        # ask if the middle is less than or greater than our target
        # if less, eliminate the right-hand side
        if target == mid:
            return middle
        elif target > mid:
            low = middle + 1
        else:
            high = middle - 1
        # adjust the low or high accordingly
    return -1  # not found
