# 1: Longest Palindromic Substring
# Given a string A of size N, find and return the longest palindromic substring in A.

# Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

# Incase of conflict, return the substring which occurs first ( with the least starting index).

class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		n = len(A)

		result = ''

		def palindromeLength(start, end):
			while(start >= 0 and end < n and A[start] == A[end]):

				start -= 1
				end += 1
			return(A[start+1:end])

		for i in range(n):
			start , end = i, i

			palindrome_length = palindromeLength(start, end)
			if len(palindrome_length) > len(result) : result = palindrome_length

			start, end = i , i+1

			palindrome_length = palindromeLength(start, end)
			if len(palindrome_length) > len(result) : result = palindrome_length
		
		return result

# 2 : Reverse the String
# You are given a string A of size N.

# Return the string A after reversing the string word by word.

# NOTE:

# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        A = A.split(" ")
        if A[-1] == '':
            A.pop()
        if A[0] == '':
            A.pop(0)
        start = 0
        end = len(A) - 1
        while start <= end:
            temp = A[start]
            A[start] = A[end]
            A[end] = temp

            start += 1
            end -= 1
        return(" ".join(A))


# 3 : Simple Reverse
# Given a string A, you are asked to reverse the string and return the reversed string.
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        result = A[n::-1]
        return result



