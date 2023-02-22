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


# 2 : Unique 2D points

# Given a 2D array A of integer points on a 2D plane. Find and return the number of unique points in the array.
# The ith point in the array is (A[i][0], A[i][1])

# Input Format
# The first argument is a 2D integer array A.


# Output Format
# Return an integer that is the number of unique points.


# Example Input
# Input:
# A = [[5, 6],
#      [2, 8],
#      [-1, -1],
#      [2, -3],
#      [2, 8],
#      [7, 7],
#      [2, -3]]


# Example Output
# Output:
# 5


# Example Explanation
# Explanation:
# There are 5 unique points in the given array.


# Approach 1
class Solution:
    def solve(self, A):
        n = len(A)
        hashSet = set()

        for i in range(n):
            x = A[i][0]
            y = A[i][1]

            element = str(x) +'@'+ str(y)
            hashSet.add(element)
        return len(hashSet)


# Approach 2 (using python tuple)
class Solution:
    def solve(self, A):
        n = len(A)
        hashSet = set()
        
        for i in range(n):
            x = A[i][0]
            y = A[i][1]

            element = (str(x), str(y))
            hashSet.add(element)
        return len(hashSet)


# 3 : Common Elements

# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.

# NOTE:

# Each element in the result should appear as many times as it appears in both arrays.
# The result can be in any order.


# Problem Constraints
# 1 <= N, M <= 105

# 1 <= A[i] <= 109



# Input Format
# First argument is an integer array A of size N.

# Second argument is an integer array B of size M.



# Output Format
# Return an integer array denoting the common elements.



# Example Input
# Input 1:

#  A = [1, 2, 2, 1]
#  B = [2, 3, 1, 2]
# Input 2:

#  A = [2, 1, 4, 10]
#  B = [3, 6, 2, 10, 10]


# Example Output
# Output 1:

#  [1, 2, 2]
# Output 2:

#  [2, 10]


# Example Explanation
# Explanation 1:

#  Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
# Explantion 2:

#  Elements (2, 10) appears in both the array.

class Solution:
    def solve(self, A, B):
        n = len(A)
        m = len(B)

        hashMapA = {}
        result = []

        for k in A:
            if k in hashMapA:
                hashMapA[k] += 1
            else:
                hashMapA[k] = 1

        for i in range(m):
            if B[i] in hashMapA:
                if hashMapA[B[i]] > 0:
                    result.append(B[i])
                    hashMapA[B[i]] -= 1
        
        return result
        