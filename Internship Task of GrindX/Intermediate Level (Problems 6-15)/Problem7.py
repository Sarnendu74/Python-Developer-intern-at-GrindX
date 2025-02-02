def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if any swap is made
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the left element is greater than the right
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swap occurs, the list is already sorted
            break

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted list:", numbers)