def repeatedString(string, number):
    numOfTheLetter = 0

    for i in string:
        if i == 'a':
            numOfTheLetter += 1

    numOfTheLetter = number // len(string) * numOfTheLetter
    remainderOfTheStringAfterDivision = string[:number % len(string)]

    for i in remainderOfTheStringAfterDivision:
        if i == 'a':
            numOfTheLetter += 1

    return print(numOfTheLetter)


repeatedString('abababababababababababababababababa', 15)
