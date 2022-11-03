# 1 : Count Rectangles

# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in a 2-D Cartesian plane.

# Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.


# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer array B.



# Output Format
# Return the number of unordered quadruplets that form a rectangle.



# Example Input
# Input 1:

#  A = [1, 1, 2, 2]
#  B = [1, 2, 1, 2]
# Input 1:

#  A = [1, 1, 2, 2, 3, 3]
#  B = [1, 2, 1, 2, 1, 2]


# Example Output
# Output 1:

#  1
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  All four given points make a rectangle. So, the answer is 1.
# Explanation 2:

#  3 quadruplets which make a rectangle are: (1, 1), (2, 1), (2, 2), (1, 2)
#                                            (1, 1), (3, 1), (3, 2), (1, 2)
#                                            (2, 1), (3, 1), (3, 2), (2, 2)


class Solution:
    def solve(self, A, B):
        # find the diagonal points as (x1,y1) and (x2,y2) 
        # and then check whether (x2,y1) and (x1,y2) points exist or not
        n = len(A)
        result = 0
        hashSet = set()

        for idx in range(n):
            element = str(A[idx]) +'@'+ str(B[idx])
            hashSet.add(element)

        for i in range(n):
            for j in range(i+1, n):
                x1, x2 = A[i], A[j]
                y1, y2 = B[i], B[j]

                # We have to look for the diogonal points so x1 != x2 and y1 != y2
                if (x1 != x2 and y1 != y2):
                    str1 = str(x1) +'@'+ str(y2)
                    str2 = str(x2) +'@'+ str(y1)

                    if (str1 in hashSet) and (str2 in hashSet):
                        result += 1
        
        #  Because we are iterating on each points, so above condition will be true
        #  for x1,y1, x2,y2 and x2,y2 , x1,y1 which is coming twice.
        #  So we have to divide the result by 2 for correct answer
        return result // 2
                    

# TC : O (N^2)
# SC : O (N)

