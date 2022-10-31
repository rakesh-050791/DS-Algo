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


# 2 : Longest Consecutive Sequence

# Given an unsorted integer array A of size N.

# Find the length of the longest set of consecutive elements from array A.


# Example Input

# Input 1:

# A = [100, 4, 200, 1, 3, 2]

# Example Output

# Output 1: 4
 
# Example Explanation

# Explanation 1:

# The set of consecutive elements will be [1, 2, 3, 4].


# Approach 1

class Solution:

    # check x-1 in hashSet , if not then start if that element and check for x+1 elements maintain count and return max(count)
    def longestConsecutive(self, A):

        hashSet = set(A) #creating set out of a given array
        longestSetLength = 0

        for x in hashSet:
            previousElement = x - 1

            if previousElement not in hashSet:
                length = 0
                while x in hashSet:
                    length += 1
                    x += 1
                longestSetLength = max(longestSetLength, length)

        return longestSetLength
    

# Approach 2

class Solution:

    def longestConsecutive(self, A):

        hashSet = set(A) #creating set out of a given array
        longestSetLength = 0

        for x in hashSet:
            previousElement = x - 1

            if previousElement in hashSet:
                continue
            else:
                length = 0
                while x in hashSet:
                    x += 1
                    length += 1
                longestSetLength = max(longestSetLength, length)

        return longestSetLength
