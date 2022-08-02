# 1 : N/3 Repeat Number
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




