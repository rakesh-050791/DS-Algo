# 1 : N integers containing only 1, 2 & 3

# Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.

# NOTE: All the A integers will fit in 32-bit integers.



# Output Format
# Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.



# Example Input
# Input 1: A = 3
# Input 2: A = 7


# Example Output
# Output 1: [1, 2, 3]

# Output 2: [1, 2, 3, 11, 12, 13, 21]


# Example Explanation
# Explanation 1: Output denotes the first 3 integers that contains only digits 1, 2 and 3.

# Explanation 2: Output denotes the first 3 integers that contains only digits 1, 2 and 3.

from collections import deque

class Solution:
    def solve(self, A):
        input = [1, 2, 3]

        myQueue = deque()
        output = []

        myQueue.append(1)
        myQueue.append(2)
        myQueue.append(3)

        while A > 0:
            element = myQueue.popleft() #Pops out the front of the queue

            output.append(element)

            for i in input:
                myQueue.append(10*element + i)

            A -= 1
        return output


# Approach 2 

from collections import deque
class Solution:
    def solve(self, A):

        myQueue = deque()
        output = []

        myQueue.append('1')
        myQueue.append('2')
        myQueue.append('3')


        for i in range(A):
            element = myQueue.popleft() #Pops out the front of the queue
            output.append(element)

            myQueue.append(element + '1')
            myQueue.append(element + '2')
            myQueue.append(element + '3')

        return output


        
