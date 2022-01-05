class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #left charcters such as '(' , '{' , '['
        left_characters = []
        lookup_list = {'(' : ')', '{' : '}', '[' : ']'}
        
        for character in s:
            if character in lookup_list:
                left_characters.append(character)
            elif left_characters == [] or lookup_list[left_characters.pop()] != character:
                return False
        return left_characters == []
        