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
        

# 4 : First Missing Integer
# Given an unsorted integer array, A of size N. Find the first missing positive integer.

# Note: Your algorithm should run in O(n) time and use constant space.

# Input 1:

# [1, 2, 0]

# Output 1:

# 3

# Explanation 1:

# A = [1, 2, 0]
# First positive integer missing from the array is 3.
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)
        i = 0

        while i < N:
            if A[i] > 0 and A[i] < N +1:
                correctindx = A[i] - 1
                if A[correctindx] != A[i]:
                    temp = A[i]
                    A[i] = A[correctindx]
                    A[correctindx] = temp
                else:
                    i+= 1

            else:
                i +=1
               
        for i in range(N):
            if A[i]-1 != i:
                return(i+1)
           
           
        return N+1


# 5 : Row with maximum number of ones

# Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.

# NOTE:

# If two rows have the maximum number of 1 then return the row which has a lower index.
# Rows are numbered from top to bottom and columns are numbered from left to right.
# Assume 0-based indexing.
# Assume each row to be sorted by values.
# Expected time complexity is O(rows).

# Input 1:

#  A = [   [0, 1, 1]
#          [0, 0, 1]
#          [0, 1, 1]   ]


# Output 1:

#  0

#  Explanation 1:

#  Row 0 has maximum number of 1s.

## Youtube explanation : https://www.youtube.com/watch?v=1iSJhfje97I

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        max1, row = 0, None        
        rows,col = len(A),len(A[0])-1
        for i in range(rows):
            while A[i][col] == 1 and col >= 0:
                count += 1
                if count > max1:
                    max1 = count
                    row = i
                col -= 1
        return row


# 6 : Maximum Absolute Difference

# You are given an array of N integers, A1, A2, .... AN.

# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, 
# where |x| denotes absolute value of x.

# Input 1: A = [1, 3, -1]

# Output 1: 5

# Explanation 1:

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

# Video Explanation : https://www.youtube.com/watch?v=tN8wEDNZKF4 

class Solution:
    def maxArr(self, A):
        # We have to find |A[i] - A[j]| + |i - j|
        # for mod we can get four possiblities (+, +) , (+ , -), (- , +), (-, -)

        # So we can write the above as
        # (A[i] - A[j]) + (i - j) => (A[i] + i) - (A[j] + j)
        # (A[i] - A[j]) - (i - j) => (A[i] - i) - (A[j] - j)
        # -(A[i] - A[j]) + (i - j) => -(A[i] - i) + (A[j] - j)
        # -(A[i] - A[j]) - (i - j) => -(A[i] + i) + (A[j] + j)

        # So from the above we can see that we have to find only four pair
        # A = A[i] + i = maxForI
        # B = A[i] - i = minForI
        # C = A[j] + j = maxForJ
        # D = A[j] - j = minForJ

        maxForI=A[0]
        maxForJ=A[0]
        minForI=A[0]
        minForJ=A[0]
        for i in range(len(A)):
            maxForI=max(maxForI,A[i]+i)
            maxForJ=max(maxForJ,A[i]-i)
            minForI=min(minForI,A[i]+i)
            minForJ=min(minForJ,A[i]-i)
        return max(maxForI-minForI, maxForJ-minForJ)


# 7 : Max Chunks To Make Sorted

# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], 
# if we split the array into some number of "chunks" (partitions), and individually sort each chunk. 
# After concatenating them in order of splitting, the result equals the sorted array.
# What is the most number of chunks we could have made?

# Input 1:
# A = [1, 2, 3, 4, 0]


# Example Output
# Output 1: 1

# Explanation 1:

#  A = [1, 2, 3, 4, 0]
#  To get the 0 in the first index, we have to take all elements in a single chunk.


class Solution:
    def solve(self, A):
        # since the input goes from 1 to n-1 we can keep track of the current max , 
        # we check if the current max is equal to current index that will suggest that 
        # current window has all the required element.

        maxElement = float('-inf')
        chunks = 0

        for i in range(len(A)):
            if A[i] > maxElement:
                maxElement = A[i]
            
            if maxElement == i:
                chunks += 1
        
        return chunks