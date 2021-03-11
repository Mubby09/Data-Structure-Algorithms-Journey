def stringToInteger(string):
    output = 0

    if string[0] == '-':
        start_index = 1
        is_negative = True
    else:
        start_index = 0
        is_negative = False

    for i in range(start_index, len(string)):
        place = 10**(len(string) - (i + 1))
        digit = ord(string[i]) - ord('0')
        output += place * digit

    if is_negative:
        return -1 * output
    else:
        return output


print(stringToInteger("-896"))
print(stringToInteger("896"))
print(stringToInteger("554"))
