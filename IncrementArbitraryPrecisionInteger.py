def plus_one(array):
    array[-1] += 1
    for i in reversed(range(1, len(array))):
        print(i)
        if array[i] != 10:
            break
        array[i] = 0
        array[i - 1] += 1
    else:
        if array[0] == 10:
            array[0] = 1
            array.append(0)
    return array


input_array1 = [1, 2, 9]
input_array2 = [3, 4, 5]
input_array3 = [9, 9, 9]
print(plus_one(input_array1))
print(plus_one(input_array2))
print(plus_one(input_array3))
