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