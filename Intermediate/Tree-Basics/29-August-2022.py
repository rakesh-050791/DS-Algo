# 1 : Tree Height

# You are given the root node of a binary tree A. You have to find the height of the given tree.

# A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.


import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        root = A 

        if root == None:
            return 0
        
        left = self.solve(root.left)
        right = self.solve(root.right)

        return 1 + max(left, right)


