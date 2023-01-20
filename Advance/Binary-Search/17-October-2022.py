# 1 :  Square Root of Integer
# Given an integer A.

# Compute and return the square root of A.

# If A is not a perfect square, return floor(sqrt(A)).

# DO NOT USE SQRT FUNCTION FROM THE STANDARD LIBRARY.

# NOTE: Do not use the sqrt function from the standard library. Users are expected to solve this in O(log(A)) time.

# Output Format
# Return floor(sqrt(A))



# Example Input
# Input 1: 11

# Example Output
# Output 1: 3

# Example Explanation
# Explanation:

#  When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
#  When A = 9 which is a perfect square of 3, so we return 3.

class Solution:
    def sqrt(self, A):
        
        if A == 0:
            return 0

        n = A
        low = 1
        high = n
        result = 1

        while (low <= high):
            mid = (low + high) // 2

            if (mid * mid) == n:
                return mid
            
            elif (mid * mid) < n:
                #search in left direction
                result = mid
                low = mid + 1
                
            elif (mid * mid) > n:
                #search in right direction
                high = mid - 1

        return int(result)

# 2 Single Element in Sorted Array

# Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

# NOTE: Users are expected to solve this in O(log(N)) time.

# Input Format
# The only argument given is the integer array A.



# Output Format
# Return the single element that appears only once.



# Example Input
# Input 1:

# A = [1, 1, 7]
# Input 2:

# A = [2, 3, 3]


# Example Output
# Output 1: 7
# Output 2: 2

# Example Explanation
# Explanation 1: 7 appears once
# Explanation 2: 2 appears once

class Solution:
    def solve(self, A):
        n = len(A)
        low = 0
        high = n - 1

        #edge cases
        ## when first element of an array is uniq
        if A[0] != A[1]:
            return A[0]
        
        ## when last element of an array is uniq
        if A[n-1] != A[n-2]:
            return A[n-1]
        
        ## when array length is 1
        if n == 1:
            return A[0]

        while (low <= high):
            mid = (low + high) // 2
            
            # when left to mid or right to mid is not equal to mid, then mid is the unique element
            if A[mid - 1] != A[mid] and A[mid] != A[mid + 1]:
                return A[mid]

            # mid can be at 1st or 2nd occurance (since n-1 elements are in pairs),now bring mid to 1st occurance
            if A[mid - 1] == A[mid]:
                mid = mid - 1
             

            if mid % 2 == 0:
                # search on right
                low = mid + 2 #(because elements are in pair)
            elif mid % 2 != 0:
                # search on left
                high = mid - 1

# 3 : Special Integer

# Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of elements greater than B.



# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9

# 1 <= B <= 10^9



# Input Format
# The first argument given is the integer array A.

# The second argument given is integer B.



# Output Format
# Return the maximum value of K (sub array length).



# Example Input
# Input 1:

# A = [1, 2, 3, 4, 5]
# B = 10
# Input 2:

# A = [5, 17, 100, 11]
# B = 130


# Example Output
# Output 1:

#  2
# Output 2:

#  3


# Example Explanation
# Explanation 1:

# Constraints are satisfied for maximal value of 2.
# Explanation 2:

# Constraints are satisfied for maximal value of 3.

class Solution:
    def solve(self, A, B):
        n = len(A)

        low = 0
        high = n
        result = 0

        while (low <= high):
            mid = (low + high) // 2 

            if self.slidingWindow(A, mid, B):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result
    
    def slidingWindow(self, arr, windowSize, B):
        windowSum = 0
        n = len(arr)

        #calculating first window sum
        for i in range(windowSize):
            windowSum += arr[i]
            if windowSum > B:
                return False
        
        #now slide window & calculate sum 
        ## below both J loops are working, need to figure out which one to keep
        
        for j in range(n - windowSize):
            windowSum -= arr[j]
            windowSum += arr[j + windowSize]

            if windowSum > B:
                return False 

        return True

# 4 : Rotated Sorted Array Search
# Given a sorted array of integers A of size N and an integer B.

# array A is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

# You are given a target value B to search. If found in the array, return its index otherwise, return -1.

# You may assume no duplicate exists in the array.

# NOTE: Users are expected to solve this in O(log(N)) time.



# Problem Constraints
# 1 <= N <= 1000000

# 1 <= A[i] <= 10^9

# all elements in A are distinct.



# Input Format
# The first argument given is the integer array A.

# The second argument given is the integer B.



# Output Format
# Return index of B in array A, otherwise return -1



# Example Input
# Input 1:

# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4 
# Input 2:

# A = [1]
# B = 1


# Example Output
# Output 1:

#  0 
# Output 2:

#  0


# Example Explanation
# Explanation 1:

 
# Target 4 is found at index 0 in A. 
# Explanation 2:

 
# Target 1 is found at index 0 in A.

# In this problem, both minimum and maximum will act as
# pivots. If there are duplicates, then both the sub-arrays
# won’t be monotonous and so a linear search solution would
# be the optimised one.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)
        low = 0
        high = n - 1

        # conditional binary search
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B:
                return mid

            # check if the left subarray is monotonically increasing
            elif A[mid] > A[low]:
                # check if the target lies in the left subarray
                if A[low] <= B < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # check if the right subarray is monotonically increasing
            else:
                # check if the target lies in the right subarray
                if A[mid] < B <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

        # TC: O(logN); SC: O(1)