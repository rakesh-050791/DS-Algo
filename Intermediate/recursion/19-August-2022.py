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


# 2 : Check Palindrome

# Write a recursive function that checks whether string A is a palindrome or Not.
# Return 1 if the string A is a palindrome, else return 0.

# Note: A palindrome is a string that's the same when read forward and backward.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = A
        i , j = 0, len(n)-1
        return isPalindrome(A, i, j)

def isPalindrome(s, i, j):

    if i >= j:
        return 1

    if s[i] == s[j]:
        i += 1
        j -= 1
        return isPalindrome(s, i, j)
    else:
        return 0

# obj = Solution()
# result = obj.solve('madam')
# print(result)
