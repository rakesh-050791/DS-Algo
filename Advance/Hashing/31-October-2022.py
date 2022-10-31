# 1 : Longest Substring Without Repeat

# Given a string A, find the length of the longest substring without repeating characters.

# Note: Users are expected to solve in O(N) time complexity.


# Example Input

# Input 1: A = "abcabcbb"
 

# Example Output 

# Output 1: 3

# Example Explanation

# Explanation 1:

# Substring "abc" is the longest substring without repeating characters in string A.
 

class Solution:
	def lengthOfLongestSubstring(self, A):
        n = len(A)
        i = j = 0

        longestSubString = 0
        hs = set()

        while (j < n):
            if not A[j] in hs:
                hs.add(A[j])
                longestSubString = max(longestSubString, len(hs))
                j += 1
            else:
                hs.remove(A[i])
                i += 1

        return longestSubString