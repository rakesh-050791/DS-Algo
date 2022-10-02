# 1 : A, B & Modulo

# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

# Example Input
# Input 1:

# A = 1
# B = 2

# Example Output
# Output 1: 1

# Explanation 1:
# 1 is the largest value of M such that A % M == B % M.

# Approach 

# Lets say r is the remainder ,
# A%M = B%M = r
# p & q are the quotients for A/M , B/M
# A= M*p + r , B = M*q + r  
# r = A-Mp  -----(1)
# r = B-Mq  -----(2)
# Equating (1) & (2)
# A-Mp = B-Mq
# A-B = M(p-q)
# M = (A-B) / (p-q)
# For M to be maximum , (p-q) has to be minimum
# 1 is the possible minimum value for (p-q)
# => M = (A-B) / 1
# So M is the difference between A,B


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A-B)

