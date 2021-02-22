def remove_dup(array):
    if not array:
        return 0
    write_index = 1
    for i in range(1, len(array)):
        # if write_index - 1 'which is zero(0)' is not equal to the first index element in the array
        if array[write_index - 1] != array[i]:
            array[write_index] = array[i]
            write_index += 1
    return print(write_index)


remove_dup([1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 9])
