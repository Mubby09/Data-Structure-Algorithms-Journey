class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # integer_num = str(x)
        # reversedNum = reversed(str(x))
        # print(reversedNum)
        # if integer_num == reversedNum:
        #     return True
        # else:
        #     return False
        actual_integer = str(x)
        reversed_integer = str(x)[::-1]
        
        if actual_integer == reversed_integer:
            return True
        return False