# 1 : Merge Intervals
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example Input
# Input 1:

# Given intervals [1, 3], [6, 9] insert and merge [2, 5] .

# Example Output
# Output 1: [ [1, 5], [6, 9] ]

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        result = []
        n = len(intervals)

        for i in range(n):
            if intervals[i].end < newInterval.start:
                result.append(intervals[i])
                
            elif newInterval.end < intervals[i].start:
                result.append(newInterval)
                for j in range(i, n):
                    result.append(intervals[j])
                return result
            else:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
            
        result.append(newInterval)

        return result

# 2 : Minimum Swaps
# Given an array of integers A and an integer B, find and return the minimum number of swaps 
# required to bring all the numbers less than or equal to B together.
# Note: It is possible to swap any two elements, not necessarily consecutive.

# Example Input

# Input 1:

#  A = [1, 12, 10, 3, 14, 10, 5]
#  B = 8

#  Example Output

# Output 1: 2

# Explanation 1:

#  A = [1, 12, 10, 3, 14, 10, 5]
#  After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
#  After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
#  Now, all elements less than or equal to 8 are together.

class Solution:
    def solve(self, A, B):
        n = len(A)
        noOfSwaps = 0
        result = float('inf')
        noOfElementsLessthenB = 0 

        for element in A:
            if element <= B:
                noOfElementsLessthenB += 1

        for i in range(noOfElementsLessthenB):
            if A[i] > B:
                noOfSwaps += 1

        result = min(result, noOfSwaps)

        for i in range(noOfElementsLessthenB, n):
            if A[i-noOfElementsLessthenB] <=B and A[i] > B:
                noOfSwaps += 1
            elif A[i-noOfElementsLessthenB] > B and A[i] <=B:
                noOfSwaps -= 1
            result = min(result, noOfSwaps)

        return result



# 3 : Minimum Swaps 2

# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)]. It is allowed to 
# swap any two elements (not necessarily consecutive).
# Find the minimum number of swaps required to sort the array in ascending order.

# Example Input
# Input 1:

# A = [1, 2, 3, 4, 0]

# Example Output
# Output 1: 4

# Example Explanation
# Explanation 1:

#  If you swap (1, 2) -> (2, 3) -> (4, 0) -> (3, 0). You will get a sorted array.
#  You cannot sort it with lesser swaps.

class Solution:
    def solve(self, A):
        n = len(A)
        noOfSwaps = 0
        i = 0
        while i < n:
            num = A[i]
            if num == i:
                i+=1
            else:
                temp = A[i]
                A[i] = A[num]
                A[num] = temp
                noOfSwaps += 1
        return noOfSwaps
        
