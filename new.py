
def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element
        print(int_list)


original_list = [2, 3, 4, 5]
print(square_list_in_place(original_list))
# print("list is : %s" % original_list)
