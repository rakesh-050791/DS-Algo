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


# 2 : 

