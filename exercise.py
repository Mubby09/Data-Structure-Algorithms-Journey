# Write a function that takes a list of characters and reverses the letters in place.

def reverseListOfStrings(listOfChars):
    left_index = 0
    right_index = len(listOfChars) - 1

    while left_index < right_index:
        listOfChars[left_index], listOfChars[right_index] = \
            listOfChars[right_index], listOfChars[left_index]

        left_index += 1
        right_index -= 1
    return listOfChars


list_of_strings = ['A', 'T', 'U', 'R', 'E']
print(reverseListOfStrings(list_of_strings))
