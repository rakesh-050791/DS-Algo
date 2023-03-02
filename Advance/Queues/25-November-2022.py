# 1 : First non-repeating character

# Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
# B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.


# Input Format
# The only argument given is string A.


# Output Format
# Return a string B after processing the stream of lowercase alphabets A.


# Example Input
# Input 1: A = "abadbc"

# Input 2: A = "abcabc"


# Example Output
# Output 1: "aabbdd"

# Output 2: "aaabc#"

# Example Explanation

# Explanation 1:
# "a"      -   first non repeating character 'a'
# "ab"     -   first non repeating character 'a'
# "aba"    -   first non repeating character 'b'
# "abad"   -   first non repeating character 'b'
# "abadb"  -   first non repeating character 'd'
# "abadbc" -   first non repeating character 'd'

# Explanation 2:
# "a"      -   first non repeating character 'a'
# "ab"     -   first non repeating character 'a'
# "abc"    -   first non repeating character 'a'
# "abca"   -   first non repeating character 'b'
# "abcab"  -   first non repeating character 'c'
# "abcabc" -   no non repeating character so '#'

# Solution Approach :

# You need to maintain a map for each character of the stream.
# After that, you can also maintain a queue for the extraction of information.
# Each character is inserted and removed from the queue at most once; hence time complexity is O(n).

from collections import deque

class Solution:
    def solve(self, A):
        n = len(A)
        hashMap = {}
        myQueue = deque()
        resultStr = ''

        for char in A:
            if char not in hashMap:
                hashMap[char] = 1
                # if char ocuring for the first time, insert in queue
                myQueue.append(char)
            else:
                hashMap[char] += 1

            while myQueue and hashMap[myQueue[0]] > 1:
                myQueue.popleft()
            
            if myQueue:
                resultStr += myQueue[0]
            else:
                resultStr += '#'
        
        return resultStr

# 2 : Min Stack

# Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# NOTE:
# All the operations have to be constant time operations.
# getMin() should return -1 if the stack is empty.
# pop() should return nothing if the stack is empty.
# top() should return -1 if the stack is empty.
# Problem Constraints

# 1 <= Number of Function calls <= 107
# Input Format

# Functions will be called by the checker code automatically.
# Output Format

# Each function should return the values as defined by the problem statement.
# Example Input

# Input 1:
# push(1)
# push(2)
# push(-2)
# getMin()
# pop()
# getMin()
# top()
# Input 2:
# getMin()
# pop()
# top()
# Example Output

# Output 1:
#  -2 1 2
# Output 2:
#  -1 -1
# Example Explanation

# Explanation 1:
# Let the initial stack be : []
# 1) push(1) : [1]
# 2) push(2) : [1, 2]
# 3) push(-2) : [1, 2, -2]
# 4) getMin() : Returns -2 as the minimum element in the stack is -2.
# 5) pop() : Return -2 as -2 is the topmost element in the stack.
# 6) getMin() : Returns 1 as the minimum element in stack is 1.
# 7) top() : Return 2 as 2 is the topmost element in the stack.
# Explanation 2:
# Let the initial stack be : []
# 1) getMin() : Returns -1 as the stack is empty.
# 2) pop() :  Returns nothing as the stack is empty.
# 3) top() : Returns -1 as the stack is empty

class MinStack:
    def __init__(self):
        self.mainstack = []
        self.minStack = []
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.mainstack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
        

    # @return nothing
    def pop(self):
        if self.mainstack:
            value = self.mainstack.pop()
        
            if self.minStack and value == self.minStack[-1]:
                self.minStack.pop()
        else:
            return


    # @return an integer
    def top(self):
        if self.mainstack:
            return self.mainstack[-1]
        else:
            return -1
        

    # @return an integer
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            return -1


# 3 : Sum of min and max
# Given an array A of both positive and negative integers.

# Your task is to compute the sum of minimum and maximum elements of all sub-array of size B.

# NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.



# Problem Constraints
# 1 <= size of array A <= 105

# -109 <= A[i] <= 109

# 1 <= B <= size of array



# Input Format
# The first argument denotes the integer array A.
# The second argument denotes the value B



# Output Format
# Return an integer that denotes the required value.



# Example Input
# Input 1:

#  A = [2, 5, -1, 7, -3, -1, -2]
#  B = 4
# Input 2:

#  A = [2, -1, 3]
#  B = 2


# Example Output
# Output 1:

#  18
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  Subarrays of size 4 are : 
#     [2, 5, -1, 7],   min + max = -1 + 7 = 6
#     [5, -1, 7, -3],  min + max = -3 + 7 = 4      
#     [-1, 7, -3, -1], min + max = -3 + 7 = 4
#     [7, -3, -1, -2], min + max = -3 + 7 = 4   
#     Sum of all min & max = 6 + 4 + 4 + 4 = 18 
# Explanation 2:

#  Subarrays of size 2 are : 
#     [2, -1],   min + max = -1 + 2 = 1
#     [-1, 3],   min + max = -1 + 3 = 2
#     Sum of all min & max = 1 + 2 = 3 

from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def slidingMaximum(self,arr,k):
        N = len(arr)
        ans = 0
        q = deque()
        
        # sliding window in front window
        for i in range(k):
            cur_ele = arr[i]
            while q and cur_ele > q[-1]:
                q.pop()
            q.append(cur_ele)
        
        # start sliding 
        for i in range(N-k):
            out_gng = arr[i]
            
            if out_gng == q[0]:
                peek = q.popleft()
                ans += peek
            else:
                ans += q[0]
        
            in_cmg  = arr[i+k]
            
            while q and in_cmg > q[-1]:
                q.pop()
                
            q.append(in_cmg)
        
        if q: ans += (q.popleft())
                
        return ans 

    def slidingMinimum(self,arr,k):
        N = len(arr)
        ans = 0
        q = deque()
        
        # sliding window in front window
        for i in range(k):
            cur_ele = arr[i]
            while q and cur_ele < q[-1]:
                q.pop()
            q.append(cur_ele)
        
        # start sliding 
        for i in range(N-k):
            out_gng = arr[i]
            
            if out_gng == q[0]:
                peek = q.popleft()
                ans += peek
            else:
                ans += q[0]
        
            in_cmg  = arr[i+k]
            
            while q and in_cmg < q[-1]:
                q.pop()
                
            q.append(in_cmg)
        
        if q: 
            ans += (q.popleft())
                
        return ans 


    def solve(self, A, B):
        mod = 1000000007
        max_sum  =  self.slidingMaximum(A,B)
        min_sum  =  self.slidingMinimum(A,B)

        return (min_sum + max_sum) % mod 


# 4 : Sliding Window Maximum
# Given an array of integers A. There is a sliding window of size B, moving from the very left of the array to the very right. You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window.

# Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].

# Refer to the given example for clarity.

# NOTE: If B > length of the array, return 1 element with the max of the array.



# Problem Constraints
# 1 <= |A|, B <= 106



# Input Format
# The first argument given is the integer array A.

# The second argument given is the integer B.



# Output Format
# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].



# Example Input
# Input 1:

#  A = [1, 3, -1, -3, 5, 3, 6, 7]
#  B = 3
# Input 2:

#  A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
#  B = 6


# Example Output
# Output 1:

#  [3, 3, 5, 5, 6, 7]
# Output 2:

#  [7, 7, 7, 7]


# Example Explanation
# Explanation 1:

#  Window position     | Max
#  --------------------|-------
#  [1 3 -1] -3 5 3 6 7 | 3
#  1 [3 -1 -3] 5 3 6 7 | 3
#  1 3 [-1 -3 5] 3 6 7 | 5
#  1 3 -1 [-3 5 3] 6 7 | 5
#  1 3 -1 -3 [5 3 6] 7 | 6
#  1 3 -1 -3 5 [3 6 7] | 7
# Explanation 2:

#  Window position     | Max
#  --------------------|-------
#  [1 2 3 4 2 7] 1 3 6 | 7
#  1 [2 3 4 2 7 1] 3 6 | 7
#  1 2 [3 4 2 7 1 3] 6 | 7
#  1 2 3 [4 2 7 1 3 6] | 7


from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        q = deque()
        ans = []
        n = len(A)
        for i in range(B) :
            if not q :
                q.append(A[i])
            else :
                while q and A[i] > q[-1] :
                    q.pop()
                else :
                    q.append(A[i])
        ans.append(q[0])

        for i in range(1, n-B +1) :
            leaving = A[i-1]
            if q[0] == leaving :
                x= q.popleft()
            while q and A[i+B-1] > q[-1] :
                q.pop()
            else :
                q.append(A[i+B-1])
            ans.append(q[0])
        return ans

