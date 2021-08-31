def spreadSheetEncoding(column_string):
    num = 0
    count = len(column_string) - 1
    print(count)
    for i in column_string:
        num += 26 ** count * (ord(i) - ord('A') + 1)
        count -= 1
    return print(num)


spreadSheetEncoding('ZZ')
