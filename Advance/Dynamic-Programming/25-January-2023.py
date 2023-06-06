# 1 : Longest Common Subsequence

# Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.

# You need to return the length of such longest common subsequence.



# Problem Constraints
# 1 <= Length of A, B <= 1005



# Input Format
# First argument is a string A.
# Second argument is a string B.



# Output Format
# Return an integer denoting the length of the longest common subsequence.



# Example Input
# Input 1:

#  A = "abbcdgf"
#  B = "bbadcgf"
# Input 2:

#  A = "aaaaaa"
#  B = "ababab"


# Example Output
# Output 1:

#  5
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  The longest common subsequence is "bbcgf", which has a length of 5.
# Explanation 2:

#  The longest common subsequence is "aaa", which has a length of 3.

# Top Down approach

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def helper(self, dp, i, A, j, B):
        if i < 0 or j < 0: return 0

        if dp[i][j] != -1: return dp[i][j]

        if A[i] == B[j]:
            dp[i][j] = 1 + self.helper(dp, i - 1, A, j - 1, B)

        else:
            dp[i][j] = max(self.helper(dp, i, A, j - 1, B), self.helper(dp, i - 1, A, j, B))

        return dp[i][j]

    def solve(self, A, B):
        n = len(A)
        m = len(B)

        dp = [[-1] * m for _ in range(n)]

        self.helper(dp, n - 1, A, m - 1, B)
        return dp[n - 1][m - 1]

        # TC: O(MN); SC: O(MN)


# Bottom Up approach

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

        # TC: O(MN); SC: O(MN)


# Bottom Up - Recursion

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def helper(self, dp, i, A, j, B):
        if i == len(A) or j == len(B): return 0

        if dp[i][j] != -1: return dp[i][j]

        if A[i] == B[j]:
            dp[i][j] = 1 + self.helper(dp, i + 1, A, j + 1, B)

        else:
            dp[i][j] = max(self.helper(dp, i, A, j + 1, B), self.helper(dp, i + 1, A, j, B))

        return dp[i][j]

    def solve(self, A, B):
        n = len(A)
        m = len(B)

        dp = [[-1] * m for _ in range(n)]

        self.helper(dp, 0, A, 0, B)
        return dp[0][0]

        # TC: O(MN); SC: O(MN)


# Bottom Up - Optimised

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        t = min(n, m)

        arr1 = [0] * (t + 1)
        arr2 = [0] * (t + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    arr2[j] = 1 + arr1[j - 1]
                else:
                    arr2[j] = max(arr1[j], arr2[j - 1])

            arr1, arr2 = arr2, arr1

        return arr1[m]

        # TC: O(NM); SC: O(min(N, M))


# 2 : Edit distance

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
        n=len(A)
        m=len(B)

        dp=[[-1 for j in range(m+1)] for i in range(n+1)]
       
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dp[i][j] = j
                    continue
                elif j == 0:
                    dp[i][j] = i
                    continue
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
       
        return dp[n][m]


# 3 : Repeating Subsequence

# Given a string A, find if there is any subsequence that repeats itself.

# A subsequence of a string is defined as a sequence of characters generated by deleting some characters in the string without changing the order of the remaining characters.

# NOTE:
# 1. Subsequence length should be greater than or equal to 2.
# 2. The repeating subsequence should be disjoint that is in both the sequence no character in the same order and position should be taken from the same index of the original string.



# Problem Constraints
# 1 <= length(A) <= 100



# Input Format
# The first and the only argument of input contains a string A.



# Output Format
# Return an integer, 1 if there is any subsequence which repeat itself else return 0.



# Example Input
# Input 1:

#  A = "abab"
# Input 2:

#  A = "abba"


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  "ab" is repeated.
# Explanation 2:

#  There is no repeating subsequence.

class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        n = m = len(A)
        dp = [[-1] * m for _ in range(n)]
        
        result = self.lrs(A, 0, 0, dp)
        
        return 1 if result >= 2 else 0
    
    def lrs(self, s1, i, j, dp):
        # return if we have reached the
        #end of either string
        if i >= len(s1) or j >= len(s1):
            return 0
    
        if dp[i][j] != -1:
            return dp[i][j]
        
        # while dp[i][j] is not computed earlier
        if dp[i][j] == -1:
        
            # if characters at index m and n matches
            # and index is different
            # Index should not match
            if s1[i] == s1[j] and i != j:
                dp[i][j] = 1 + self.lrs(s1, i+1, j+1, dp)
            
            # else if characters at index m and n don't match
            else: 
                dp[i][j] = max(self.lrs(s1, i, j+1, dp),
                                    self.lrs(s1, i+1, j, dp))


        # return answer
        return dp[i][j]
