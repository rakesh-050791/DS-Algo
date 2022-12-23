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
        

# 2 : Merge Two Sorted Arrays
# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.

# Input Format
# First Argument is a 1-D array representing A.

# Second Argument is also a 1-D array representing B.



# Output Format
# Return a 1-D vector which you got after merging A and B.



# Example Input
# Input 1:

# A = [4, 7, 9 ]
# B = [2, 11, 19 ]
# Input 2:

# A = [1]
# B = [2]


# Example Output
# Output 1:

# [2, 4, 7, 9, 11, 19]
# Output 2:

# [1, 2]


# Example Explanation
# Explanation 1:

# Merging A and B produces the output as described above.
# Explanation 2:

#  Merging A and B produces the output as described above.


class Solution:
    def solve(self, A, B):
        M = len(A)
        N = len(B)

        C = [0] * (N+M)

        P1, P2, P3 = 0, 0, 0

        while P1 < M and P2 < N:
            if A[P1] <= B[P2]:
                C[P3] = A[P1]
                P1 += 1
                P3 += 1
            else:
                C[P3] = B[P2]
                P2 += 1
                P3 += 1
        
        while P1 < M:
            C[P3] = A[P1]
            P1 += 1
            P3 += 1
        
        while P2 < N:
            C[P3] = B[P2]
            P2 += 1
            P3 += 1
        
        return C