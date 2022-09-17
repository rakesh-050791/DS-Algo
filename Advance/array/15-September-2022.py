# 1 : Merge Intervals
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example Input
# Input 1:

# Given intervals [1, 3], [6, 9] insert and merge [2, 5] .

# Example Output
# Output 1:

#  [ [1, 5], [6, 9] ]

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

# 2 : Minimum Swaps 2

# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)]. It is allowed to 
# swap any two elements (not necessarily consecutive).
# Find the minimum number of swaps required to sort the array in ascending order.

# Example Input
# Input 1:

# A = [1, 2, 3, 4, 0]

# Example Output
# Output 1:

# 4

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

