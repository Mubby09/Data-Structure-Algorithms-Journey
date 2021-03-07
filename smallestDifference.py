def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    indexOfArrayOne = 0
    indexofArrayTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while indexOfArrayOne < len(arrayOne) and indexofArrayTwo < len(arrayTwo):
        firstNum = arrayOne[indexOfArrayOne]
        secondNum = arrayTwo[indexofArrayTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            indexOfArrayOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indexofArrayTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


smallestDifference([1, 3, 4, 34, 6, 78, 73], [79, 83, 91, 0, 7])
