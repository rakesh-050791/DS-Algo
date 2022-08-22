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

def calculateExponent(A,B,C):
    if B == 0:
        return 1 % C

    if B == 1:
        return A % C

    exponent = (calculateExponent(A, B//2, C)) % C

    if B % 2 == 0:
        return (exponent * exponent) % C
    else:
        return ((exponent * exponent) % C * A ) % C

