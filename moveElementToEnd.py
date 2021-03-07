def moveElementsToEnd(array, elementToMove):
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index:
        while left_index < right_index and array[right_index] == elementToMove:
            right_index -= 1
        if array[left_index] == elementToMove:
            array[left_index], array[right_index] = array[right_index], array[left_index]
        left_index += 1
    return print(array)


moveElementsToEnd([3, 5, 4, 4, 2, 1, 5, 5, 7, 3, 2, 2, 8], 5)
