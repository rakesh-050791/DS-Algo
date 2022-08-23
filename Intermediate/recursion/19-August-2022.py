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


# 3 : Find Fibonacci - II
# The Fibonacci numbers are the numbers in the following integer sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

# Fn = Fn-1 + Fn-2

# Given a number A, find and return the Ath Fibonacci Number.

# Given that F0 = 0 and F1 = 1.

class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):

        return fibSeries(A)
    

def fibSeries(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibSeries(n - 1) + fibSeries(n - 2)

# 4 : Print reverse string

# Write a recursive function that, given a string S, prints the characters of S in reverse order.

def main(s):
    i, j = 0, len(s) - 1
    ar = list(s)
    print(reverseString(ar, i, j))

def reverseString(ar, i, j):
    if i >= j:
        return "".join(ar)

    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp
    return reverseString(ar, i+1, j-1)

if __name__ == '__main__':
    s = input()
    main(s)

    
