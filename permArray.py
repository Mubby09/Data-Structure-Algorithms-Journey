def permArray(perm, array):
    perm_dict = {}
    for i in range(len(perm_dict)):
        perm_dict[perm[i]] = array[i]

    for index in perm_dict:
        array[index] = perm_dict[index]


print(permArray([2, 0, 1, 3], ['a', 'b', 'c', 'd']))
