# Write a program that takes an array of intergers as an parameter, and reorder the integers such that the even numbers
# come before the odd numbers

def even_odd(array):
    next_even, next_odd = 0, len(array) - 1

    while next_even < next_odd:
        if array[next_even] % 2 == 0:
            next_even += 1
        else:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -= 1
    return array


print(even_odd([7, 9, 2, 4, 90, 8, 71, 54, 3, 9]))
