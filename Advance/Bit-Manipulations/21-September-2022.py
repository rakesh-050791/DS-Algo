# 1 : Given two binary strings, return their sum (also a binary string).
# Example:

# a = "100"

# b = "11"
# Return a + b = "111".


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
