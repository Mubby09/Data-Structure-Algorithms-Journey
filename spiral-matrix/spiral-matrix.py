class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        startRow, endRow = 0, len(matrix) - 1
        startColumn, endColumn = 0, len(matrix[0]) - 1
        
        while startRow <= endRow and startColumn <= endColumn:
            for column in range(startRow, endColumn + 1):
                result.append(matrix[startRow][column])
            
            for row in range(startRow + 1, endRow + 1):
                result.append(matrix[row][endColumn])
                
            for column in reversed(range(startColumn, endColumn)):
                if startRow == endRow:
                    break  
                   
                result.append(matrix[endRow][column])
                
            for row in reversed(range(startRow + 1, endRow)):
                if startColumn == endColumn:
                    break
                    
                result.append(matrix[row][startColumn])  
                
            startRow += 1
            endRow -= 1
            startColumn += 1
            endColumn -= 1
        
        return result
        
        
        
                
        