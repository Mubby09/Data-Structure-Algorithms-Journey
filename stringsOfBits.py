# Write a program which take as input two strings s and t of bits encoding binary
# numbers Bs and Bt, respectively and returns a new string of bits representing the number Bs + Bt

def bit_addition(s, t):
    numberValue_s = int(s, 2)
    numberValue_t = int(t, 2)

    return (bin(numberValue_s + numberValue_t))


print(bit_addition('0101', '010100'))
print(bit_addition('010101010', '011011'))
print(bit_addition('01010010', '0110000101'))
