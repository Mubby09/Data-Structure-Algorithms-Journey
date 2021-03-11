def integerToString(integer):
    is_negative = False

    if integer < 0:
        integer = -integer
        is_negative = True

    to_reverse = []
    while True:
        to_reverse.append(chr(ord('0') + integer % 10))
        integer //= 10
        if integer == 0:
            break

    return print(('-' if is_negative else '') + ''.join(reversed(to_reverse)))


integerToString(-8685)
