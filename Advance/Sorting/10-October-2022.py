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


# 2 : Count swaps in InsertionSort - II
# Given an integer array A of size N, sort the elements in increasing order using Insertion Sort.

# You are asked to return the total number of shifts/swaps done.


# Input Format
# First and only argument is an integer array A.



# Output Format
# Return an integer denoting the number of swaps.



# Example Input
# Input 1:

#  A = [5, 3, 1, 9, 4]
# Input 2:

#  A = [2, 10, 4, 11]


# Example Output
# Output 1:

#  5
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Array will be sorted in 5 Swaps.
# Explanation 2:

#  Only 1 swap is required.

class Solution:
    def solve(self, A):
        n = len(A)
        swapCount = 0
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if A[j] > A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp 
                    swapCount += 1
                else:
                    break;
        return swapCount


# 3 : Sum the Difference
# Given an integer array, A of size N.
# You have to find all possible non-empty subsequences of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence. Then add up all the differences to get the number.

# As the number may be large, output the number modulo 1e9 + 7 (1000000007).

# NOTE: Subsequence can be non-contiguous.



# Problem Constraints
# 1 <= N <= 10000

# 1<= A[i] <=1000



# Input Format
# First argument is an integer array A.



# Output Format
# Return an integer denoting the output.



# Example Input
# Input 1:

# A = [1, 2] 
# Input 2:

# A = [1]


# Example Output
# Output 1:

#  1 
# Output 2:

#  0


# Example Explanation
# Explanation 1:

# All possible non-empty subsets are:
# [1]    largest-smallest = 1 - 1 = 0
# [2]    largest-smallest = 2 - 2 = 0
# [1 2]  largest-smallest = 2 - 1 = 1
# Sum of the differences = 0 + 0 + 1 = 1
# So, the resultant number is 1 
# Explanation 2:

#  Only 1 subsequence of 1 element is formed.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        if n == 1:
            return 0
        
        A.sort()
        result = 0
        maxElementSum = 0
        minElementSum = 0
        mod = 1000000007

        for i in range(n):
            maxElementSum += A[i] * ((1 << i) % mod)
            minElementSum += A[i] * ((1 << (n-1)-i) % mod)

        return (maxElementSum - minElementSum) % mod
        