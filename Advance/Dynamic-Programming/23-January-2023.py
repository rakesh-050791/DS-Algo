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
