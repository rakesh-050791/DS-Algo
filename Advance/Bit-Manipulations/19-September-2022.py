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

# 4 :  Interesting Array
# You have an array A with N elements. We have two types of operation available on this array :
# We can split an element B into two elements, C and D, such that B = C + D.
# We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
# You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0 after several splits and/or merge?



# Problem Constraints
# 1 <= N <= 100000

# 1 <= A[i] <= 106



# Input Format
# The first argument is an integer array A of size N.



# Output Format
# Return "Yes" if it is possible otherwise return "No".



# Example Input
# Input 1:

#  A = [9, 17]
# Input 2:

#  A = [1]


# Example Output
# Output 1:

#  Yes
# Output 2:

#  No


# Example Explanation
# Explanation 1:

#  Following is one possible sequence of operations -  
#  1) Merge i.e 9 XOR 17 = 24  
#  2) Split 24 into two parts each of size 12  
#  3) Merge i.e 12 XOR 12 = 0  
#  As there is only 1 element i.e 0. So it is possible.
# Explanation 2:

#  There is no possible way to make it 0.

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        res=0
        if len(A)==1:
            return 'No'

        for num in A:
            res ^= num

        return 'Yes' if res&1==0 else 'No'


# 5 : Min XOR value
# Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.



# Problem Constraints
# 2 <= length of the array <= 100000
# 0 <= A[i] <= 109



# Input Format
# First and only argument of input contains an integer array A.



# Output Format
# Return a single integer denoting minimum xor value.



# Example Input
# Input 1:

#  A = [0, 2, 5, 7]
# Input 2:

#  A = [0, 4, 7, 9]


# Example Output
# Output 1:

#  2
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  0 xor 2 = 2

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        ans=float('inf')
        n=len(A)
        A.sort()
        for i in range(0,n-1):
            ans=min(ans,A[i]^A[i+1])
        return ans

