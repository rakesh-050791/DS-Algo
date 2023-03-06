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


# 2 : Task Scheduling

# A CPU has N tasks to be performed. It is to be noted that the tasks have to be completed in a specific order to avoid deadlock. In every clock cycle, the CPU can either perform a task or move it to the back of the queue. You are given the current state of the scheduler queue in array A and the required order of the tasks in array B.

# Determine the minimum number of clock cycles to complete all the tasks.


# Input Format
# First argument consist of integer array A.
# Second argument consist of integer array B.


# Output Format
# Return an integer denoting the minimum number of clock cycles required to complete all the tasks.

# Example Input
# Input 1:

# A = [2, 3, 1, 5, 4]
# B = [1, 3, 5, 4, 2]

# Input 2:

# A = [1]
# B = [1]


# Example Output
# Output 1: 10
# Output 2: 1


# Example Explanation
# Explanation 1:

# According to the order array B task 1 has to be performed first, so the CPU will move tasks 2 and 3 to the end of the queue (in 2 clock cycles).
# Total clock cycles till now = 2
# Now CPU will perform task 1.
# Total clock cycles till now = 3
# Now, queue becomes [5, 4, 2, 3]
# Now, CPU has to perform task 3. So it moves tasks 5, 4, and 2 to the back one-by-one.
# Total clock cycles till now = 6
# Now all the tasks in the queue are as in the required order so the CPU will perform them one-by-one.
# Total clock cycles = 10
# Explanation 2:

# Directly task 1 is completed.

from collections import deque

class Solution:
    def solve(self, A, B):
        n = len(A)
        myQueue = deque(A)
        count = 0
        
        if A == B:
            return n
        else:

            for i in B:
                while i != myQueue[0]:
                    x = myQueue.popleft()
                    myQueue.append(x)
                    count += 1

                myQueue.popleft()
                count += 1
        return count


# 3 : Perfect Numbers
# Given an integer A, you have to find the Ath Perfect Number.

# A Perfect Number has the following properties:

# It comprises only 1 and 2.

# The number of digits in a Perfect number is even.

# It is a palindrome number.

# For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not


# Output Format
# Return a string that denotes the Ath Perfect Number.

# Example Input
# Input 1: A = 2
# Input 2: A = 3


# Example Output
# Output 1: 22
# Output 2: 1111


# Example Explanation
# Explanation 1:

# First four perfect numbers are:
# 1. 11
# 2. 22
# 3. 1111
# 4. 1221

# Explanation 2:
# First four perfect numbers are:
# 1. 11
# 2. 22
# 3. 1111
# 4. 1221

from collections import deque

class Solution:
    def solve(self, A):
        input = [1, 2]
        
        myQueue = deque()

        myQueue.append(1)
        myQueue.append(2)

        while A > 0:
            element = myQueue.popleft() #Pops out the front of the queue

            output = str(element) + str(element)[::-1]

            for i in input:
                myQueue.append(10*element + i)

            A -= 1
        return output

# 4 : Reversing Elements Of Queue

# Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, leaving the other elements in the same relative order.

# NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.



# Problem Constraints
# 1 <= B <= length of the array <= 500000
# 1 <= A[i] <= 100000



# Input Format
# The argument given is the integer array A and an integer B.



# Output Format
# Return an array of integer after reversing the first B elements of A using queue.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5]
#  B = 3
# Input 2:

#  A = [5, 17, 100, 11]
#  B = 2


# Example Output
# Output 1:

#  [3, 2, 1, 4, 5]
# Output 2:

#  [17, 5, 100, 11]


# Example Explanation
# Explanation 1:

#  Reverse first 3 elements so the array becomes [3, 2, 1, 4, 5]
# Explanation 2:

#  Reverse first 2 elements so the array becomes [17, 5, 100, 11]


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
            que=[]
            for i in reversed(range(B)):  
                que.append(A[i])
            ans=len(A)-B
            if ans>0:
                s=B        # starting index
                e=len(A)   # end index
                while s<e:
                    que.append(A[s])
                    s+=1
            return que
    # T.C: O(N) & S.C: O(N)  
    # code Explanation: for loop in range reversed of B--> range=1,0
    # so in que A[1] & A[0] will append
    # for dry run visualization : click on -->    shorturl.at/dpv34


