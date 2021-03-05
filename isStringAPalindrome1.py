import string


def isStringAPalindrome(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")

    if s == s[::-1]:
        return print(f"{s} is a palindrome")

    return print('False')


isStringAPalindrome('race: car')
