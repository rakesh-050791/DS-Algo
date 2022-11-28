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

        
