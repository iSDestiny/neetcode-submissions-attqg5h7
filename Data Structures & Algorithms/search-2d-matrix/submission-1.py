class Solution:
    # Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
    # binary search to identify which row the target is in (i.e. row at index 1)
    # then binary search the row itself to check if target is inside, if not found return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl, rowr = 0, len(matrix) - 1

        while rowl <= rowr:
            rowm = (rowl + rowr) // 2

            if matrix[rowm][0] <= target <= matrix[rowm][-1]:
                return self.searchArray(matrix[rowm], target)
            elif matrix[rowm][0] > target:
                rowr = rowm - 1
            else:
                rowl = rowm + 1
        
        return False
    
    def searchArray(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1

        while l <= r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False