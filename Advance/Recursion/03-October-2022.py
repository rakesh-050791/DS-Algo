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