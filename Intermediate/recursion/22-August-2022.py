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

