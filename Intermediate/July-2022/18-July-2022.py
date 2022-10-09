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



# 6 : Matrix Subtraction 

# You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M)). You have to subtract matrix A from B and return the resultant matrix. (i.e. return the matrix A - B).

# If X and Y are two matrices of the same order (same dimensions). Then X - Y is a matrix of the same order as X and Y and its elements are obtained by subtracting the elements of Y from the corresponding elements of X. Thus if Z = [z[i][j]] = X - Y, then [z[i][j]] = [x[i][j]] – [y[i][j]].

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(B[0])):
                A[i][j] -= B[i][j]
        return A


# 7 : Rotate Matrix
# You are given a n x n 2D matrix A representing an image.
# Rotate the image by 90 degrees (clockwise).
# You need to do this in place.
# Note: If you end up using an additional array, you will only receive partial score.

class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)

        for col in range(1, n) :
            for row in range(col) :
                A[col][row], A[row][col] = A[row][col], A[col][row]

        for element in A:
            element.reverse()

        return A

# 8 : Spiral Order Matrix II
# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and 
# return the generated square matrix.
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        n = A
        rows, cols = A, A
        resultMatrix = [[0 for i in range(cols)] for j in range(rows)]

        k = 1
        d, i , j = 0, 0, 0
        nSquare = n*n 

        while(k <= nSquare ):

            resultMatrix[i][j] = k
            k += 1

            # Moving in right direction
            if d == 0:
                j += 1
                if (j == n or resultMatrix[i][j] != 0): # Changing direction from right to down
                    d = 1
                    j -= 1
                    i += 1 

            # Moving in Down direction
            elif d == 1:
                i += 1
                if (i == n or resultMatrix[i][j] != 0): # Changing direction from Down to Left
                    d = 2
                    i  -= 1 
                    j  -= 1 

            # Moving in Left direction
            elif d == 2:
                j -= 1
                if (j < 0 or resultMatrix[i][j] != 0): # Changing direction from Left to Up
                    d = 3
                    i -= 1
                    j += 1

            # Moving in Up direction
            elif d == 3:
                i -= 1
                if (i < 0 or resultMatrix[i][j] != 0): # Changing direction from up to Right
                    d = 0
                    i += 1
                    j += 1

        return resultMatrix
            

# 9 : Row to Column Zero
# You are given a 2D integer matrix A, 
# make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        rows = len(A)
        cols = len(A[0])

        rowIndex = set()
        colIndex = set()

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 0:
                    rowIndex.add(i)
                    colIndex.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in rowIndex or j in colIndex:
                    A[i][j] = 0
        
        return A
# TIME COMPLEXITY- O(M*N) where M and N are the number of rows and columns respectively.
# SPACE COMPLEXITY- O(M+N)



# 10 : Row Sum
# You are given a 2D integer matrix A, return a 1D integer array containing row-wise sums of original matrix.

# Example Input
# Input 1:

# [1,2,3,4]
# [5,6,7,8]
# [9,2,3,4]


# Example Output
# Output 1: {10,26,18}

# Explanation 1

# Row 1 = 1+2+3+4 = 10
# Row 2 = 5+6+7+8 = 26
# Row 3 = 9+2+3+4 = 18

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        output = []

        for i in range(0, len(A)):
            sum = 0
            for j in range(0,len(A[0])):
                sum += A[i][j]
            output.append(sum)
        return output


# 11 : Main Diagonal Sum
# You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.

# Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

# Example Input
# Input 1:

#  A = [[1, -2, -3],
#      [-4, 5, -6],
#      [-7, -8, 9]]

# Output 1: 15 

# Explanation 1:

#  A[1][1] + A[2][2] + A[3][3] = 1 + 5 + 9 = 15

class Solution:
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        result = 0
        for i in range(rows):
            for j in range(cols):
                if i == j:
                    result += A[i][j]
        
        return result


