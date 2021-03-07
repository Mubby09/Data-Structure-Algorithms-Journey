def isArrayMonotonic(array):
    decreasing = True
    increasing = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            increasing = False
        if array[i] < array[i + 1]:
            decreasing = False
    return decreasing | increasing


isArrayMonotonic([1, 2, 3, 5, 7, 9])
isArrayMonotonic([1, 4, 2, 9, 7, 8])
