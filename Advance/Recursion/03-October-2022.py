# 1 : Tower of Hanoi

# In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right) and A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
# You have the following constraints:
# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.
# You have to find the solution to the Tower of Hanoi problem.
# You have to return a 2D array of dimensions M x 3, where M is the minimum number of moves needed to solve the problem.
# In each row, there should be 3 integers (disk, start, end), where:

# disk - number of disk being moved
# start - number of the tower from which the disk is being moved
# stop - number of the tower to which the disk is being moved

# Example Input
# Input 1: A = 2

# Example Output
# Output 1: [1 1 2 ] [2 1 3 ] [1 2 3 ]

# Explanation 1:
# We shift the first disk to the middle tower.
# We shift the second disk to the last tower.
# We, finally, shift the first disk from the middle tower to the last tower.

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def towerOfHanoi(self, A):
        result = []
        def TOH(n, source, temp, destination):
            if n == 0:
                return

            TOH(n-1, source, destination, temp) # Move n-1 discs from source to temp step by step

            current = [n, source, destination]  # Move n discs from source to destination
            result.append(current)

            TOH(n-1, temp, source, destination) # Move n-1 discs from temp to destination step by step

        TOH(A, 1, 2, 3)

        return result

# 2 : Gray Code
# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

# A gray code sequence must begin with 0.

# Example Input
# Input 1: A = 2


# Example Output
# output 1: [0, 1, 3, 2]

# Explanation 1:

# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        result = self.getGrayCode(A)
        return [int(element, 2) for element in result]
    
    def getGrayCode(self, n):
        if n <= 0:
            return ['0']
        if n == 1:
            return ['0', '1']

        rescursionResult = self.getGrayCode(n-1)

        output = []

        for i in range(len(rescursionResult)):
            s = rescursionResult[i]
            output.append('0' + s)
        
        for i in range(len(rescursionResult) - 1, -1, -1):
            s = rescursionResult[i]
            output.append('1' + s)

        return output
