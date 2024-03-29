# 1 : Matrix Median

# Given a matrix of integers A of size N x M in which each row is sorted.

# Find and return the overall median of matrix A.

# NOTE: No extra memory is allowed.

# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.


# Example Input

# Input 1:

# A = [   [1, 3, 5],
#         [2, 6, 9],
#         [3, 6, 9]   ] 

# Example Output

# Output 1: 5 

# Example Explanation

# Explanation 1:

# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
# Median is 5. So, we return 5. 

# Approach 1 

from bisect import bisect_right
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def binSearch(self, matrix, min_el, max_el, cntElBeforeMed):
        start = min_el
        end = max_el
        while start < end:
            mid = start + ((end - start) // 2)
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, mid)
            if cnt > cntElBeforeMed:
                end = mid
            else:
                start = mid + 1
        
        return start
    
    def getMinMax(self, matrix):
        min_el = float('inf')
        max_el = float('-inf')
        for row in matrix:
            if min_el > row[0]:
                min_el = row[0]
            if max_el < row[-1]:
                max_el = row[-1]
        
        return min_el, max_el
    
    def findMedian(self, A):
        matrix = A
        rn = len(matrix)
        cn = len(matrix[0])
        cntElBeforeMed = (rn * cn) // 2
        min_el, max_el = self.getMinMax(matrix)
        return self.binSearch(matrix, min_el, max_el, cntElBeforeMed)
        


# Approach 2

from bisect import bisect_right as upper_bound

class Solution:
	def findMedian(self, A):
        n = len(A)
        m = len(A[0])

        low = float('inf')
        high = float('-inf')

        for i in range(n):
            low = min(low, A[i][0])
            high = max(high, A[i][m-1])
        
        desired = (n * m + 1) // 2
        

        while (low < high):
            mid = (low + high) // 2
            place = [0]
         
            # Find count of elements smaller than or equal to mid
            for i in range(n):
                j = upper_bound(A[i], mid)
                place[0] = place[0] + j
            if place[0] < desired:
                low = mid + 1
            else:
                high = mid

        return low
        
