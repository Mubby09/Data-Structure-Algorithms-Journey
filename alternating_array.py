def alternate_array(array):
    for i in range(len(array)):
        array[i:i+2] = sorted(array[i:i+2], reverse=bool(i % 2))

    return array


print(alternate_array([2, 7, 9, 4, 1, 8, 5]))
