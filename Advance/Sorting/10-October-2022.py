# 1 : Inversion count in an array
# Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).


# Input Format
# The only argument given is the integer array A.



# Output Format
# Return the number of inversions of A modulo (109 + 7).



# Example Input
# Input 1:

# A = [3, 2, 1]
# Input 2:

# A = [1, 2, 3]


# Example Output
# Output 1:

# 3
# Output 2:

# 0


# Example Explanation
# Explanation 1:

#  All pairs are inversions.
# Explanation 2:

#  No inversions.

class Solution:
    def solve(self, A):
        n = len(A)
        mod = 10**9 + 7
        result = self.mergeSort(A, 0, n-1)
        return result % mod


    def mergeSort(self, arr, start, end):
        if start == end:
            return 0
        
        midElement = (start + end) // 2

        X = self.mergeSort(arr, start, midElement) #Left array
        Y = self.mergeSort(arr, midElement + 1, end) #Right array
        Z = self.mergeSubarrays(arr, start, midElement, end)
        inversionPairsCount = X + Y + Z

        return inversionPairsCount #% (10**9 + 7)

    def mergeSubarrays(self, arr, start, midElement, end):
        #consider two sorted sub arrays
        ##1 start to midElement
        ##2 midElement+1 to end
        p1 = start
        p2 = midElement + 1
        p3 = 0
        inversionPairs = 0

        tempArray = [0] * (end - start + 1)

        while (p1 <= midElement and p2 <= end):
            if arr[p1] <= arr[p2]:
                tempArray[p3] = arr[p1]
                p1 += 1
                p3 += 1
            else:
                inversionPairs += midElement - p1 + 1
                tempArray[p3] = arr[p2]
                p2 += 1
                p3 += 1
        
        #Copying remaining elements
        while p1 <= midElement:
            tempArray[p3] = arr[p1]
            p1 += 1
            p3 += 1
        
        #Copying remaining elements
        while p2 <= end:
            tempArray[p3] = arr[p2]
            p2 += 1
            p3 += 1
        
        # copying the sorted tempArray (merged two sub arrays) to main array
        i = start
        j = 0 

        while i <= end:
            arr[i] = tempArray[j]
            i += 1
            j += 1
        
        return inversionPairs
        