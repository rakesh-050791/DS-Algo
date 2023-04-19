# 1 : Unique Paths in a Grid
# Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

# Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.



# Problem Constraints
# 1 <= n, m <= 100
# A[i][j] = 0 or 1



# Input Format
# Firts and only argument A is a 2D array of size n * m.



# Output Format
# Return an integer denoting the number of unique paths from (1, 1) to (n, m).



# Example Input
# Input 1:

#  A = [
#         [0, 0, 0]
#         [0, 1, 0]
#         [0, 0, 0]
#      ]
# Input 2:

#  A = [
#         [0, 0, 0]
#         [1, 1, 1]
#         [0, 0, 0]
#      ]


# Example Output
# Output 1:

#  2
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Possible paths to reach (n, m): {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)} and {(1 ,1), (2, 1), (3, 1), (3, 2), (3, 3)}  
#  So, the total number of unique paths is 2. 
# Explanation 2:

#  It is not possible to reach (n, m) from (1, 1). So, ans is 0.


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
        n = len(A)
        m = len(A[0])

        dp = [[-1] * m for _ in range(n)]

        return self.uniqueWays(A, dp, n-1, m-1)
    
    def uniqueWays(self, A, dp, i, j):
        if i < 0 or j < 0:
            return 0

        if A[i][j] == 1:
            dp[i][j] = 0
            return dp[i][j]
  
        if i == 0 and j == 0:
            dp[i][j] = 1
            return dp[i][j]

        if dp[i][j] != -1:
            return dp[i][j]


        dp[i][j] = self.uniqueWays(A, dp, i-1, j) + self.uniqueWays(A, dp, i, j-1)

        return dp[i][j]


# 2 : N digit numbers

# Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.

# Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.

# Since the answer can be large, output answer modulo 1000000007



# Problem Constraints
# 1 <= A <= 1000

# 1 <= B <= 10000



# Input Format
# First argument is the integer A

# Second argument is the integer B



# Output Format
# Return a single integer, the answer to the problem



# Example Input
# Input 1:

#  A = 2
#  B = 4
# Input 2:

#  A = 1
#  B = 3


# Example Output
# Output 1:

#  4
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Valid numbers are {22, 31, 13, 40}
#  Hence output 4.
# Explanation 2:

#  Only valid number is 3

MODULO = 1000000007
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        dp = [[-1]*(B+1) for _ in range(A+1)]
        dp[0][0] = 1

        output = 0

        for i in range(1, 10):
            if (B - i >= 0):
                output += self.digitsCount(dp, A-1, B-i)
                output %= MODULO
        
        return output

    def digitsCount(self, dp, A, summ):
        if (A == 0):
            return summ == 0

        if dp[A][summ] != -1:
            return dp[A][summ]

        result = 0

        for i in range(10):
            if (summ - i >= 0):
                result += self.digitsCount(dp, A-1, summ-i)
                result %= MODULO 
        dp[A][summ] = result
        
        return dp[A][summ]


