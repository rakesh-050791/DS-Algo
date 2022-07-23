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
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        res=[[0]*n for r in range(2*n-1)]
        for j in range(n):
            x , y = 0, j 
            while(x < n and y >= 0):
                res[x+y][x] = A[x][y]
                x += 1
                y -= 1

        for i in range(1, n):
            x, y, l = i, n-1, 0

            while(x < n and y >= 0):
                res[x+y][l] = A[x][y]
                x += 1
                y -= 1
                l += 1
        return res

# 3 : Column Sum
# You are given a 2D integer matrix A, 
# return a 1D integer vector containing column-wise sums of original matrix.
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        result = []
    
        for j in range(len(A[0])):
            sums = 0
            for i in range(n):
                sums += A[i][j]
            result.append(sums)
        return result



# 4 : Matrix Multiplication
# You are given two integer matrices A(having M X N size) and B(having N X P). 
# You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        rows = len(A)
        cols = len(B[0])

        C = [[0]* cols for i in range(rows)]

        for i in range(len(C)):
            for j in range(len(C[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        return C


# 5 : Matrix Transpose
# You are given a matrix A, you have to return another matrix which is the transpose of A.

# NOTE: Transpose of a matrix A is defined as - AT[i][j] = A[j][i] ; Where 1 ≤ i ≤ col and 1 ≤ j ≤ row

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        transposed_matrix = []
        for col in range(len(A[0])):
            result_matrix = []
            for row in range(len(A)):
                result_matrix.append(A[row][col])
            transposed_matrix.append(result_matrix)
        
        return(transposed_matrix)


















