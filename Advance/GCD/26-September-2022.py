# 1 : Delete one

# Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
# Find the maximum value of GCD.

# Input 1:
#  A = [12, 15, 18]

# Output 1:
#  6

#  Explanation 1:
#  If you delete 12, gcd will be 3.
#  If you delete 15, gcd will be 6.
#  If you delete 18, gcd will 3.
#  Maximum vallue of gcd is 6.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        
        # Calculating prefix GCD array 
        prefixGCD = [0]*n
        prefixGCD[0] = A[0]
        result1 = 0

        for i in range(n):
            result1 = self.calculateGCD(result1, A[i])
            prefixGCD[i] = result1

        # Calculating suffix GCD array 
        suffixGCD = [0]*n
        suffixGCD[-1] = A[-1]
        result2 = 0
        for i in range(n-1, -1, -1):
            result2 = self.calculateGCD(result2, A[i])
            suffixGCD[i] = result2
        
        answer = float('-inf')
        for i in range(n):
            if i == 0:
                value = suffixGCD[i + 1]
            elif i == n-1:
                value = prefixGCD[i - 1]
            else:
                value = self.calculateGCD(prefixGCD[i-1], suffixGCD[i+1])

            answer = max(answer, value)
        return answer

    # Calculating GCD
    def calculateGCD(self, a, b):
        a = abs(a)
        b = abs(b)
 
        if b == 0:
            return a 
        return self.calculateGCD(b, a % b)


