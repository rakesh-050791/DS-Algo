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