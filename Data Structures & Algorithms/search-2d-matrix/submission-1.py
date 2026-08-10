class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        if not (top<=bottom):
            return False
        
        left = 0
        right = COLUMNS - 1
        row = (top + bottom) // 2
        while left <= right:
            mid = (left + right) // 2
            
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False 

        

        
        