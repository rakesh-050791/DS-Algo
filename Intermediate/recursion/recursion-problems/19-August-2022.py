# 1 : Find Factorial!

# Write a program to find the factorial of the given number A.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return factorial(A)

def factorial(n):
    if n == 0:
        return 1

    return factorial(n-1) * n
    
    
# obj = Solution()
# result = obj.solve(3)
# print(result)

