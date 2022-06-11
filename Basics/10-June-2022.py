# 1 : Given a 2D array A of N rows and M columns. Find value of largest element in each row.

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        elements = A
        result = []
        for i in range(len(elements)):
            result.append(max(elements[i]))
        return(result)


# 2 : You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        result_matrix = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                product = B * A[i][j]
                row.append(product)
            result_matrix.append(row)
        return(result_matrix)

# 3 : You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.

# Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        sum = 0

        for i in range(len(A)):
            sum += A[i][i]
        return(sum)

# 4 : You are given a 2D integer matrix A, return a 1D integer vector containing row-wise sums of original matrix.
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):

        result = []
        for row in range(len(A)):
            sum = 0
            for col in range(len(A[row])):
                sum +=  A[row][col]
            result.append(sum)
        return(result)

# 5 : You are given a matrix A, you have to return another matrix which is the transpose of A.

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





# 6 : Given a 2D integer array C[][] of A rows and B columns. 
 # Return an integer array of size B that represents the sums of the columns of the 2D array C.

 class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return a list of integers

    def solve(self, A, B, C):
         
        result = []

        for row in range(B):
            sum = 0
            for col in range(A):
                sum += C[col][row]
            result.append(sum)
        return(result)


# 7 : You are given two matrices A & B of equal dimensions and you have to check whether two matrices are equal or not.

# NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j in the given range.

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != B[i][j]:
                    return 0 
        return 1


# 8 : Write a program to input an integer N and a N*N matrix Mat from user and print the matrix in wave form (column wise)

# See example for clarifications regarding wave print.
def main():
    
    matrix_size = int(input())
    result_matrix = []

    for i in range(matrix_size):
        result_matrix.append(list(map(int, input().split())))
    
    # print('Printing result_matrix %s' % result_matrix)
    #  [[4, 1, 2], [7, 4, 4], [3, 7, 4]]

    #   4 7 3 7 4 1 2 4 4

    for j in range (matrix_size):
        if j%2==0:
            for i in range(matrix_size):
                print(result_matrix[i][j],end= " ")
        else:
            for i in range(matrix_size):
                print(result_matrix[matrix_size-i-1][j],end= ' ')

if __name__ == '__main__':
    main()



# 9 :



# 10 :
# You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M)). 
# You have to subtract matrix A from B and return the resultant matrix. (i.e. return the matrix A - B).

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        final_matrix = []

        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                diff = A[i][j] - B[i][j]
                row.append(diff)
            final_matrix.append(row)







