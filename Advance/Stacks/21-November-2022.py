# 1 : Largest Rectangle in Histogram

# Given an array of integers A.

# A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.

# Find the area of the largest rectangle formed by the histogram.

# Example Input
# Input 1: A = [2, 1, 5, 6, 2, 3]

# Input 2: A = [2]


# Example Output
# Output 1: 10
# Output 2: 2


# Example Explanation
# Explanation 1: The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
# Explanation 2: Largest rectangle has area 2.

from collections import deque

class Solution:    

    def leftSmallestIndex(self, arr):
        n = len(arr)
        result = [-1] * n
        myStack = deque()

        for i in range(n):
            while myStack and (arr[myStack[-1]] >= arr[i]):
                myStack.pop()

            if myStack:
                result[i] = myStack[-1]
        
            myStack.append(i)
        
        return result
    
    def rightSmallestIndex(self, arr):
        n = len(arr)
        result = [n] * n
        myStack = deque()

        for i in range(n-1, -1, -1):
            while myStack and (arr[myStack[-1]] >= arr[i]):
                myStack.pop()

            if myStack:
                result[i] = myStack[-1]
        
            myStack.append(i)
        
        return result

    def largestRectangleArea(self, A):
        leftIndex = self.leftSmallestIndex(A)
        rightIndex = self.rightSmallestIndex(A)

        area = float('-inf')

        for ind, ele in enumerate(A):
            p1 = leftIndex[ind]
            p2 = rightIndex[ind]
            width = p2 - p1 - 1
            height = ele #height of histogram

            area = max(area,  width * height )

        return area




        