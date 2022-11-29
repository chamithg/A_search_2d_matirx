class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for each in matrix:
            if target > each[0] and target< each[-1]:
                return target in each
        
        return False




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16

obj = Solution()

print(obj.searchMatrix(matrix,target))