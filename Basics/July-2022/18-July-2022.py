# 1 : Add the matrices

# You are given two matrices A & B of same size, 
# you have to return another matrix which is the sum of A and B.

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] += B[i][j]
        return A        


# 2 : Anti Diagonals
# Give a N * N square matrix A, return an array of its anti-diagonals. 
# Look at the example for more details.
