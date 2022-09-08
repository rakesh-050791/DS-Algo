# 1 : A, B and Modulo
# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A-B)


# 2 : Concatenate Three Numbers
# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.

# Return the minimum result obtained.
class Solution:
    def solve(self, A, B, C):
        minimumElement = min(A, B, C)
        maximumElement = max(A, B, C)
        middleElement = A + B + C - maximumElement - minimumElement
        
        return (minimumElement*10000 + middleElement*100 + maximumElement)


# 3 : Find if two rectangles overlap

# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
# For the first rectangle, its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left corner is (E, F), and the top right corner is (G, H).

# Find and return whether the two rectangles overlap or not.

# Example Input
# Input 1:

# A = 0   B = 0
# C = 4   D = 4
# E = 2   F = 2
# G = 6   H = 6

# Output 1:
# 1

# Explanation 1:
# Rectangle with bottom left (2, 2) and top right (4, 4) is overlapping.

# Solution Approach 
# we can formulate the required conditions.

# First, we can see if a foot of one rectangle is >= top of another rectangle, then an answer is not possible.

# You can make a similar argument about the y-axis.

class Solution:
    def solve(self, A, B, C, D, E, F, G, H):
        if A >= G or E >= C:
            return 0
        if D <= F or H <= B:
            return 0
        return 1

# 4 : Leap year? - III
# Given an integer A representing a year, Return 1 if it is a leap year else, return 0.

# A year is a leap year if the following conditions are satisfied:

# The year is multiple of 400.
# Else the year is multiple of 4 and not multiple of 100.

class Solution:
    def solve(self, A):
        n = A

        if n % 400 == 0:
            return 1

        if (n % 4 == 0 and  n % 100 != 0):
            return 1
    
        return 0




