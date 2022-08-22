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