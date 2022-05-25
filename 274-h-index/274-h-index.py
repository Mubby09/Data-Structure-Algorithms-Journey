class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i, c in enumerate(citations):
            if c >= n - i:
                return n - i 
                
        return 0
        