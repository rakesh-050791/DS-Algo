# 1 : Given a number A, we need to find the sum of its digits using recursion.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return digitsSum(A)

def digitsSum(A):

    if A == 0:
        return 0

    lastDigit = A % 10
    remainingDigits = A // 10

    return (lastDigit + digitsSum(remainingDigits))


# 2 : Implement Power Function

# Implement pow(A, B) % C.
# In other words, given A, B and C, Find (AB % C).

# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        return calculateExponent(A,B,C)

def calculateExponent(base,power,mod):
    if power == 0:
        return 1 % mod

    if power == 1:
        return base % mod

    exponent = (calculateExponent(base, power//2, mod)) % mod

    if power % 2 == 0:
        return (exponent * exponent) % mod
    else:
        return ((exponent * exponent) % mod * base ) % mod


# 3 : Is magic?

# Given a number A, check if it is a magic number or not.
# A number is said to be a magic number if the sum of its digits is calculated till a single digit 
# recursively by adding the sum of the digits after every addition.
# If the single digit comes out to be 1, then the number is a magic number.
# Return an 1 if the given number is magic else return 0.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        result = digitSum(A)

        if result > 9:
            return self.solve(result)

        return 1 if result == 1 else 0

def digitSum(x):
    if x == 0:
        return 0

    lastDigit = x % 10
    remainingDigits = x // 10

    return lastDigit + digitSum(remainingDigits)


# 4 : Kth Symbol / Identify Kth Grammer
# On the first row, we write a 0. Now in every subsequent row,
# we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).
class Solution:
    def solve(self, A, B):
        n = A
        k = B
        return findKSymbol(n, k-1) #Passing k - 1 because question stated that indexing should start from 1

def findKSymbol(n, k):
    if k == 0:
        return 0

    parentData = findKSymbol(n-1, k // 2)

    if (k % 2 == 0):
        return parentData
    else:
        return (1 - parentData) # 1's complement or inverse of 1 or 0

# 5 : Gray Code
# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

# A gray code sequence must begin with 0.

# Example Input
# Input 1:

# A = 2

# Example Output
# output 1:

# [0, 1, 3, 2]

## Video Hint : https://www.youtube.com/watch?v=KOD2BFauQbA
## 

## Below solution is using recursion for returning decimal numbers, as asked in question
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        result = self.getGrayCode(A)
        ## result contains binary numbers, in next line we are returning and 
        #converting them to decimal numbers
        return [int(element, 2) for element in result]

    def getGrayCode(self, A):
        # base case
        if A <= 0:
            return ['0']
        
        if A == 1:
            return ['0', '1']

        # recursive case
        recAns = self.getGrayCode(A-1)

        mainAns = []

        # Append 0 to the first half
        for i in range(len(recAns)):
            s = recAns[i]
            mainAns.append('0' + s)
        
        # Append 1 to the second half
        for i in range(len(recAns) - 1, -1, -1):
            s = recAns[i]
            mainAns.append('1' + s)
        
        return mainAns


## Below solution is using recursion 
class Solution:
    def grayCode(self, A):
        ans = []
        for i in range(2 ** A):
            ans.append((i>>1) ^ i)
        return ans
