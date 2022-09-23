# 1 : Single Number

# Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

# NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Input 1:

#  A = [1, 2, 2, 3, 1]

# Output 1:

#  3

 class Solution:
    def singleNumber(self, A):
        result = 0

        for i in A:
            result = result ^ i
        
        return result


# 2 : Number of 1 Bits
# Write a function that takes an integer and returns the number of 1 bits it has.

# Example Input
# Input1:
# 11

# Example Output
# Output1:
# 3

# Explaination1:
# 11 is represented as 1011 in binary.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        totalOneBits = 0
        for i in range(32):
           if ( (A >> i) & 1) == True:
               totalOneBits += 1
        
        return totalOneBits


# 3 : Single Number II

# Problem Description
# Given an array of integers, every element appears thrice except for one, which occurs once.

# Find that element that does not appear thrice.

# NOTE: Your algorithm should have a linear runtime complexity.

# Could you implement it without using extra memory?

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0

        for i in range(32):
            ci = 0 # For ith bit calculate number of ar[] with ith bit set ?
            for j in range(len(A)):
                if self.checkBit(A[j], i) == True:
                    ci += 1

            if (ci % 3 != 0): # Checking if for unique element ith bit is set ?
                result += (1 << i) # OR 2 raise to power i
        return result


    ## Below is the method that will tell if bit is 
    ## set or unset at particular position or any binary number
    
    def checkBit(self, element, position):
        
        return (element >> position) & 1 
