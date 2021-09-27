def permArray(perm, array):
    perm_dict = {}
    for i in range(len(perm_dict)):
        perm_dict[perm[i]] = array[i]

    for index in perm_dict:
        array[index] = perm_dict[index]


print(permArray([2, 0, 1, 3], ['a', 'b', 'c', 'd']))


def permArray(perm_array, array):
    for i in range(len(array)):
        # while the element at perm[i], (first loop the element is 2), is not equal
        # to index 0, (first loop), swap the current element in the array to correspond present index
        # in perm_array
        while perm_array[i] != i:
            array[perm_array[i]], array[i] = array[i], array[perm_array[i]]
            perm_array[perm_array[i]
                       ], perm_array[i] = perm_array[i], perm_array[perm_array[i]]
    return array


print(permArray([2, 0, 1, 3], ['a', 'b', 'c', 'd']))
