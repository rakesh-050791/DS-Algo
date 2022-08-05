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
