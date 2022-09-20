# 1 : A, B and Modulo
# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A-B)


# 2 : Concatenate Three Numbers
# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.

# Return the minimum result obtained.
class Solution:
    def solve(self, A, B, C):
        minimumElement = min(A, B, C)
        maximumElement = max(A, B, C)
        middleElement = A + B + C - maximumElement - minimumElement
        
        return (minimumElement*10000 + middleElement*100 + maximumElement)


# 3 : Find if two rectangles overlap

# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
# For the first rectangle, its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left corner is (E, F), and the top right corner is (G, H).

# Find and return whether the two rectangles overlap or not.

# Example Input
# Input 1:

# A = 0   B = 0
# C = 4   D = 4
# E = 2   F = 2
# G = 6   H = 6

# Output 1:
# 1

# Explanation 1:
# Rectangle with bottom left (2, 2) and top right (4, 4) is overlapping.

# Solution Approach 
# we can formulate the required conditions.

# First, we can see if a foot of one rectangle is >= top of another rectangle, then an answer is not possible.

# You can make a similar argument about the y-axis.

class Solution:
    def solve(self, A, B, C, D, E, F, G, H):
        if A >= G or E >= C:
            return 0
        if D <= F or H <= B:
            return 0
        return 1

# 4 : Leap year? - III
# Given an integer A representing a year, Return 1 if it is a leap year else, return 0.

# A year is a leap year if the following conditions are satisfied:

# The year is multiple of 400.
# Else the year is multiple of 4 and not multiple of 100.

class Solution:
    def solve(self, A):
        n = A

        if n % 400 == 0:
            return 1

        if (n % 4 == 0 and  n % 100 != 0):
            return 1
    
        return 0


# 5 : Least Common Multiple
# Write a program to input an integer T and then for each test case input two integers A and B in two different lines and then print T lines containing Least Common Multiple (LCM) of two given 2 numbers A and B.

# LCM of two integers is the smallest positive integer divisible by both.

# Input Format
# In first-line input T which means number of test cases.

# Next 2T lines contains input A and B for each testcase.
# First line of each testcase contain an integer A and second line of the testcase contains input B.

def main():
    T = int(input())

    while T:
        T -= 1
        A = int(input())
        B = int(input())

        greaterNo = max(A,B)

        lcm = greaterNo
        while (True):
            if greaterNo % A == 0 and greaterNo % B == 0:
                lcm = greaterNo
                break
            greaterNo += 1
        print(lcm)

if __name__ == '__main__':
    main()


# 5 : Repeat and Missing Number Array
# There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.
# This is one of those problems.
# Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

# Food for thought :

# Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
# For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
# Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
# Obviously approach 1 is more susceptible to overflows.

# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4

## SOlution Explanation : https://www.youtube.com/watch?v=ExXfLZEuV5Y 

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        N = len(A)

        #IF A = [1, 2, 2, 3,1]
        arraySum = sum(A) # 3 + 1 + 2 + 5 + 3 = 14
        
        repeatedNumber = arraySum - self.ASetSum(A)
        missingNumber = self.sumOfnNaturalNumbers(N) - self.ASetSum(A)

        return [repeatedNumber, missingNumber]

    def ASetSum(self, A):
        #IF  A = [1, 2, 2, 3,1]
        #create set from an aaray & get sum of unique elements (SET) of an array
        setSum = sum(set(A)) # 3 + 1 + 2 + 5 = 11
        return setSum

    def sumOfnNaturalNumbers(self, N):
        #IF  N = 5 
        # Formula to calculate sum of n natural numbers = (N (N + 1)) / 2
        nNaturalNoSum = int((N * (N + 1)) / 2) # 1 + 2 + 3 + 4 + 5 = 15
        return nNaturalNoSum

