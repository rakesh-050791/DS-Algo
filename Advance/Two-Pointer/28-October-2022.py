# 1 : Count of pairs with the given sum

# Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

# Input 1:
#     A = [1, 2, 3, 4, 5]
#     B = 5

# Output 1: 2

class Solution:
    def solve(self, A, B):
        n = len(A)
        pairs = 0
        i = 0
        j = n-1

        while (i < j):
            if A[i] + A[j] == B: # we got a valid pair,increase pair count and move left
                pairs += 1
                j -= 1
            elif A[i] + A[j] > B: # move to left side
               j -= 1
            elif A[i] + A[j] < B: # move to right side
                i += 1
        return pairs