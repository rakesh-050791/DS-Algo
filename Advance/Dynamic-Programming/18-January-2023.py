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

        # Traverse through every digit from 1 to
        # 9 and count numbers beginning with it
        for i in range(1, 10):
            if (B - i >= 0):
                output += self.digitsCount(dp, A-1, B-i)
                output %= MODULO
        
        return output

    def digitsCount(self, dp, A, summ):
        if (A == 0):
            return summ == 0

        # If this subproblem is already evaluated,
        # return the evaluated value

        if dp[A][summ] != -1:
            return dp[A][summ]

        result = 0

        # Traverse through every digit and
        # recursively count numbers beginning
        # with it
        for i in range(10):
            if (summ - i >= 0):
                result += self.digitsCount(dp, A-1, summ-i)
                result %= MODULO 
        dp[A][summ] = result
        
        return dp[A][summ]


# 3 : Dungeon Princess

# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial health so that he is able to rescue the princess.



# Problem Constraints
# 1 <= M, N <= 500

# -100 <= A[i] <= 100



# Input Format
# First and only argument is a 2D integer array A denoting the grid of size M x N.



# Output Format
# Return an integer denoting the knight's minimum initial health so that he is able to rescue the princess.



# Example Input
# Input 1:

#  A = [ 
#        [-2, -3, 3],
#        [-5, -10, 1],
#        [10, 30, -5]
#      ]
# Input 2:

#  A = [ 
#        [1, -1, 0],
#        [-1, 1, -1],
#        [1, 0, -1]
#      ]


# Example Output
# Output 1:

#  7
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Initially knight is at A[0][0].
#  If he takes the path RIGHT -> RIGHT -> DOWN -> DOWN, the minimum health required will be 7.
#  At (0,0) he looses 2 health, so health becomes 5.
#  At (0,1) he looses 3 health, so health becomes 2.
#  At (0,2) he gains 3 health, so health becomes 5.
#  At (1,2) he gains 1 health, so health becomes 6.
#  At (2,2) he looses 5 health, so health becomes 1.
#  At any point, the health point doesn't drop to 0 or below. So he can rescue the princess with minimum health 7.
 
# Explanation 2:

#  Take the path DOWN -> DOWN ->RIGHT -> RIGHT, the minimum health required will be 1.

import sys 
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        n = len(A)
        m = len(A[0])

        dp = [[-1] * m for _ in range(n)]

        return self.minHealth(A, dp, 0, 0)

    def minHealth(self, mat, dp, i, j):
        if (i == len(mat)-1 and j == len(mat[0])-1):
            return max(1, 1 - mat[i][j])

        if (i == len(mat) or j == len(mat[0])):
            return float('inf')

        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = max(min(self.minHealth(mat, dp, i+1, j), self.minHealth(mat, dp, i, j+1)) - mat[i][j], 1)

        return dp[i][j]



# 4 : Min Sum Path in Triangle

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# Adjacent numbers for jth column of ith row is jth and (j+1)th column of (i + 1)th row



# Problem Constraints
# |A| <= 1000

# A[i] <= 1000



# Input Format
# First and only argument is the vector of vector A defining the given triangle



# Output Format
# Return the minimum sum



# Example Input
# Input 1:

 
# A = [ 
#          [2],
#         [3, 4],
#        [6, 5, 7],
#       [4, 1, 8, 3]
#     ]
# Input 2:

#  A = [ [1] ]


# Example Output
# Output 1:

#  11
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Explanation 2: Only 2 can be collected.

# Approach 1

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)

        for i in range(n - 2, -1, -1):
            for j in range(len(A[i])):
                A[i][j] += min(A[i + 1][j], A[i + 1][j + 1])

        return A[0][0]


# Approach 2

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        dp = [[float('inf')] * n for _ in range(n)]

        return self.dfs(A, n, dp, 0, 0)

    
    def dfs(self, A, n, dp, i, j):

        #Base case: we have reached the last row, so return the value of the current cell
        if i == n-1:
            return A[i][j]

        if dp[i][j] != float('inf'):
            return dp[i][j]

        left = self.dfs(A, n, dp, i+1 , j)
        right = self.dfs(A, n, dp, i+1, j+1)  

        dp[i][j] = A[i][j] + min(left, right)

        return dp[i][j]


