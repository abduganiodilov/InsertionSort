def insertion_sort(arr):
    n = len(arr)
    # Calculate the length of the array to determine how many elements need to be sorted.

    for i in range(1, n):
        # Start iterating from the second element (index 1) because the first element is considered sorted.

        key = i
        # Set 'key' as the current index whose element will be compared with the sorted portion.

        while key > 0 and arr[key - 1] > arr[key]:
            # Continue swapping while:
            #   1. We haven't reached the beginning of the array (key > 0)
            #   2. The element on the left (arr[key-1]) is greater than the element at the current position (arr[key]).

            arr[key], arr[key - 1] = arr[key - 1], arr[key]
            # Swap the element at 'key' with the element immediately to its left.

            key -= 1
            # Move the 'key' one position to the left to continue comparing and swapping if necessary.

    return arr
    # After processing all elements, return the sorted array.


print(insertion_sort([6, 2, 6, 3, 8, 9, 1, 5]))
# Call the insertion_sort function with the provided list and print the resulting sorted list.
