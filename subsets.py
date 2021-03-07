def subsets(array):
    resultOutput = [[]]
    for i in array:
        resultOutput += [lst + [i] for lst in resultOutput]
    return print(resultOutput)


subsets([1, 6, 2, 8])
