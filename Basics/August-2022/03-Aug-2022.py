# 1: Arithmetic Progression?
# Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, 
# otherwise return 0.
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sortedA = sorted(A)

        if len(A) <= 1:
            return 0

        diff = sortedA[1] - sortedA[0]

        for i in range(1, len(A)-1):
            if ((sortedA[i+1] - sortedA[i]) == diff):
                pass
            else:
                return 0
        return 1






