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


# 2 : Ways to send the signal
# You are trying to send signals to aliens using a linear array of A laser lights. You don't know much about how the aliens are going to percieve the signals, but what you know is that if two consecutive lights are on then the aliens might take it as a sign of danger and destroy the earth.

# Find and return the total number of ways in which you can send a signal without compromising the safty of the earth. Return the ans % 109 + 7.



# Problem Constraints

# 1 <= A <= 105



# Input Format

# The only argument given is integer A.



# Output Format

# Return the ans%(109+7).



# Example Input

# Input 1:

#  A = 2
# Input 2:

#  A = 3


# Example Output

# Output 1:

#  3
# Output 2:

#  5


# Example Explanation

# Explanation 1:

#  OFF OFF
#  OFF ON 
#  ON OFF
# All lights off is also a valid signal which probably means 'bye'

# Explanation 2:

#  OFF OFF OFF
#  OFF OFF ON
#  OFF ON OFF 
#  ON OFF OFF
#  ON OFF ON

import sys
sys.setrecursionlimit(10**6)
class Solution:
# @param A : integer
# @return an integer
    def solve(self, A):
        MOD = 10**9 + 7
        if A == 0:
            return 1
        elif A == 1:
            return 2

        dp = [0] * (A + 1)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, A + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        return dp[A]


# 3 : Edit Distance
# Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character


# Problem Constraints
# 1 <= length(A), length(B) <= 450



# Input Format
# The first argument of input contains a string, A.
# The second argument of input contains a string, B.



# Output Format
# Return an integer, representing the minimum number of steps required.



# Example Input
# Input 1:

#  A = "abad"
#  B = "abac"
# Input 2:

#  A = "Anshuman"
#  B = "Antihuman


# Example Output
# Output 1:

#  1
# Output 2:

#  2


# Example Explanation
# Exlanation 1:

#  A = "abad" and B = "abac"
#  After applying operation: Replace d with c. We get A = B.
 
# Explanation 2:

#  A = "Anshuman" and B = "Antihuman"
#  After applying operations: Replace s with t and insert i before h. We get A = B.

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        dp = [[-1 for _ in range(len(B))] for _ in range(len(A))]
        return self.findDistance(A, B, len(A)-1, len(B)-1, dp)
            
    def findDistance(self, A, B, i, j, dp):
        if i == -1 and j == -1 :
            return 0
        elif i == -1 :
            return j+1
        elif j == -1 :
            return i+1
        elif dp[i][j] == -1 :
            if A[i] == B[j]:
                dp[i][j] = self.findDistance(A, B, i-1, j-1, dp)
            else:
                dp[i][j] = min(1+ self.findDistance(A, B, i-1, j, dp), 1+ self.findDistance(A, B, i, j-1, dp), 1+ self.findDistance(A, B, i-1,j-1, dp))
        return dp[i][j]



# 4 : Regular Expression Match

# Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

# ' ? ' : Matches any single character.
# ' * ' : Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).



# Problem Constraints
# 1 <= length(A), length(B) <= 104



# Input Format
# The first argument of input contains a string A.
# The second argument of input contains a string B.



# Output Format
# Return 1 if the patterns match else return 0.



# Example Input
# Input 1:

#  A = "aaa"
#  B = "a*"
# Input 2:

#  A = "acz"
#  B = "a?a"


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Since '*' matches any sequence of characters. Last two 'a' in string A will be match by '*'.
#  So, the pattern matches we return 1.
# Explanation 2:

#  '?' matches any single character. First two character in string A will be match. 
#  But the last character i.e 'z' != 'a'. Return 0.

import sys
sys.setrecursionlimit(10**7)
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        N = len(A)
        M = len(B)

        # initialize the DP table and the base cases
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True  # empty string matches empty pattern
        for j in range(1, M + 1):
            if B[j-1] == '*':
                dp[0][j] = dp[0][j-1]  # if pattern starts with '*', we can match with an empty string

        # fill the DP table in a bottom-up manner
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]  # current characters match, so we can check previous characters
                elif B[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]  # current pattern is '*', so we can either match zero or more characters
                else:
                    dp[i][j] = False  # current characters don't match, and pattern isn't '*', so no match

        return int(dp[N][M])


# 5 :  Interleaving Strings

# Given A, B, C find whether C is formed by the interleaving of A and B.



# Problem Constraints
# 1 <= length(A), length(B) <= 100

# 1 <= length(C) <= 200



# Input Format
# The first argument of input contains a string, A.
# The second argument of input contains a string, B.
# The third argument of input contains a string, C.



# Output Format
# Return 1 if string C is formed by interleaving of A and B else 0.



# Example Input
# Input 1:

#  A = "aabcc"
#  B = "dbbca"
#  C = "aadbbcbcac"
# Input 2:

#  A = "aabcc"
#  B = "dbbca"
#  C = "aadbbbaccc"


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)
# Explanation 2:

#  It is not possible to get C by interleaving A and B.

import sys 
sys.setrecursionlimit(10**6)
from functools import lru_cache

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return 0
        N , M = len(s1) , len(s2)

        @lru_cache(None)
        def recurBro(indx1 , indx2):
            if indx1 == N and indx2 == M:
                return True

            ans = False
            if indx1 < N and s1[indx1] == s3[indx1 + indx2]:
                ans |= recurBro(indx1 +1 , indx2 )
            if indx2 < M and s2[indx2] == s3[indx1 + indx2]:
                ans |= recurBro(indx1 , indx2 +1)
            return ans

        if recurBro(0,0): return 1
        return 0

# 6 : Coin Sum Infinite
# You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.

# NOTE:

# Coins in set A will be unique. Expected space complexity of this problem is O(B).
# The answer can overflow. So, return the answer % (106 + 7).


# Problem Constraints
# 1 <= A <= 500
# 1 <= A[i] <= 1000
# 1 <= B <= 50000



# Input Format
# First argument is an integer array A representing the set.
# Second argument is an integer B.



# Output Format
# Return an integer denoting the number of ways.



# Example Input
# Input 1:

#  A = [1, 2, 3]
#  B = 4
# Input 2:

#  A = [10]
#  B = 10


# Example Output
# Output 1:

#  4
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  The 4 possible ways are:
#  {1, 1, 1, 1}
#  {1, 1, 2}
#  {2, 2}
#  {1, 3} 
# Explanation 2:

#  There is only 1 way to make sum 10.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, coins, amount):
        N = len(coins)
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for indx  in range(N):
            for coins_used in range(1,amount+1):
                if coins_used >= coins[indx]:
                    dp[coins_used] += dp[coins_used - coins[indx]]
        return dp[amount] % 1000007


# 7 : 0-1 Knapsack II
# Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

# Also given an integer C which represents knapsack capacity.

# Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

# NOTE: You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).



# Problem Constraints
# 1 <= N <= 500

# 1 <= C, B[i] <= 106

# 1 <= A[i] <= 50



# Input Format
# First argument is an integer array A of size N denoting the values on N items.

# Second argument is an integer array B of size N denoting the weights on N items.

# Third argument is an integer C denoting the knapsack capacity.



# Output Format
# Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.



# Example Input
# Input 1:

#  A = [6, 10, 12]
#  B = [10, 20, 30]
#  C = 50
# Input 2:

#  A = [1, 3, 2, 4]
#  B = [12, 13, 15, 19]
#  C = 10


# Example Output
# Output 1:

#  22
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Taking items with weight 20 and 30 will give us the maximum value i.e 10 + 12 = 22
# Explanation 2:

#  Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.

# this question can be solved only using bottom up approach because for topdown approach we are unable to obtain values for every single cell

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer

   
    def solve(self, A, B, C):  # TC:O(N*maxval) SC:O(maxval)  #this is a bit faster as well
        maxval=sum(A)
        dp=[float('inf') for _ in range(maxval+1)]
        dp[0]=0
       
        for i in range(len(A)):   #A- values B- weights C-knapsack weight
            for j in range(maxval,-1,-1):
                if A[i-1]<=j:
                    dp[j]=min(dp[j-A[i-1]]+B[i-1],dp[j])
                else:
                    dp[j]=dp[j]
        for k in range(len(dp)-1,-1,-1):
            if dp[k]<=C:
                return k

# 8 : Length of Longest Fibonacci Subsequence

# Given a strictly increasing array A of positive integers forming a sequence.

# A sequence X1, X2, X3, ..., XN is fibonacci like if


# N > =3
# Xi + Xi+1 = Xi+2 for all i+2 <= N
# Find and return the length of the longest Fibonacci-like subsequence of A.

# If one does not exist, return 0.

# NOTE: A subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.



# Problem Constraints
# 3 <= length of the array <= 1000

# 1 <= A[i] <= 109



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return the length of the longest Fibonacci-like subsequence of A.
# If one does not exist, return 0.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5, 6, 7, 8]
# Input 2:

#  A = [1, 3, 7, 11, 12, 14, 18]


# Example Output
# Output 1:

#  5
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  The longest subsequence that is fibonacci-like: [1, 2, 3, 5, 8].
# Explanation 2:

#  The longest subsequence that is fibonacci-like: [1, 11, 12], [3, 11, 14] or [7, 11, 18].
#  The length will be 3.


# reference : https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-873-length-of-longest-fibonacci-subsequence/

from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        n = len(arr)
        lookup = {}
        for i in range(n):
            lookup[arr[i]] = i

        longest = defaultdict(lambda: 2)
        ans = 0
        for i in range(n):
            a = arr[i]
            for j in range(i+1,n):
                b = arr[j]
                c = a + b

                if c in lookup:
                    longest[(j,lookup[c])] = longest[(i,j)] + 1

                    ans = max(ans,longest[(j,lookup[c])])


        return ans 

# 9 : 0-1 Knapsack


# Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

# Also given an integer C which represents knapsack capacity.

# Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

# NOTE:

# You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


# Problem Constraints
# 1 <= N <= 103

# 1 <= C <= 103

# 1 <= A[i], B[i] <= 103



# Input Format
# First argument is an integer array A of size N denoting the values on N items.

# Second argument is an integer array B of size N denoting the weights on N items.

# Third argument is an integer C denoting the knapsack capacity.



# Output Format
# Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.



# Example Input
# Input 1:

#  A = [60, 100, 120]
#  B = [10, 20, 30]
#  C = 50
# Input 2:

#  A = [10, 20, 30, 40]
#  B = [12, 13, 15, 19]
#  C = 10


# Example Output
# Output 1:

#  220
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
# Explanation 2:

#  Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.

import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        dp = [[-1 for _ in range(C+1)] for _ in range(len(A))]
        return self.solveHelper(C, A, B, len(A)-1, dp)

    def solveHelper(self, tot, values, weights, i, dp):
        if i == -1 or tot == 0:
            return 0
        if dp[i][tot] != -1:
            return dp[i][tot]
        if weights[i-1] <= tot:
            dp[i][tot] = max(values[i-1] + self.solveHelper(tot - weights[i-1], values, weights, i-1, dp), self.solveHelper(tot, values, weights, i - 1, dp))
        else:
            dp[i][tot] = self.solveHelper(tot, values, weights, i - 1, dp)
        return dp[i][tot]


