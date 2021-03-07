class Solution(object):
    def isMonotonic(self, A):
        decreasing = True
        increasing = True
        for i in range(len(A) -1):
            if A[i] > A[i + 1]:
                increasing = False
            if A[i] < A[i + 1]:
                decreasing = False
        return increasing | decreasing        
        """
        :type A: List[int]
        :rtype: bool
        """
        