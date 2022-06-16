# 1 : You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        result = A
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                result[i][j] = A[i][j] + B[i][j]
        return(result)

# 2 :



# 3 : Given an array A, check if it is sorted in non decreasing order or not.

