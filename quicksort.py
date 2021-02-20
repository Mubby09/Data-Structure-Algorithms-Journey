def quick_sort(pivot, array):
    pivot = array[pivot]
    start = 0
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[start] = array[start], array[i]
        start += 1

    end = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] > pivot:
            array[i], array[end] = array[end], array[i]
        end -= 1
    return array


print(quick_sort(6, [5, 5, 8, 9, 3, 1, 3, 5, 6, 8, 9, 0, 2, 7]))
