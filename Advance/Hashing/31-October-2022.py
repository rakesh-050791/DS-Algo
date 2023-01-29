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


from collections import Counter

class Solution:
   def minWindow(self, A, B):
        freq = Counter(B)
        req = len(B)

        min_left = float('inf')
        min_len = float('inf')

        l = 0
        for r, c in enumerate(A):
            freq[c] -= 1
            if freq[c] >= 0: 
                req -= 1

            while req == 0: 
                if r - l + 1 < min_len: 
                    min_left = l 
                    min_len = r - l + 1

                freq[A[l]] += 1

                if freq[A[l]] > 0: 
                    req += 1

                l += 1

        return '' if min_left == float('inf') else A[min_left:min_left + min_len]

# 4 : Window String

# Given a string A and a string B, find the window with minimum length in A, which will contain all the characters in B in linear time complexity.
# Note that when the count of a character c in B is x, then the count of c in the minimum window in A should be at least x.

# Note:

# If there is no such window in A that covers all characters in B, return the empty string.
# If there are multiple such windows, return the first occurring minimum window ( with minimum start index and length )


# Problem Constraints
# 1 <= size(A), size(B) <= 106



# Input Format
# The first argument is a string A.
# The second argument is a string B.



# Output Format
# Return a string denoting the minimum window.



# Example Input
# Input 1:

#  A = "ADOBECODEBANC"
#  B = "ABC"
# Input 2:

#  A = "Aa91b"
#  B = "ab"


# Example Output
# Output 1:

#  "BANC"
# Output 2:

#  "a91b"


# Example Explanation
# Explanation 1:

#  "BANC" is a substring of A which contains all characters of B.
# Explanation 2:

#  "a91b" is the substring of A which contains all characters of B.

from collections import Counter

class Solution:
   # @param A : string
   # @param B : string
   # @return a strings
   def minWindow(self, A, B):
        freq = Counter(B)
        
        # idea is to track the required number of 
        # characters and their minimum frequency 
        req = len(B)

        # we have to return the smallest possible window string 
        # and in case of equal length substrings - window string with smaller index 
        min_left = float('inf')
        min_len = float('inf')

        l = 0
        for r, c in enumerate(A):
            # req is initalised to len(B), meaning it takes all the characters
            # and their frequency count 

            # as we traverse A, we reduce the count of each character in 
            # freq. If after processing a character count, we find that the 
            # count of that character is non-negative, that means it is a 
            # character which is present in B and hence we update the req 
            # as we have now found this particular character and thus, require 
            # 1 less character to match B in A  
            freq[c] -= 1
            if freq[c] >= 0: 
                req -= 1

            # when req == 0, it means that we have found the required window string 
            # but, now the task is to fetch the minimum size window sub-string and so,
            # we move the l pointer forward while updating min_left and min_len.  
            while req == 0: 
                if r - l + 1 < min_len: 
                    min_left = l 
                    min_len = r - l + 1

                # Since we were decrementing the freq count when processing characters
                # when the r pointer was moving, now the counts are incremented as the 
                # l pointer moves which is reflected in the min_left and min_right in the
                # next iteration. 
                freq[A[l]] += 1

                # when the right pointer moves, it decrements and so the characters 
                # in B which are found in A move towards 0. Once the right pointer stops
                # then the characters in B are all found in A, and their freq count is 
                # either 0 or negative. So, when the left pointer moves, it starts to 
                # increment freq count and so, if the freq count goes above 0 for a 
                # character, that means it must be a character in B, because these are 
                # the only ones which had positive counts before the for loop ran.
                # So, every other character at max can have a 0 count when the left 
                # pointer increments frequency. So, when the count of a character goes 
                # above 0, it means that we have a lost a character which was in B and 
                # had been found in A, and so now we increment req as we need that character 
                if freq[A[l]] > 0: 
                    req += 1

                l += 1

        # if the while loop is never processed, then we never update min_left and 
        # it implies that the characters in B can't be found in A 
        return '' if min_left == float('inf') else A[min_left:min_left + min_len]


# 5 : Sort Array in given Order

# Given two arrays of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B.
# For the elements not present in B, append them at last in sorted order.

# Return the array A after sorting from the above method.

# NOTE: Elements of B are unique.



# Problem Constraints
# 1 <= length of the array A <= 100000

# 1 <= length of the array B <= 100000

# -10^9 <= A[i] <= 10^9



# Input Format
# The first argument given is the integer array A.

# The second argument given is the integer array B.



# Output Format
# Return the array A after sorting as described.



# Example Input
# Input 1:

# A = [1, 2, 3, 4, 5]
# B = [5, 4, 2]
# Input 2:

# A = [5, 17, 100, 11]
# B = [1, 100]


# Example Output
# Output 1:

# [5, 4, 2, 1, 3]
# Output 2:

# [100, 5, 11, 17]


# Example Explanation
# Explanation 1:

#  Simply sort as described.
# Explanation 2:

#  Simply sort as described.

from collections import OrderedDict
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        # BruteForce 
        A.sort()

        bmap = OrderedDict()
        for i in B:
            if i not in bmap:
                bmap[i] = 1
            else:
                bmap[i] += 1

        amap = OrderedDict()
        for i in A:
            if i not in amap:
                amap[i] = 1
            else:
                amap[i] += 1


        ans = []
        for k in bmap:
            if k in amap:
                while amap[k] > 0:
                    ans.append(k)
                    amap[k] -= 1

        for jk in amap:
            while amap[jk] > 0:
                ans.append(jk)
                amap[jk] -= 1


        return ans 

# 6 : Anagrams

# Given an array A of N strings, return all groups of strings that are anagrams.

# Represent a group by a list of integers representing the index(1-based) in the original list. Look at the sample case for clarification.

# NOTE: Anagram is a word, phrase, or name formed by rearranging the letters, such as 'spar', formed from 'rasp'.



# Problem Constraints
# 1 <= N <= 104

# 1 <= |A[i]| <= 104

# Each string consists only of lowercase characters.

# The sum of the length of all the strings doesn't exceed 107



# Input Format
# The first and only argument is an integer array A.



# Output Format
# Return a two-dimensional array where each row describes a group.

# Note:

# Ordering of the result :
# You should not change the relative ordering of the strings within the group suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.



# Example Input
# Input 1:

#  A = [cat, dog, god, tca]
# Input 2:

#  A = [rat, tar, art]


# Example Output
# Output 1:

#  [ [1, 4],
#    [2, 3] ]
# Output 2:

#  [ [1, 2, 3] ]


# Example Explanation
# Explanation 1:

#  "cat" and "tca" are anagrams which correspond to index 1 and 4 and "dog" and "god" are another set of anagrams which correspond to index 2 and 3.
#  The indices are 1 based ( the first element has index 1 instead of index 0).
# Explanation 2:

#  All three strings are anagrams.

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        n = len(A)
        d = {}
        ans = []
        for i in range(n):
            st = ''.join(sorted(A[i]))
            if st in d:
                a = d[st]
                a.append(i+1)
            else:
                d[st] = [i+1]
        for k,v in d.items():
            ans.append(v)
        return ans



