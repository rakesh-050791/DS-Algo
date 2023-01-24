# 1 : Cutting a Rod

# Given a rod of length N units and an array A of size N denotes prices that contains prices of all pieces of size 1 to N.

# Find and return the maximum value that can be obtained by cutting up the rod and selling the pieces.



# Problem Constraints
# 1 <= N <= 1000

# 0 <= A[i] <= 106



# Input Format
# First and only argument is an integer array A of size N.



# Output Format
# Return an integer denoting the maximum value that can be obtained by cutting up the rod and selling the pieces.



# Example Input
# Input 1:

#  A = [3, 4, 1, 6, 2]
# Input 2:

#  A = [1, 5, 2, 5, 6]


# Example Output
# Output 1:

#  15
# Output 2:

#  11


# Example Explanation
# Explanation 1:

#  Cut the rod of length 5 into 5 rods of length (1, 1, 1, 1, 1) and sell them for (3 + 3 + 3 + 3 + 3) = 15.
# Explanation 2:

#  Cut the rod of length 5 into 3 rods of length (2, 2, 1) and sell them for (5 + 5 + 1) = 11.

import sys
sys.setrecursionlimit(10**6) 
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N     = len(A)
        cost    = A 
        
        rods = [i+1 for i in range(N)]

        dp    = [ [-1] * (N+1) for i in range(N+1) ]

        def CoinChageII(indx,amount_used):
            if indx < 0 or amount_used < 0:
                return 0


            if dp[indx][amount_used] != -1:
                return dp[indx][amount_used]

            dont_take = CoinChageII(indx-1 , amount_used)

            take_it   = 0

            if rods[indx] <= amount_used:
                take_it = cost[indx] + CoinChageII(indx , amount_used - rods[indx])

            dp[indx][amount_used] = max(take_it,dont_take)

            return dp[indx][amount_used]


        return CoinChageII(N-1,N)

