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