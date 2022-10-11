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
