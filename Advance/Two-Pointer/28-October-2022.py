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


# 2 : Pairs with Given Difference

# Given an one-dimensional integer array A of size N and an integer B.

# Count all distinct pairs with difference equal to B.

# Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.

# Example Input

# Input 1:

# A = [1, 5, 3, 4, 2]
# B = 3

# Example Output
# Output 1: 2


# Example Explanation

# Explanation 1:

# There are 2 unique pairs with difference 3, the pairs are {1, 4} and {5, 2} 


# Approach 1 # TC: O(NlogN); SC: O(N^2)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = set()
        n = len(A)
        p1 = 0
        p2 = 1
        A.sort()

        while p2 < n:
            diff = A[p2] - A[p1]
            if diff == B:
                ans.add(tuple([A[p1], A[p2]]))
                p1 += 1
                p2 += 1
            elif diff > B:
                p1 += 1
                if p1 == p2:
                    p2 += 1
            else:
                p2 += 1

        return len(ans)

    
# Approach 2 # TC: O(N); SC: O(N)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq = {}
        p = 0

        # hashing for arrays with unique elements
        if B != 0:
            for a in set(A):
                if a in freq:
                    freq[a] += 1
                if a not in freq:
                    freq[a] = 1
                if a + B in freq:
                    p += 1
                if a - B in freq:
                    p += 1

        # hashing for arrays with duplicates
        else:
            for a in A:
                if a in freq:
                    freq[a] += 1
                else:
                    freq[a] = 1
            for f in freq:
                if freq[f] > 1:
                    p += 1

        return p

# Final Approach 3 # TC: O(NlogN); SC: O(1) 

class Solution:
    def solve(self, A, B):

        n = len(A)
        start = 0 
        end = 1
        pairs = 0
        A.sort()

        while (end < n):
            diff = abs(A[end] - A[start])
            if diff == B:
                pairs += 1
                start += 1
                end += 1

                # handling duplicates
                while end < n and A[end] == A[end - 1]:
                    end += 1
                while start < end and start > 0 and A[start] == A[start - 1]:
                    start += 1

            elif diff < B:
                end += 1
            elif diff > B:
                start += 1
                if start == end:
                    end += 1
        return pairs

