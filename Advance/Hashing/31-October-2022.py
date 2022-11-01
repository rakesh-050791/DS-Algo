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


# 3 : Permutations of A in B

# You are given two strings, A and B, of size N and M, respectively.

# You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.


# Example Input

# Input 1:

#  A = "abc"
#  B = "abcbacabc"

# Example Output

# Output 1: 5

# Example Explanation

# Explanation 1:

# Permutations of A that are present in B as substring are:
#     1. abc
#     2. cba
#     3. bac
#     4. cab
#     5. abc
#     So ans is 5.

# Approach 1 

class Solution:
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        totalPermutations = 0
        hashMapA = {}
        hashMapB = {}

        for i in A:
            if i in hashMapA:
                hashMapA[i] += 1
            else:
                hashMapA[i] = 1

        # creating 1st window from B
        for j in range(n):
            if B[j] in hashMapB:
                hashMapB[B[j]] += 1
            else:
                hashMapB[B[j]] = 1

        if hashMapA == hashMapB:
            totalPermutations += 1


        # Applying sliding window on hashMapB
        l = 0
        for r in range(n, m):
            hashMapB[B[l]] -= 1

            if hashMapB[B[l]] == 0:
                del hashMapB[B[l]]
            
            if B[r] not in hashMapB:
                hashMapB[B[r]] = 1
            else:
                hashMapB[B[r]] += 1
            
            l += 1
            
            if hashMapA == hashMapB:
                totalPermutations += 1

        return totalPermutations

    
# Approach 2  (Different sliding window technique)

class Solution:
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        totalPermutations = 0
        hashMapA = {}
        hashMapB = {}

        for i in A:
            if i in hashMapA:
                hashMapA[i] += 1
            else:
                hashMapA[i] = 1

        for j in range(n):
            if B[j] in hashMapB:
                hashMapB[B[j]] += 1
            else:
                hashMapB[B[j]] = 1

        if hashMapA == hashMapB:
            totalPermutations += 1

        for i in range(1, m-n+1):
            # remove previous element
            previousElement = B[i-1]
            if previousElement in hashMapB and hashMapB[previousElement] != 0:
                hashMapB[previousElement] -= 1

            if previousElement in hashMapB and hashMapB[previousElement] == 0:
                del hashMapB[previousElement]

            # add next element 
            nextElement = B[i+n-1]
            if nextElement in hashMapB:
                hashMapB[nextElement] += 1
            else:
                hashMapB[nextElement] = 1
            
            if hashMapA == hashMapB:
                totalPermutations += 1

        return totalPermutations