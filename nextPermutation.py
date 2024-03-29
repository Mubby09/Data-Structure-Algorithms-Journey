def next_permutation(array):

    # to get the order of the strictly decreasing section of the array
    # i.e, to get the entry before the strictly decreasing suffix of the array
    inversion_point = len(array) - 2
    # print(inversion_point)
    while inversion_point >= 0 and array[inversion_point] > array[inversion_point + 1]:
        inversion_point -= 1
    # to check if the entire array is a strictly decreasing array, return an empty array
        if inversion_point == -1:
            return []
# swapping the invertion point element with the element greater
# than the invertion point element in the strictly decreasing
# suffix of the array, which starts to the end of the array and breaks when it swaps both element
# instead of going on to swap the invertion point element with another element greater than itself in the strictly
# decreasing suffix of the array
        for i in reversed(range(inversion_point + 1, len(array))):
            if array[i] > array[inversion_point]:
                array[i], array[inversion_point] = array[inversion_point], array[i]
                break
# reordering the strictly decreasing section in an ascending order towards the end of the array
            array[inversion_point + 1:] = reversed(array[inversion_point + 1:])
    return array


next_permutation([6, 2, 1, 5, 4, 3, 0])
