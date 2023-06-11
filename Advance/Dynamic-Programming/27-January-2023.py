# 1 : Russian Doll envelopes

# Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.

# One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# Find the maximum number of envelopes you can put one inside other.



# Problem Constraints
# 1 <= N <= 1000
# 1 <= A[i][0], A[i][1] <= 109



# Input Format
# The only argument given is the integer matrix A.



# Output Format
# Return an integer denoting the maximum number of envelopes you can put one inside other.



# Example Input
# Input 1:

#  A = [ 
#          [5, 4]
#          [6, 4]
#          [6, 7]
#          [2, 3]  
#      ]
# Input 2:

#  A = [     '
#          [8, 9]
#          [8, 18]    
#      ]


# Example Output
# Output 1:

#  3
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Step 1: put [2, 3] inside [5, 4]
#  Step 2: put [5, 4] inside [6, 7]
#  3 envelopes can be put one inside other.
# Explanation 2:

#  No envelopes can be put inside any other so answer is 1.

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda item: (item[0], -item[1]))
        N = len(A)
        
        dp = [[-1]*(N+1) for _ in range(N+1)]
        
        def LIS(indx,prev_indx):
            if indx >= N:
                return 0
            
            if dp[indx][prev_indx] != -1:
                return dp[indx][prev_indx]
            
            # dont_take 
            
            dont_take = LIS(indx+1, prev_indx)
            take_it   = -1
            
            
            # to take the element cur_ele should be greater than prev element
            cur_w , cur_h = A[indx][0] , A[indx][1]
            pre_w , pre_h = A[prev_indx][0] , A[prev_indx][1]
            
            if prev_indx == -1 or (cur_w > pre_w and cur_h > pre_h):
                take_it =  1 + LIS(indx+1,indx)
                
            dp[indx][prev_indx] = max(dont_take,take_it)
            
            return  dp[indx][prev_indx]
        
        
        return LIS(0,-1)


