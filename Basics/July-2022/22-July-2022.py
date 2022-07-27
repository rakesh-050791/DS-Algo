					# Bit Manipulations - 1


# 1 : Find the integer that occurs once

# Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

# NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0 

        for i in A:
            result = result ^ i 
        return result


# 2 : Add Binary Strings

# Given two binary strings, return their sum (also a binary string).

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
        carry = 0
		result = ''
		i = len(A) - 1
		j = len(B) - 1

		while(i>=0 and j>=0):
			addAll = int(A[i]) + int(B[j]) + carry
			result = result + str(addAll % 2)
			carry = addAll // 2 
			i -= 1
			j -= 1
		
		while(i>=0):
			addAll = carry + int(A[i])
			result = result + str(addAll % 2)
			carry = addAll // 2 
			i -= 1
		
		while(j>=0):
			addAll = carry + int(B[j])
			result = result + str(addAll % 2)
			carry = addAll // 2 
			j -= 1
		
		while(carry > 0):
			result = result + str(carry % 10)
			carry = carry // 10
		
		return result[::-1]






		