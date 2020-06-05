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
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
