# 1 : Majority Element
# Given an array of size N, find the majority element. 
# The majority element is the element that appears more than floor(n/2) times.
# You may assume that the array is non-empty and the majority element always exists in the array.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):

        targetElement = A[0]
        targetElementFrequency = 1

        for i in range(1, len(A)):
            if targetElementFrequency == 0:
                targetElement = A[i]
                targetElementFrequency += 1
            elif A[i] == targetElement:
                targetElementFrequency += 1
            else:
                targetElementFrequency -= 1
        return targetElement


# 2 : N/3 Repeat Number
# You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
# If so, return the integer. If not, return -1.

# If there are multiple solutions, return any one.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)

        if n == 1:
            return A[0]

        targetIntA = A[0]
        targetIntB = A[1]
        IntAFreq = 0
        IntBFreq = 0

        for i in range(n):
            if A[i] == targetIntA:
                IntAFreq += 1
            elif A[i] == targetIntB:
                IntBFreq += 1
               
            else :
                if IntAFreq == 0:
                   targetIntA = A[i]
                   IntAFreq += 1
                elif IntBFreq == 0:
                    targetIntB = A[i]
                    IntBFreq += 1
                else:
                    IntAFreq -= 1
                    IntBFreq -= 1

        N3 = n // 3
        actualAFrequency = 0
        actualBFrequency = 0 

        for element in A:
            if element == targetIntA:
                actualAFrequency += 1
            elif element == targetIntB:
                actualBFrequency += 1
        
        if actualAFrequency > N3:
            return targetIntA
        elif actualBFrequency > N3:
            return targetIntB
        else:
            return -1


# 3 : Find nth Magic Number
# Given an integer A, find and return the Ath magic number.

# A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.

# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        result = 0
        currentBit = 1

        while (A > 0):
            currentBit *= 5
            if (A & 1 == 1):
                result += currentBit
            # A //= 2
            A = A >> 1
        return result


