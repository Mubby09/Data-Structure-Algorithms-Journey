def next_permutation(array):
    inversion_point = len(array) - 2
    while inversion_point > 0 and array[inversion_point] > array[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point + 1, len(array))):
        if array[i] > array[inversion_point]:
            array[i], array[inversion_point] = array[inversion_point], array[i]
            break

    array[inversion_point + 1:] = reversed(array[inversion_point + 1:])
    return array


print(next_permutation([1, 3, 4, 6, 7, 6, 7]))
