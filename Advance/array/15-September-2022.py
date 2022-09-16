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