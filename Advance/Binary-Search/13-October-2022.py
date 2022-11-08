# 3 : Find a peak element

# Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

# For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

# NOTE: Users are expected to solve this in O(log(N)) time. The array may have duplicate elements.

# Example Input
# Input 1: A = [1, 2, 3, 4, 5]

# Example Output
# Output 1: 5

# Example Explanation
# Explanation 1: 5 is the peak.


class Solution:
    def solve(self, A):
        n = len(A)
        arr = A

        if n == 1:
            return A[0]

        if arr[0] >= arr[1]:
            return arr[0]
        
        if arr[n-1] >= arr[n-2]:
            return arr[n-1]

        low = 0
        high = n-1

        while (low < high):
            mid = (low + high) // 2

            if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]):
                return arr[mid]

            elif arr[mid-1] > arr[mid]:
                high = mid - 1
                
            elif arr[mid+1] > arr[mid]:
                low = mid + 1
            
        return arr[low]
            

# 4 : Search in Bitonic Array!

# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

# NOTE:

# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


# Example Input
# Input 1:

#  A = [3, 9, 10, 20, 17, 5, 1]
#  B = 20

# Example Output
# Output 1: 3
 
# Example Explanation
# Explanation 1: B = 20 present in A at index 3

class Solution:
    def solve(self, A, B):
        n = len(A)

        #Searching Bitonic element
        low = 0
        high = n-1
        while (low <= high):
            mid = (low + high) // 2

            if (A[mid-1] < A[mid]) and (A[mid] > A[mid+1]):
                bionicPoint = mid
                break

            elif A[mid+1] > A[mid]:
                low = mid + 1
            elif A[mid-1] > A[mid]:
                high = mid - 1

        # Binary search on the left side of the Bitonic element
        low = 0
        high = bionicPoint-1
        while (low <= high):
            mid = (low + high) // 2

            if A[mid] == B:
                return mid
            
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1

        # Binary search on the right side of the Bitonic element
        low = bionicPoint
        high = n-1
        while (low <= high):
            mid = (low + high) // 2

            if A[mid] == B:
                return mid
            
            elif A[mid] < B:
                high = mid - 1
            else:
                 low = mid + 1

        return -1