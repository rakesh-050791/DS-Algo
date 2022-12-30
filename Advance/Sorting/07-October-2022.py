# 1 : Kth Smallest Element
# Find the Bth smallest element in given array A .

# NOTE: Users should try to solve it in less than equal to B swaps.

# Example Input
# Input 1:

# A = [2, 1, 4, 3, 2]
# B = 3

# Output 1: 2

# Explanation 1: 3rd element after sorting is 2.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        n = len(A)
        for i in range(len(A)):
            minElement = A[i]
            newIndex = i

            for j in range(i, n):
                if A[j] < minElement:
                    minElement = A[j]
                    newIndex = j
            
            #Swapping
            temp = A[newIndex]
            A[newIndex] = A[i]
            A[i] = temp

            if (i+1==B):
                break;
        
        return A[B-1]
        

# 2 : Merge Two Sorted Arrays
# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.

# Input Format
# First Argument is a 1-D array representing A.

# Second Argument is also a 1-D array representing B.



# Output Format
# Return a 1-D vector which you got after merging A and B.



# Example Input
# Input 1:

# A = [4, 7, 9 ]
# B = [2, 11, 19 ]
# Input 2:

# A = [1]
# B = [2]


# Example Output
# Output 1:

# [2, 4, 7, 9, 11, 19]
# Output 2:

# [1, 2]


# Example Explanation
# Explanation 1:

# Merging A and B produces the output as described above.
# Explanation 2:

#  Merging A and B produces the output as described above.


class Solution:
    def solve(self, A, B):
        M = len(A)
        N = len(B)

        C = [0] * (N+M)

        P1, P2, P3 = 0, 0, 0

        while P1 < M and P2 < N:
            if A[P1] <= B[P2]:
                C[P3] = A[P1]
                P1 += 1
                P3 += 1
            else:
                C[P3] = B[P2]
                P2 += 1
                P3 += 1
        
        while P1 < M:
            C[P3] = A[P1]
            P1 += 1
            P3 += 1
        
        while P2 < N:
            C[P3] = B[P2]
            P2 += 1
            P3 += 1
        
        return C

# 3 Array with consecutive elements

# Given an array of positive integers A, check and return whether the array elements are consecutive or not.
# NOTE: Try this with O(1) extra space.


# Input Format
# The only argument given is the integer array A.



# Output Format
# Return 1 if the array elements are consecutive else return 0.



# Example Input
# Input 1:

#  A = [3, 2, 1, 4, 5]
# Input 2:

#  A = [1, 3, 2, 5]


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  As you can see all the elements are consecutive, so we return 1.
# Explanation 2:

#  Element 4 is missing, so we return 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()

        previousElement = A[0]

        for i in range(1, n):
            if A[i] != previousElement + 1:
                return 0
            previousElement = A[i]
        return 1

# 4 : MaxMod
# Given an array A of size N, Groot wants you to pick 2 indices i and j such that

# 1 <= i, j <= N
# A[i] % A[j] is maximum among all possible pairs of (i, j).
# Help Groot in finding the maximum value of A[i] % A[j] for some i, j.


# Input Format
# First and only argument in an integer array A.



# Output Format
# Return an integer denoting the maximum value of A[i] % A[j] for any valid i, j.



# Example Input
# Input 1:

#  A = [1, 2, 44, 3]
# Input 2:

#  A = [2, 6, 4]


# Example Output
# Output 1:

#  3
# Output 2:

#  4


# Example Explanation
# Explanation 1:

#  For i = 3, j = 2  A[i] % A[j] = 3 % 44 = 3.
#  No pair exists which has more value than 3.
# Explanation 2:

#  For i = 2, j = 1  A[i] % A[j] = 4 % 6 = 4.

# Approach: In a list of numbers, the maximum remainder is always the second largest number. (Obtained by second-largest % largest). 
# Finding and returning this will give the answer.
# Observation : A % B will be maximum if A < B & A, B are maximum possible (so here A will be the second larget
# value of the array and that will be the answer)

class Solution:
    def solve(self, A):
        n = len(A)
        firstMax = secondMax = float('-inf')

        for i in range(n):
            if A[i] > firstMax:
                secondMax = firstMax
                firstMax = A[i]
            
            elif A[i] > secondMax and A[i] != firstMax:
                secondMax = A[i]
        
        if secondMax == float('-inf'):
            return 0

        return secondMax


# 5 Merge Sort


# Given an integer array A, sort the array using Merge Sort.


# Problem Constraints
# 1 <= |A| <= 105
# 1 <= A[i] <= 109


# Input Format
# First argument is an integer array A.


# Output Format
# Return the sorted array.


# Example Input
# Input 1:-
# A = [1, 4, 10, 2, 1, 5]
# Input 2:-
# A = [3, 7, 1]


# Example Output
# Output 1:-
# [1, 1, 2, 4, 5, 10]
# Output 2:-
# [1, 3, 7]


# Example Explanation
# Explanation 1:
# Return the sorted array.


class Solution:
    def solve(self, A):
        n = len(A)
        self.mergeSort(A, 0, n-1)
        return A


    def mergeSort(self, arr, start, end):
        if start == end:
            return
        
        midElement = (start + end) // 2

        self.mergeSort(arr, start, midElement) #Left array
        self.mergeSort(arr, midElement + 1, end) #Right array
        self.mergeSubarrays(arr, start, midElement, end)

        return arr

    def mergeSubarrays(self, arr, start, midElement, end):
        #consider two sorted sub arrays
        ##1 start to midElement
        ##2 midElement+1 to end
        p1 = start
        p2 = midElement + 1
        p3 = 0

        tempArray = [0] * (end - start + 1)

        while (p1 <= midElement and p2 <= end):
            if arr[p1] < arr[p2]:
                tempArray[p3] = arr[p1]
                p1 += 1
                p3 += 1
            else:
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
