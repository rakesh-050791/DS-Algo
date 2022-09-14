# 1 : Sum of all Submatrices
# Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

# Example Input
# A = [ [1, 1]
#       [1, 1] ]
# Example Output
# 16

# Example Explanation
# Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
# Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
# Number of submatrices with 3 elements = 0
# Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
# Total Sum = 4+8+4 = 16


## Solution is using contribution technique

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        sumOfSubMatrices = 0
        
        for i in range(len(A[0])):
            for j in range(len(A)):
                ijRepetitions = (i+1)*(j+1)*(N-i)*(M-j)

                ijContributionInSubMatricesSum = (A[i][j] * ijRepetitions)

                sumOfSubMatrices += ijContributionInSubMatricesSum
        
        return sumOfSubMatrices

 


