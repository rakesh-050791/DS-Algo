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


# 2 : Sub-matrix Sum Queries

# Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

# Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

# NOTE:

# Rows are numbered from top to bottom, and columns are numbered from left to right.
# Sum may be large, so return the answer mod 109 + 7.
 

# Example Input
# Input 1:

#  A = [   [1, 2, 3]
#          [4, 5, 6]
#          [7, 8, 9]   ]
#  B = [1, 2]
#  C = [1, 2]
#  D = [2, 3]
#  E = [2, 3]

# Example Output
# Output 1:

#  [12, 28]

# Example Explanation
# Explanation 1:

#  For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
#  For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        rows = len(A)
        cols = len(A[0])
        prefixSum = [[0] * cols for i in range(rows)]

        # calculating rowwise prefixSum 
        for i in range(rows):
            sums = 0
            for j in range(cols):
                sums += A[i][j]
                prefixSum[i][j] = sums

        # calculating colwise prefixSum 
        for j in range(cols):
            sums = 0
            for i in range(rows):
                sums += prefixSum[i][j]
                prefixSum[i][j] = sums


        # subMatrix Sum calculation 
        result = []

        for i in range(len(B)):
            a1, b1 = B[i] - 1 , C[i] - 1 ## TopLeft corners
            a2, b2 = D[i] - 1 , E[i] - 1 ## BottomRight corners

            totalSum = prefixSum[a2][b2] ##(BottomRight prefixSum)

            # removing extra subArrays 

            ## removing left part
            if a1 > 0:
                totalSum -= prefixSum[a1 - 1][b2]

            ## removing top part 
            if b1 > 0:
                totalSum -= prefixSum[a2][b1 - 1]

            ## neutralizing common part 
            if a1 > 0 and b1 > 0:
                totalSum += prefixSum[a1 - 1][b1 - 1]

            result.append(totalSum % (10**9 + 7))

        return result
            











