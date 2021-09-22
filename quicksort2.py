# Pivot is not given as a parameter
# THIS SOLUTION USES RECURSION

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lesserThanPivot = [i for i in array[1:] if i <= pivot]
        greaterThanPivot = [i for i in array[1:] if i > pivot]

        return quickSort(lesserThanPivot) + [pivot] + quickSort(greaterThanPivot)


print(quickSort([2, 6, 7, 1, 1, 0, 8, 6, 3, 2, 8, 5, 4]))
