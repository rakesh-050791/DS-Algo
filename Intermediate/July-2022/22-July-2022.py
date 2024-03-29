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


# 3 : Calculate no of 1 bits
# Write a function that takes an integer and returns the number of 1 bits it has.
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while(A>0):
            A, remainder = divmod(A, 2)

            if remainder > 0:
                count += 1
        return count


# 4 : Interesting Array 
# You have an array A with N elements. We have two types of operation available on this array :
# We can split an element B into two elements, C and D, such that B = C + D.
# We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
# You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0 after several splits and/or merge?

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        count = 0 

        for i in range(len(A)):
            if A[i] % 2 != 0:
                count += 1
        

        return 'Yes' if count % 2 == 0 else 'No'      


# 5 : Reverse Bits

# Reverse the bits of an 32 bit unsigned integer A.

# Explanation (https://www.youtube.com/watch?v=LJiMk8lPJNc )

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        n = A 
        result = 0

        for i in range(32): # Because question says 32 bits for looping 32 times
            
            lsb = n & 1 # STEP 1 -> Check last bit of given integer (is it 1 or 0), to do so make and operation with n

            reverseLsb = lsb << (31 - i) # STEP 2 -> reverse the LSB bit

            result = result | reverseLsb # STEP 3 -> get OR of reverseLsb with 0 (because result contains all 0 bits)  

            n = n >> 1 # STEP 4 -> right shift given input by 1, to perform the STEP 1
        
        return result

        