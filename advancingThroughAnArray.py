# def advanceThroughAnArray(array):
#     reached_so_far = 0
#     last_index = len(array) - 1
#     i = 0

#     while i <= reached_so_far and reached_so_far < last_index:
#         reached_so_far = max(reached_so_far, array[i] + 1)
#         i += 1
#     if reached_so_far >= last_index:
#         print('True')
#     else:
#         print('False')

def advanceThroughAnArray(array):
    reached_so_far, last_index = 0, len(array) - 1

    iterator = 0
    while iterator <= reached_so_far and reached_so_far < last_index:
        reached_so_far = max(reached_so_far, array[iterator] + 1)
        iterator += 1

    if reached_so_far >= last_index:
        return True
    return False
