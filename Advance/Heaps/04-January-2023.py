# 1 : K Places Apart

# N people having different priorities are standing in a queue.

# The queue follows the property that each person is standing at most B places away from its position in the sorted queue.

# Your task is to sort the queue in the increasing order of priorities.

# NOTE:

# No two persons can have the same priority.
# Use the property of the queue to sort the queue with complexity O(NlogB).


# Problem Constraints
# 1 <= N <= 100000
# 0 <= B <= N



# Input Format
# The first argument is an integer array A representing the priorities and initial order of N persons.
# The second argument is an integer B.



# Output Format
# Return an integer array representing the sorted queue.



# Example Input
# Input 1:

#  A = [1, 40, 2, 3]
#  B = 2
# Input 2:

#  A = [2, 1, 17, 10, 21, 95]
#  B = 1


# Example Output
# Output 1: [1, 2, 3, 40]
# Output 2: [1, 2, 10, 17, 21, 95]


# Example Explanation
# Explanation 1:

#  Given array A = [1, 40, 2, 3]
#  After sorting, A = [1, 2, 3, 40].
#  We can see that difference between initial position of elements amd the final position <= 2.
# Explanation 2:

#  After sorting, the array becomes [1, 2, 10, 17, 21, 95].

import heapq as heap

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        #size of the array.
        lengthOfArray = len(A)
        # check if B = 0.
        if B == 0:
            return A

        # create a answer array
        ans = []

        # create a min heap array
        minHeap = []
       
        # Push elements from 0 --> B in min Heap
        for i in range(B):
            heap.heappush(minHeap,A[i])

        # iterate through B --> lengthOfArray.
            #- push the next element in minHeap
            #- pop min element from minHeap and put it in ans array.
            # - remember after going through the entire array. B elements will still remain in minHeap as you are iterating through b --> n.
        for i in range(B,lengthOfArray):
            heap.heappush(minHeap,A[i])
            ans.append(heap.heappop(minHeap))

        # Push all the min element one by one in ans array.
        while minHeap:
            ans.append(heap.heappop(minHeap))

        return ans

# 2 : Running median

# Given an array of integers, A denoting a stream of integers. New arrays of integer B and C are formed.
# Each time an integer is encountered in a stream, append it at the end of B and append the median of array B at the C.

# Find and return the array C.

# NOTE:

# If the number of elements is N in B and N is odd, then consider the median as B[N/2] ( B must be in sorted order).
# If the number of elements is N in B and N is even, then consider the median as B[N/2-1]. ( B must be in sorted order).


# Problem Constraints
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 109



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return an integer array C, C[i] denotes the median of the first i elements.



# Example Input
# Input 1:

#  A = [1, 2, 5, 4, 3]
# Input 2:

#  A = [5, 17, 100, 11]


# Example Output
# Output 1:

#  [1, 1, 2, 2, 3]
# Output 2:

#  [5, 5, 17, 11]


# Example Explanation
# Explanation 1:

#  stream          median
#  [1]             1
#  [1, 2]          1
#  [1, 2, 5]       2
#  [1, 2, 5, 4]    2
#  [1, 2, 5, 4, 3] 3
# Explanation 2:

#  stream          median
#  [5]              5
#  [5, 17]          5
#  [5, 17, 100]     17
#  [5, 17, 100, 11] 11 

import heapq
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_heap=[]
        min_heap=[]
        B=[]
        # ans=[]
        for i,v in enumerate(A):
            diff=len(max_heap)-len(min_heap)
            # print(diff)
            if diff==0:
                if len(min_heap)!=0 and v>min_heap[0]:
                    min_elem=heapq.heappop(min_heap)
                    heapq.heappush(max_heap,-min_elem)
                    heapq.heappush(min_heap,v)
                else:
                    heapq.heappush(max_heap,-v)
            else:
                if v<-max_heap[0]:
                    max_elem=heapq.heappop(max_heap)
                    heapq.heappush(min_heap,-max_elem)
                    heapq.heappush(max_heap,-v)
                else:
                    heapq.heappush(min_heap,v)
            B.append(-max_heap[0])
            # ans.append(B[i//2])
        return B
