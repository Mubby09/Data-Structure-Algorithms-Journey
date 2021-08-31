def revereseWords(string):
    def reverse_range(string, start, finish):
        while start < finish:
            string[start], string[finish] = string[finish], string[start]
            start += 1
            finish -= 1
    reverse_range(string, 0, len(string) - 1)

    start = 0
    while True:
        finish = start

        while finish < len(string) and string[finish] != "":
            finish += 1
        if finish == len(string):
            break

        reverse_range(string, 0, finish - 1)
        start = finish + 1

    reverse_range(string, start, len(string) - 1)


print(revereseWords(["n", "a", "m", "e", "", "i", "s", "",
                     "M", "u", "b", "a", "r", "a", "k"]))
