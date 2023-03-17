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


# 4 : tolower()
# You are given a function to_lower() which takes a character array A as an argument.

# Convert each character of A into lowercase characters if it exists. If the lowercase of a character does not exist, it remains unmodified.
# The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.

# Return the lowercase version of the given character array.
class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        for i in range(len(A)):
            if ord(A[i]) >= 65 and ord(A[i]) <= 90 :
                A[i]  = chr(ord(A[i]) + 32)
        return A

# 5 : toupper()
# You are given a function to_upper() consisting of a character array A.

# Convert each charater of A into Uppercase character if it exists. If the Uppercase of a character does not exist, it remains unmodified.
# The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.

# Return the uppercase version of the given character array.


class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        for i in range(len(A)):
            if ord(A[i]) >= 97 and ord(A[i]) <= 122:
                A[i] = chr(ord(A[i]) - 32)
        return A


# 6 : Isalnum()
# You are given a function isalpha() consisting of a character array A.

# Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.

# Output Format
# Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.



# Example Input
# Input 1:

# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']

# Example Output
# Output 1: 1

# Explanation 1:

# All the characters are alphanumeric.

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        nonAlphanumericCount = 0
        for i in range(len(A)):
            if (ord(A[i]) >= 65 and ord(A[i]) <= 90) or (ord(A[i]) >= 97 and ord(A[i]) <= 122) or (ord(A[i]) >= 48 and ord(A[i]) <= 57):
                pass
            else:
                nonAlphanumericCount += 1
        
        return 0 if nonAlphanumericCount > 0 else 1


# 7 : Isalpha()

# You are given a function isalpha() consisting of a character array A.

# Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.

# Output Format

# Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.

# Example Input

# Input 1:

# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']

# Example Output

# Output 1: 1

# Explanation 1:

# All the characters are alphabets.

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        nonAlphanumericCount = 0
        for i in range(len(A)):
            if (ord(A[i]) >= 65 and ord(A[i]) <= 90) or (ord(A[i]) >= 97 and ord(A[i]) <= 122):
                pass
            else:
                nonAlphanumericCount += 1
        
        return 0 if nonAlphanumericCount > 0 else 1


# 8 : Amazing Subarrays

# You are given a string S, and you have to find all the amazing substrings of S.

# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

# Input

# Only argument given is string S.
# Output

# Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
# Constraints

# 1 <= length(S) <= 1e6
# S can have special characters
# Example

# Input
#     ABEC

# Output
#     6

# Explanation
#     Amazing substrings of given string are :
#     1. A
#     2. AB
#     3. ABE
#     4. ABEC
#     5. E
#     6. EC
#     here number of substrings are 6 and 6 % 10003 = 6.

    class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
            N = len(A)
            no_elements = 0
            count = 0
            vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
            for i in range(N-1, -1, -1):
                no_elements += 1
                if A[i] in vowels:
                    count += no_elements
            return count%10003

# 9 : Count Occurrences

# Find the number of occurrences of bob in string A consisting of lowercase English alphabets.



# Problem Constraints
# 1 <= |A| <= 1000


# Input Format
# The first and only argument contains the string A, consisting of lowercase English alphabets.


# Output Format
# Return an integer containing the answer.


# Example Input
# Input 1:

#   "abobc"
# Input 2:

#   "bobob"


# Example Output
# Output 1:

#   1
# Output 2:

#   2


# Example Explanation
# Explanation 1:

#   The only occurrence is at second position.
# Explanation 2:

#   Bob occures at first and third position.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n=len(A)
        ans="bob"
        coun=0
        for i in range(n-2):
            if A[i:i+3]==ans:
                coun+=1
        return coun
