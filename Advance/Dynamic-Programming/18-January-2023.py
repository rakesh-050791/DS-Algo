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


#  5: Ways to Decode

# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.



# Problem Constraints
# 1 <= length(A) <= 105



# Input Format
# The first and the only argument is a string A.



# Output Format
# Return an integer, representing the number of ways to decode the string modulo 109 + 7.



# Example Input
# Input 1:

#  A = "12"
# Input 2:

#  A = "8"


# Example Output
# Output 1:

#  2
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
#  The number of ways decoding "12" is 2.
# Explanation 2:

#  Given encoded message "8", it could be decoded as only "H" (8).
#  The number of ways decoding "8" is 1.


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        mod = 10**9 + 7
        N = len(A)
        if N == 0 :
            return 0
        if A[0] == "0":
            return 0
        dp = [0] * (N+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, N+1):
            if int(A[i-1]) >= 1 and int(A[i-1]) <= 9:
                dp[i] = dp[i-1]
            if int(A[i-2]) == 1 or (int(A[i-2]) == 2 and int(A[i-1])>= 0 and int(A[i-1]) <= 6):
                dp[i] = (dp[i] + dp[i-2]) % mod
        return dp[N]


# 6 : Max Product Subarray

# Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

# Return an integer corresponding to the maximum product possible.

# NOTE: Answer will fit in 32-bit integer value.



# Problem Constraints
# 1 <= N <= 5 * 105

# -100 <= A[i] <= 100



# Input Format
# First and only argument is an integer array A.



# Output Format
# Return an integer corresponding to the maximum product possible.



# Example Input
# Input 1:

#  A = [4, 2, -5, 1]
# Input 2:

#  A = [-3, 0, -5, 0]


# Example Output
# Output 1:

#  8
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  We can choose the subarray [4, 2] such that the maximum product is 8.
# Explanation 2:

#  0 will be the maximum product possible.

# Solution reference : https://www.youtube.com/watch?v=lXVy6YWFcRM 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        result = max(A)
        currMin , currMax = 1, 1

        for n in A:
            temp = n * currMax

            currMax = max(n * currMax, n * currMin, n )
            currMin = min(temp, n * currMin, n)

            result = max(result, currMax)

        return result

# Another approach :

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        result = max(A)
        currMin , currMax = 1, 1

        for n in A:
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if n < 0:
                currMax, currMin = currMin, currMax

            currMax = max(n * currMax, n)
            currMin = min(n * currMin, n)

            result = max(result, currMax)

        return result


# 7 : Maximum Sum Value

# You are given an array A of N integers and three integers B, C, and D.

# You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.



# Problem Constraints

# 1 <= N <= 105

# -10000 <= A[i], B, C, D <= 10000



# Input Format

# First argument is an array A
# Second argument is an integer B
# Third argument is an integer C
# Fourth argument is an integer D



# Output Format

# Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.



# Example Input

# Input 1:

#  A = [1, 5, -3, 4, -2]
#  B = 2
#  C = 1
#  D = -1
# Input 2:

#  A = [3, 2, 1]
#  B = 1
#  C = -10
#  D = 3


# Example Output

# Output 1:

#  18
# Output 2:

#  -4


# Example Explanation

# Explanation 1:

#  If you choose i = 2, j = 2, and k = 3 then we will get
#  A[2]*B + A[2]*C + A[3]*D = 5*2 + 5*1 + (-3)*(-1) = 10 + 5 + 3 = 18
# Explanation 2:

#  If you choose i = 1, j = 3, and k = 3 then we will get
#  A[1]*B + A[3]*C + A[3]*D = (3*1) + (-10*1) + (3*1) = 3 - 10 + 3 = -4


# Expected Output
# Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)
       
        # Create a dp array to store the answers of previous states
        dp = [[float("-inf")] * 3 for _ in range(N+1)]
       
        for i in range(1, N+1):
            j = i-1  # j is used to keep track of the previous element
           
            # Compute the maximum value of A[i]*B
            dp[i][0] = max(dp[j][0], A[j]*B)
           
            # Compute the maximum value of A[i]*B + A[j]*C
            dp[i][1] = max(dp[j][1], dp[i][0]+A[j]*C)
           
            # Compute the maximum value of A[i]*B + A[j]*C + A[k]*D
            dp[i][2] = max(dp[j][2], dp[i][1]+A[j]*D)
       
   
        return dp[N][2]


# 8 : Min Sum Path in Matrix
# Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Return the minimum sum of the path.

# NOTE: You can only move either down or right at any point in time.



# Problem Constraints
# 1 <= M, N <= 2000

# -1000 <= A[i][j] <= 1000



# Input Format
# First and only argument is a 2-D grid A.



# Output Format
# Return an integer denoting the minimum sum of the path.



# Example Input
# Input 1:

#  A = [
#        [1, 3, 2]
#        [4, 3, 1]
#        [5, 6, 1]
#      ]
# Input 2:

#  A = [
#        [1, -3, 2]
#        [2, 5, 10]
#        [5, -5, 1]
#      ]


# Example Output
# Output 1:

#  8
# Output 2:

#  -1


# Example Explanation
# Explanation 1:

#  The path will be: 1 -> 3 -> 2 -> 1 -> 1.
# Input 2:

#  The path will be: 1 -> -3 -> 5 -> -5 -> 1.

# Top Down Memoization

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        n = len(A)
        m = len(A[0])

        dp = [[0] * m for _ in range(n)]

        self.getPathSum(dp, A, n-1, m-1)

        return dp[n-1][m-1]

    
    def getPathSum(self, dp, A, i, j):
        if i < 0 or j < 0:
            return float('inf')
        
        if i == 0 and j == 0:
            dp[i][j] = A[i][j]
            return dp[i][j]
        
        if dp[i][j] == 0:
            dp[i][j] = min(self.getPathSum(dp, A, i-1, j), self.getPathSum(dp, A, i, j-1)) + A[i][j]

        return dp[i][j]

        # TC: O(MN); SC: O(MN)


# 9 : Unbounded Knapsack

# Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit in this quantity.

# This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.



# Problem Constraints
# 1 <= A <= 1000

# 1 <= |B| <= 1000

# 1 <= B[i] <= 1000

# 1 <= C[i] <= 1000



# Input Format
# First argument is the Weight of knapsack A

# Second argument is the vector of values B

# Third argument is the vector of weights C



# Output Format
# Return the maximum value that fills the knapsack completely



# Example Input
# Input 1:

# A = 10
# B = [5]
# C = [10]
# Input 2:

# A = 10
# B = [6, 7]
# C = [5, 5]


# Example Output
# Output 1:

#  5
# Output 2:

# 14


# Example Explanation
# Explanation 1:

# Only valid possibility is to take the given item.
# Explanation 2:

# Take the second item twice.

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        # Initialize a list `ds` of size `A+1` with all zeros
        ds = [0]*(A+1)
        # Get the length of the list of values and weights of items
        N = len(B)
        
        # Loop through each item
        for i in range(N):
            # Loop through all the weights from the weight of the item to the knapsack weight `A`
            for j in range(C[i], A+1):
                # Calculate the maximum value that can be obtained by either not taking the current item or taking the current item
                ds[j] = max(ds[j], ds[j-C[i]]+B[i])
                
        # Return the maximum value that can be obtained by filling the knapsack of weight `A` with items from the given set
        return ds[A]


# 9 : Flip Array

# Given an array A of positive elements, you have to flip the sign of some of its elements such that the resultant sum of the elements of array should be minimum non-negative(as close to zero as possible).

# Return the minimum number of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.



# Problem Constraints

# 1 <= length of(A) <= 100

# Sum of all the elements will not exceed 10,000.



# Input Format

# First and only argument is an integer array A.



# Output Format

# Return an integer denoting the minimum number of elements whose sign needs to be flipped.



# Example Input

# Input 1:

#  A = [15, 10, 6]
# Input 2:

#  A = [14, 10, 4]


# Example Output

# Output 1:

#  1
# Output 2:

#  1


# Example Explanation

# Explanation 1:

#  Here, we will flip the sign of 15 and the resultant sum will be 1.
# Explanation 2:

#  Here, we will flip the sign of 14 and the resultant sum will be 0.
#  Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there sign are not minimum.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        arrsum = sum(A)
        target = arrsum // 2

        dp = [[n + 1 for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if A[i-1] <= j:
                    dp[i][j] = min(1 + dp[i-1][j-A[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        for i in range(target, -1, -1):
            if dp[n][i] < n:
                return dp[n][i]


# 10 : Buying Candies

# Rishik likes candies a lot. So, he went to a candy-shop to buy candies.

# The shopkeeper showed him N packets each containg A[i] candies for cost of C[i] nibbles, each candy in that packet has a sweetness B[i]. The shopkeeper puts the condition that Rishik can buy as many complete candy-packets as he wants but he can't buy a part of the packet.

# Rishik has D nibbles, can you tell him the maximum amount of sweetness he can get from candy-packets he will buy?


# Problem Constraints
# 1 <= N <= 700

# 1 <= A[i] <= 1000

# 1 <= B[i] <= 1000

# 1 <= C[i],D <= 1000



# Input Format
# First argument of input is an integer array A
# Second argument of input is an integer array B
# Third argument of input is an integer array C
# Fourth argument of input is an integer D


# Output Format
# Return a single integer denoting maximum sweetness of the candies that he can buy


# Example Input
# Input 1:

#  A = [1, 2, 3]
#  B = [2, 2, 10]
#  C = [2, 3, 9]
#  D = 8
# Input 2:

#  A = [2]
#  B = [5]
#  C = [10]
#  D = 99


# Example Output
# Output 1:

#  10
# Output 2:

#  90


# Example Explanation
# Explanation 1:

#  Choose 1 Packet of kind 1 = 1 Candy of 2 Sweetness = 2 Sweetness
#  Choose 2 Packet of kind 2 = 2 Candy of 2 Sweetness = 8 Sweetness
# Explanation 2:

#  Buy 9 Packet of kind 1. 18 Candy each of 5 Sweetness = 90 Sweetness


class Solution:
    # @param A : list of integers (number of candies in each packet)
    # @param B : list of integers (sweetness of each candy in each packet)
    # @param C : list of integers (cost of each packet in nibbles)
    # @param D : integer (total number of nibbles Rishik has)
    # @return an integer (maximum sweetness Rishik can get)

    def solve(self, A, B, C, D):
        N = len(A)  # number of candy packets
        sweetness=[A[i]*B[i] for i in range(N)]  # list to store sweetness of each candy packet
        dp = [0] * (D + 1)  # list to store the maximum sweetness for each number of nibbles from 0 to D

        for i in range(N):  # iterate over each candy packet in the shop
            for j in range(C[i], D + 1):  # iterate over each possible number of nibbles from C[i] to D
                # if we don't buy the current candy packet, we keep the same sweetness as before
                # otherwise, we add the sweetness of the candy packet to the best possible solution we can get with the remaining nibbles
                dp[j] = max(dp[j], dp[j - C[i]] + sweetness[i])

        return dp[D]  # return the maximum sweetness we can get with D nibbles
        

# 11 : Tushar's Birthday Party
# As it is Tushar's Birthday on March 1st, he decided to throw a party to all his friends at TGI Fridays in Pune. Given are the eating capacity of each friend, filling capacity of each dish and cost of each dish. A friend is satisfied if the sum of the filling capacity of dishes he ate is equal to his capacity. Find the minimum cost such that all of Tushar's friends are satisfied (reached their eating capacity).

# NOTE:

# Each dish is supposed to be eaten by only one person. Sharing is not allowed.

# Each friend can take any dish unlimited number of times.

# There always exists a dish with filling capacity 1 so that a solution always exists.



# Problem Constraints
# |A| <= 1000

# |B| <= 1000

# |C| <= 1000



# Input Format
# First Argument is vector A, denoting eating capacities

# Second Argument is vector B, denoting filling capacities

# Third Argument is vector C, denoting cost



# Output Format
# Return a single integer, the answer to the problem



# Example Input
# Input 1:

# A = [2, 4, 6]
# B = [2, 1, 3]
# C = [2, 5, 3]
# Input 2:

# A = [2]
# B = [1]
# C = [2]


# Example Output
# Output 1:

# 12
# Output 2:

# 4


# Example Explanation
# Explanation 1:

# First friend takes dish 1, Second friend takes dish 1 twice and third friend takes dish 3 twice.
# So 2 + 2*2 + 3*2 = 12.
# Explanation 2:

# Only way is to take 2 dishes of cost 2, hence 4.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):

        max_appetite = max(A)
        N = len(B)

        dp = [float('inf')]*(max_appetite+1)
        dp[0] = 0

        for i in range(N):
            for j in range(B[i], max_appetite+1):
                dp[j] = min(dp[j], C[i] + dp[j-B[i]])

        min_cost = 0
        for capacity in A:
            min_cost += dp[capacity]
        return min_cost

