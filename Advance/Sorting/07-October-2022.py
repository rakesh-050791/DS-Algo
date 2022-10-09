# 1 : Kth Smallest Element
# Find the Bth smallest element in given array A .

# NOTE: Users should try to solve it in less than equal to B swaps.

# Example Input
# Input 1:

# A = [2, 1, 4, 3, 2]
# B = 3

# Output 1: 2

# Explanation 1: 3rd element after sorting is 2.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        n = len(A)
        for i in range(len(A)):
            minElement = A[i]
            newIndex = i

            for j in range(i, n):
                if A[j] < minElement:
                    minElement = A[j]
                    newIndex = j
            
            #Swapping
            temp = A[newIndex]
            A[newIndex] = A[i]
            A[i] = temp

            if (i+1==B):
                break;
        
        return A[B-1]
        
