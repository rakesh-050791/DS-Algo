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

# 2 : MAX and MIN (Sum of max of every sub array)

# Given an array of integers A.

# value of a array = max(array) - min(array).

# Calculate and return the sum of values of all possible subarrays of A modulo 109+7.

# Output Format
# Return the sum of values of all possible subarrays of A modulo 109+7.



# Example Input
# Input 1: A = [1]
# Input 2: A = [4, 7, 3, 8]


# Example Output
# Output 1: 0

# Output 2: 26

# Example Explanation
# Explanation 1:

# Only 1 subarray exists. Its value is 0.
# Explanation 2:

# value ( [4] ) = 4 - 4 = 0
# value ( [7] ) = 7 - 7 = 0
# value ( [3] ) = 3 - 3 = 0
# value ( [8] ) = 8 - 8 = 0
# value ( [4, 7] ) = 7 - 4 = 3
# value ( [7, 3] ) = 7 - 3 = 4
# value ( [3, 8] ) = 8 - 3 = 5
# value ( [4, 7, 3] ) = 7 - 3 = 4
# value ( [7, 3, 8] ) = 8 - 3 = 5
# value ( [4, 7, 3, 8] ) = 8 - 3 = 5
# sum of values % 10^9+7 = 26


# Solution approach
# Calculate the next greater element and previous greater element for each element in the array. Each element Ai is the maximum of all subarrays starting at (previous greater element)i + 1 to (next greater element)i - 1.

# Similarly, the next smaller element and previous smaller element can be used for minimum values of subarrays

# Time Complexity:- O(N)


from collections import deque

class Solution:
    def leftSmaller(self, A, n):
        output = [-1] * n
        myStack = deque()

        for i in range(n):
            while (myStack and A[myStack[-1]] >= A[i]):
                myStack.pop()

            if myStack:
                output[i] = myStack[-1]
            
            myStack.append(i)
        
        return output
    

    def leftGreater(self, A, n):
        output = [-1] * n
        myStack = deque()

        for i in range(n):
            while (myStack and A[myStack[-1]] <= A[i]):
                myStack.pop()
            
            if myStack:
                output[i] = myStack[-1]
            
            myStack.append(i)
        
        return output

    
    def rightSmaller(self, A, n):
        output = [n] * n
        myStack = deque()

        for i in range(n-1, -1, -1):
            while (myStack and A[myStack[-1]] >= A[i]):
                myStack.pop()
                
            if myStack:
                output[i] = myStack[-1]
            
            myStack.append(i)
        
        return output

    
    def rightGreater(self, A, n):
        output = [n] * n
        myStack = deque()

        for i in range(n-1, -1, -1):
            while (myStack and A[myStack[-1]] <= A[i]):
                myStack.pop()
            
            if myStack:
                output[i] = myStack[-1]

            myStack.append(i)
        
        return output

    def solve(self, A):
        n = len(A)
        prevSmall = self.leftSmaller(A, n)
        nextSmall = self.rightSmaller(A, n)
        prevGreater = self.leftGreater(A, n)
        nextGreater = self.rightGreater(A, n)

        ans = 0
        maxContribution = 0
        minContribution = 0
        mod = 1000000007

        for i in range(n):
            p1 = prevGreater[i]
            p2 = nextGreater[i]
            maxContribution = (i-p1)*(p2-i)*A[i]

            p1 = prevSmall[i] 
            p2 = nextSmall[i]
            minContribution = (i-p1)*(p2-i)*A[i]

            ans += (maxContribution - minContribution)
        return ans%mod 


        