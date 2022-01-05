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
    
    ###################################################
    #Essencially, the line of code below referenced to the solution above simply checks for the value 
    # of the key in the 'lookup_list' object and compares if the character in the 's' string that is 
    # also found in the 'lookup_list' object and if they match.
    
    # lookup_list[left_characters.pop()] != character:
        