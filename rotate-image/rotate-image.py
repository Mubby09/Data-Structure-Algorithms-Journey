class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top = l
                bottom = r
                #top left corner of the matrix
                topLeft = matrix[top][l + i]
                
                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left to top right
                matrix[top + i][r] = topLeft
            
            l += 1
            r -= 1
                