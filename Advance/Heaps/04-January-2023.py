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


# 3 : Ath largest element

# Given an integer array B of size N.

# You need to find the Ath largest element in the subarray [1 to i], where i varies from 1 to N. In other words, find the Ath largest element in the sub-arrays [1 : 1], [1 : 2], [1 : 3], ...., [1 : N].

# NOTE: If any subarray [1 : i] has less than A elements, then the output should be -1 at the ith index.



# Problem Constraints
# 1 <= N <= 100000
# 1 <= A <= N
# 1 <= B[i] <= INT_MAX



# Input Format
# The first argument is an integer A.
# The second argument is an integer array B of size N.



# Output Format
# Return an integer array C, where C[i] (1 <= i <= N) will have the Ath largest element in the subarray [1 : i].



# Example Input
# Input 1:

#  A = 4  
#  B = [1 2 3 4 5 6] 
# Input 2:

#  A = 2
#  B = [15, 20, 99, 1]


# Example Output
# Output 1:

#  [-1, -1, -1, 1, 2, 3]
# Output 2:

#  [-1, 15, 20, 20]


# Example Explanation
# Explanation 1:

#  for i <= 3 output should be -1.
#  for i = 4, Subarray [1:4] has 4 elements 1, 2, 3 and 4. So, 4th maximum element is 1.
#  for i = 5, Subarray [1:5] has 5 elements 1, 2, 3, 4 and 5. So, 4th maximum element is 2.
#  for i = 6, Subarray [1:6] has 6 elements 1, 2, 3, 4, 5 and 6. So, 4th maximum element is 3.
#  So, output array is [-1, -1, -1, 1, 2, 3].
 
# Explanation 2:

#  for i <= 1 output should be -1.
#  for i = 2 , Subarray [1:2] has 2 elements 15 and 20. So, 2th maximum element is 15.
#  for i = 3 , Subarray [1:3] has 3 elements 15, 20 and 99. So, 2th maximum element is 20.
#  for i = 4 , Subarray [1:4] has 4 elements 15, 20, 99 and 1. So, 2th maximum element is 20.
#  So, output array is [-1, 15, 20, 20].

import heapq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        temp = []
        ans = []
        for i in range(A):
            temp.append(B[i])
            if i!=A-1:
                ans.append(-1)
        heapq.heapify(temp)
        # temp contains A items and it is min heap, so answer will be the min element which is temp[0]
        ans.append(temp[0])
        for i in range(A, len(B)):
            if B[i]>temp[0]:
                heapq.heapreplace(temp, B[i])
            ans.append(temp[0])
        return ans


# 4 : Ways to form Max Heap

# Max Heap is a special kind of complete binary tree in which, for every node, the value present in that node is greater than the value present in its children nodes.

# Find the number of distinct Max Heap that can be made from A distinct integers.

# In short, you have to ensure the following properties for the max heap :

# Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.)
# Every node is greater than all its children.
# NOTE: If you want to know more about Heaps, please visit this link. Return your answer modulo 109 + 7.



# Problem Constraints
# 1 <= A <= 100



# Input Format
# The first and only argument is an integer A.



# Output Format
# Return an integer denoting the number of distinct Max Heap.



# Example Input
# Input 1:

#  A = 4
# Input 2:

#  A = 10


# Example Output
# Output 1:

#  3
# Output 2:

#  3360


# Example Explanation
# Explanation 1:

#  Let us take 1, 2, 3, 4 as our 4 distinct integers
#  Following are the 3 possible max heaps from these 4 numbers :
#       4           4                     4
#     /  \         / \                   / \ 
#    3    2   ,   2   3      and        3   1
#   /            /                     /    
#  1            1                     2
# Explanation 2:

#  Number of distinct heaps possible with 10 distinct integers = 3360.

MOD = 10**9+7

class Solution:
    # @param A : integer
    # @return an integer
    
    def comb(self,r,n) :
        if 2*r > n : 
            return self.comb(n-r,n)
        c = 1
        for i in range(r) :
            c = c*(n-i)//(i+1)
        return c
    
    def solve(self, A):
        ans,h = [1,1], 0
        for n in range(2,A+1) :
            if 2<<h <= n :
                h += 1
            m = n-(1<<h)+1
            l = (1<<(h-1))-1 + min(m,1<<(h-1))
            r = (1<<(h-1))-1 + max(0,m-(1<<(h-1)))
            ans.append((self.comb(l,n-1)*ans[l]*ans[r])%MOD)
        return ans[A]



