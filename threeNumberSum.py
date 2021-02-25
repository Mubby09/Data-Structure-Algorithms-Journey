def threeNumberSum(array, target):
    # sorting the array in an ascending order
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left_pointer = i + 1
        right_pointer = len(array) - 1
        while left_pointer < right_pointer:
            currentSum = array[i] + array[left_pointer] + array[right_pointer]
            if currentSum == target:
                triplets.append([
                    array[i], array[left_pointer], array[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
            if currentSum < target:
                left_pointer += 1
            if currentSum > target:
                right_pointer -= 1
    return print(triplets)


threeNumberSum([-8, 6, 1, 2, 3, 5, 6, 12], 0)

# Time complexity = O(N ^ 2)
# Space complexity = O(N)
