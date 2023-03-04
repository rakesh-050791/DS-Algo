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


# 3 : Nearest Smaller Element
# Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

# More formally,

# G[i] for an element A[i] = an element A[j] such that

# j is maximum possible AND

# j < i AND

# A[j] < A[i]

# Elements for which no smaller element exist, consider the next smaller element as -1.


# Input Format
# The only argument given is integer array A.

# Output Format
# Return the integar array G such that G[i] contains the nearest smaller number than A[i]. If no such element occurs G[i] should be -1.

# Example Input
# Input 1: A = [4, 5, 2, 10, 8]
# Input 2: A = [3, 2, 1]


# Example Output
# Output 1: [-1, 4, -1, 2, 2]
# Output 2: [-1, -1, -1]


# Example Explanation
# Explanation 1:

# index 1: No element less than 4 in left of 4, G[1] = -1
# index 2: A[1] is only element less than A[2], G[2] = A[1]
# index 3: No element less than 2 in left of 2, G[3] = -1
# index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
# index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
# Explanation 2:

# index 1: No element less than 3 in left of 3, G[1] = -1
# index 2: No element less than 2 in left of 2, G[2] = -1
# index 3: No element less than 1 in left of 1, G[3] = -1

# Solution Approach 

# The naive solution would look something like this:

#   for i = 0 to size(A):
#     G[i] = -1
#     for j = i - 1 to 0:
#         if A[j] < A[i]:
#             G[i] = j
#             break
# Now look at A[i-1]. All elements with index smaller than i - 1 and greater than A[i-1] are useless to us because they would never qualify for G[i], G[i+1], ...

# We know that we only need previous numbers in descending order using the above fact.

# The pseudocode would look something like this:

# 1) Create a new empty stack st

# 2) Iterate over array `A`,
#    where `i` goes from `0` to `size(A) - 1`.
#     a) We are looking for value just smaller than `A[i]`. So keep popping from `st` till elements in `st.top() >= A[i]` or st becomes empty.
#     b) If `st` is non-empty, then the top element is our previous element. Else the previous element does not exist. 
#     c) push `A[i]` onto st
    
from collections import deque

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        if n == 1: return [-1]

        output = [-1] * n
        myStack = deque()

        for indx in range(n):
            while (myStack and myStack[-1] >= A[indx]):
                myStack.pop()

            if myStack:
                output[indx] = myStack[-1]
            
            myStack.append(A[indx])
        
        return output


# 4 : Next Greater
# Given an array A, find the next greater element G[i] for every element A[i] in the array.
# The next greater element for an element A[i] is the first greater element on the right side of A[i] in the array, A.

# More formally:

# G[i] for an element A[i] = an element A[j] such that 
#     j is minimum possible AND 
#     j > i AND
#     A[j] > A[i]
# Elements for which no greater element exists, consider the next greater element as -1.



# Problem Constraints
# 1 <= |A| <= 105

# 1 <= A[i] <= 107



# Input Format
# The first and the only argument of input contains the integer array, A.



# Output Format
# Return an integer array representing the next greater element for each index in A.



# Example Input
# Input 1:

#  A = [4, 5, 2, 10] 
# Input 2:

#  A = [3, 2, 1] 


# Example Output
# Output 1:

#  [5, 10, 10, -1] 
# Output 2:

#  [-1, -1, -1] 


# Example Explanation
# Explanation 1:

# For 4, the next greater element towards its right is 5.
# For 5 and 2, the next greater element towards their right is 10.
# For 10, there is no next greater element towards its right.
# Explanation 2:

# As the array is in descending order, there is no next greater element for all the elements. 

from collections import deque

class Solution:
    def nextGreater(self, A):
        n = len(A)

        if n == 1: return [-1]

        output = [0] * n
        myStack = deque()

        for i in range(n-1, -1, -1):
            while myStack and myStack[-1] <= A[i]:
                myStack.pop()
            
            if myStack:
                output[i] = myStack[-1]
            else:
                output[i] = -1
            
            myStack.append(A[i])

        return output
     
# 5 : All Subarrays
   
# Given an integer array A of size N. You have to generate it's all subarrays having a size greater than 1.

# Then for each subarray, find Bitwise XOR of its maximum and second maximum element.

# Find and return the maximum value of XOR among all subarrays.



# Problem Constraints
# 2 <= N <= 105

# 1 <= A[i] <= 107



# Input Format
# The only argument is an integer array A.



# Output Format
# Return an integer, i.e., the maximum value of XOR of maximum and 2nd maximum element among all subarrays.



# Example Input
# Input 1:

#  A = [2, 3, 1, 4]
# Input 2:

#  A = [1, 3]


# Example Output
# Output 1:

#  7
# Outnput 2:

#  2


# Example Explanation
# Explanation 1:

#  All subarrays of A having size greater than 1 are:
#  Subarray            XOR of maximum and 2nd maximum no.
#  1. [2, 3]           1
#  2. [2, 3, 1]        1
#  3. [2, 3, 1, 4]     7
#  4. [3, 1]           2
#  5. [3, 1, 4]        7
#  6. [1, 4]           5
#  So maximum value of Xor among all subarrays is 7.
# Explanation 2:

#  Only subarray is [1, 3] and XOR of maximum and 2nd maximum is 2.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        stack=[0]
        final_xor=0
        for i in range(1,len(A)):
            while len(stack)!=0:
                final_xor=max(final_xor, A[stack[-1]]^A[i])
                if A[i]<A[stack[-1]]:
                    break
                stack.pop()
            stack.append(i)
        return final_xor


