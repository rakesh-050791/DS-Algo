# 1 : QuickSort

# Given an integer array A, sort the array using QuickSort.

# Input 1:

# A = [1, 4, 10, 2, 1, 5]

# Example Output

# Output 1: [1, 1, 2, 4, 5, 10]

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def solve(self, A):
        n = len(A)
        self.quickSort(A, 0, n-1)
        return A

    
    def quickSort(self, arr, start, end):
        if end <= start:
            return 

        pos = self.rearrangeArray(arr, start, end)

        self.quickSort(arr, start, pos - 1)
        self.quickSort(arr, pos + 1, end)


    def rearrangeArray(self, arr, start, end):
        p1 = start + 1
        p2 = end 

        while p1 <= p2:
            if arr[p1] <= arr[start]: #when p1 is at right position
                p1 += 1
            elif arr[p2] >= arr[start]: #when p2 is at right position
                p2 -= 1
            else: #when both p1 & p2 are at wrong position, swap them
                temp = arr[p1]
                arr[p1] = arr[p2]
                arr[p2] = temp
                p1 += 1
                p2 -= 1

        #Swap arr[start] & arr[p2]
        temp = arr[start]
        arr[start] = arr[p2]
        arr[p2] = temp

        return p2 # current position of start


# 2 : Maximum Unsorted Subarray

# Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.

# Output Format
# Return an array of length two where the first element denotes the starting index(0-based) and the second element denotes the ending index(0-based) of the sub-array. If the array is already sorted, return an array containing only one element i.e. -1.

# Example Input
# Input 1:

# A = [1, 3, 2, 4, 5]

# Example Output
# Output 1: [1, 2]

# Explanation 1:

# If we sort the sub-array A1, A2, then the whole array A gets sorted.


class Solution:
    def subUnsort(self, A):
        n = len(A)

        #STEP 1 : To fix the start point of the array traverse through the array and check if any element
        # is greater than the next element A[i] > A[i+1] take that as the start element and break
        start = end = 0
    
        for i in range(0, n-1):
            if A[i] > A[i+1]:
                start = i
                break
        
        #STEP 2 : To fix from the end point of the array traverse through the array and check if any element
        # is lesser than the next element A[i] < A[i-1] and take that as the end point and break;
        for j in range(n-1, 0, -1):
            if A[j] < A[j-1]:
                end = j
                break

        # Corner case if the array is sorted i will reach till n-1
        if start == 0:
            return [-1]


        #STEP 3 : Now find the max and the min element in between the subarray of start and element
        minElement = float('inf')
        maxElement = float('-inf')

        for i in range(start, end+1):
            minElement = min(A[i], minElement)
            maxElement = max(A[i], maxElement)
        

        #STEP 5 : Traverse from the start to end of the array and check if anyelement is greater than minelement
        # If there is anyelement greater then include that also
        newStart = newEnd = 0
        for i in range(n):
            if A[i] > minElement:
                newStart = i
                break
        
        # STEP 6 : Traver from the end to start of the array and check if any element is lesser than the max element
        # If there is any element lesser than the max_element include that also
        for i in range(n-1, -1, -1):
            if A[i] < maxElement:
                newEnd = i
                break


        return [newStart, newEnd]


# Approach 2 


class Solution:
    def subUnsort(self, A):
        # Step 1 : To fix the start point of the array traverse through the array and check if any element
        # is greater than the next element A[i] > A[i+1] take that as the start element and break
        # start = end = 0
        # start = 0
        # end = 0
        n = len(A)
        sorted = True
        minIncorrect = float('inf')
        maxIncorrect = float('-inf')
    
        for i in range(n-1):
            if A[i] <= A[i+1]:
                continue
            else:
                # start = i
                sorted = False
                minIncorrect = min(A[i+1], minIncorrect)
                # break
        
        for j in range(n-1, 0, -1):
            if A[j-1] <= A[j]:
                continue
            else:
                # end = j
                maxIncorrect = max(A[j-1], maxIncorrect)

                # break

        # Corner case if the array is sorted i will reach till n-1
        if sorted:
            return [-1]


        # Now find the max and the min element in between the subarray of start and element
        # minElement = float('inf')
        # maxElement = float('-inf')

        # for i in range(start, end):
        #     minElement = min(A[i], minElement)
        #     maxElement = max(A[i], maxElement)
        
        newStart = newEnd = -1
        for i in range(n):
            # if A[i] > minElement:
            if A[i] <= minIncorrect:
                continue
            else:
                newStart = i
                break
        
        for i in range(n-1, -1, -1):
            # if A[i] < maxElement:
            if A[i] >= maxIncorrect:
                continue
            else:
                newEnd = i
                break


        return [newStart, newEnd]

# 3 : Maximum & Minimum Magic
# Given an array of integers A of size N where N is even.

# Divide the array into two subsets such that

# 1.Length of both subset is equal.
# 2.Each element of A occurs in exactly one of these subset.
# Magic number = sum of absolute difference of corresponding elements of subset.

# Note: You can reorder the position of elements within the subset to find the value of the magic number.

# For Ex:- 
# subset 1 = {1, 5, 1}, 
# subset 2 = {1, 7, 11}
# Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
# Return an array B of size 2, where B[0] = maximum possible value of Magic number modulo 109 + 7, B[1] = minimum possible value of a Magic number modulo 109 + 7.



# Problem Constraints
# 1 <= N <= 105

# -109 <= A[i] <= 109

# N is even



# Input Format
# The first argument given is the integer array A.



# Output Format
# Return an array B of size 2, where B[0] = maximum possible value of Magic number % 109 + 7,B[1] = minimum possible value of a Magic number % 109 + 7.



# Example Input
# Input 1:

#  A = [3, 11, -1, 5]
# Input 2:

#  A = [2, 2]


# Example Output
# Output 1:

#  [14, 10]
# Output 2:

#  [0, 0]


# Example Explanation
# Explanation 1:

#  All possible magical numbers:-
#  sub1 = {3, 11}, sub2 = {-1, 5}, Magic Number = abs(3 - -1) + abs(11 - 5) = 10
#  sub1 = {3, -1}, sub2 = {11, 5}, Magic Number = abs(3 - 11) + abs(-1 - 5) = 14 
#  sub1 = {3, 5}, sub2 = {11, -1}, Magic Number = abs(3 - 11) + abs(5 - -1) = 14
#  sub1 = {11, -1}, sub2 = {3, 5}, Magic Number = abs(11 - 3) + abs(-1 - 5) = 14
#  sub1 = {11, 5}, sub2 = {3, -1}, Magic Number = abs(11 - 3) + abs(5 - -1) = 14
#  sub1 = {-1, 5}, sub2 = {3, 11}, Magic Number = abs(-1 - 3) + abs(5 - 11) = 10 
#  maximum of all magic number = 14 % 10^9 + 7 = 14
#  minimum of all magic number = 10 % 10^9 + 7 = 10
# Explanation 2:

#  Answer is evident.

class Solution:
    def solve(self, A):
        n = len(A)
        mod = 1000000007
        A.sort()

        maxMagicNo = 0

        point1 = 0
        point2 = n//2


        while (point2 <= n-1):
            maxMagicNo = ((maxMagicNo%mod) + (abs(A[point2]-A[point1])%mod))%mod
            point1 += 1
            point2 += 1


        minMagicNo = 0

        for i in range(0, n, 2):
            minMagicNo = (minMagicNo + abs(A[i] - A[i+1])) % mod
        
        return [maxMagicNo, minMagicNo]


# 4 : Maximum Unsorted Subarray

# Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) that sub-array, then the whole array should get sorted. If A is already sorted, output -1.



# Problem Constraints
# 1 <= N <= 1000000
# 1 <= A[i] <= 1000000



# Input Format
# First and only argument is an array of non-negative integers of size N.



# Output Format
# Return an array of length two where the first element denotes the starting index(0-based) and the second element denotes the ending index(0-based) of the sub-array. If the array is already sorted, return an array containing only one element i.e. -1.



# Example Input
# Input 1:

# A = [1, 3, 2, 4, 5]
# Input 2:

# A = [1, 2, 3, 4, 5]


# Example Output
# Output 1:

# [1, 2]
# Output 2:

# [-1]


# Example Explanation
# Explanation 1:

# If we sort the sub-array A1, A2, then the whole array A gets sorted.
# Explanation 2:

# A is already sorted.


## Approach
# Basic Idea would be to 

# Copy the Array
# Sort the Copied Array
# Now we want to know which is the first element is displaced from the start
# Similarly we will find which is the first element displaced from the end
# Answer would be difference of those Index.

# TC would be o(nlogn) for above approach 

# o(n) Approach:

# So following up from above idea what we need to do is find out which is first & last element which is displaced.

# Here we also need to maintain max_so_far

# 1.Iterate through array

 

# If max_so_far > nums[i] => ith element is not currenlty not in correct position.. Now we iterate back untill we find element smaller than it.
# We just need to iterate from start (not i) because we already know element from start are not correct ordered(this avoid repeat )
# Last element for which max_so_far > nums[i] 
# Would be our end point




class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        start = -1; end = -1
        max_so_far = -math.inf
        for i in range(len(A)):
            if max_so_far > A[i]:
                if start == -1:
                    start = i - 1
                while start -1 >= 0 and A[start-1] > A[i] :
                    start -= 1
                end = i+1
            else:
                max_so_far = A[i]
        if end == -1:
            return [-1]
        return [start, end -1]
