import string


def isStringAPalindrome(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")

    if s == s[::-1]:
        return print(f"{s} is a palindrome")

    return print('False')


isStringAPalindrome('racecar')


# ////////////////////////////////////////////////////////////////////////////////

def isStringAPalindrome(s):
    print(all(s[i] == s[~i] for i in range(len(s) // 2)))


isStringAPalindrome('madam')
