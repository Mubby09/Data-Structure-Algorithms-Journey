def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(bubbleSort([8, 2, 1, 7, 3, 0, 4]))
