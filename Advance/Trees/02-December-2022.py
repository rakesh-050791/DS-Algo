# 1 : Valid Binary Search Tree

# You are given a binary tree represented by root A.

# Assume a BST is defined as follows:

# 1) The left subtree of a node contains only nodes with keys less than the node's key.

# 2) The right subtree of a node contains only nodes with keys greater than the node's key.

# 3) Both the left and right subtrees must also be binary search trees.

# Output Format
# Return 0 if false and 1 if true.



# Example Input
# Input 1:
 
#    1
#   /  \
#  2    3

# Input 2:

#   2
#  / \
# 1   3

# Example Output
# Output 1: 0
# Output 2: 1

# Example Explanation
# Explanation 1: 2 is not less than 1 but is in left subtree of 1.
# Explanation 2: Satisfies all conditions.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
        start = float('-inf')
        end = float('inf')
        root = A

        result =  self.validBST(root, start, end)
        return 1 if result else 0

    
    def validBST(self, root, start, end):
        if root == None:
            return True
        
        if start <= root.val and root.val <= end:
            lst = self.validBST(root.left, start, root.val - 1)
            rst = self.validBST(root.right, root.val+1, end)
            return lst and rst
        else:
            return False



# 2 : Largest BST Subtree

# You are given a Binary Tree A with N nodes.

# Write a function that returns the size of the largest subtree, which is also a Binary Search Tree (BST).

# If the complete Binary Tree is BST, then return the size of the whole tree.

# NOTE:

# The largest subtree is the subtree with the most number of nodes.

# Input Format
# First and only argument is an pointer to root of the binary tree A.

# Output Format
# Return an single integer denoting the size of the largest subtree which is also a BST.

# Example Input
# Input 1:

#      10
#     / \
#    5  15
#   / \   \ 
#  1   8   7

# Input 2:

#      5
#     / \
#    3   8
#   / \ / \
#  1  4 7  9


# Example Output
# Output 1: 3
# Output 2: 7


# Example Explanation
# Explanation 1:

#  Largest BST subtree is
#                             5
#                            / \
#                           1   8
# Explanation 2:

#  Given binary tree itself is BST.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Info:
    def __init__(self, sz, mx, mn, ans, isBST):
        self.sz = sz
        self.mx = int(mx)
        self.mn = int(mn)
        self.ans = ans
        self.isBST = isBST


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        res = self.largestBSTinBinaryTree(A)
        return res.ans

    def largestBSTinBinaryTree(self, root):

        if root == None:
            return Info(0, -2e9, 2e9, 0, True)

        if root.left == None and root.right == None:
            return Info(1, root.val, root.val, 1, True)

        l = self.largestBSTinBinaryTree(root.left)
        r = self.largestBSTinBinaryTree(root.right)

        ret = Info(0, 0, 0, 0, True)
        ret.sz = 1 + l.sz + r.sz

        if l.isBST and r.isBST and l.mx < root.val and r.mn > root.val:
            ret.mn = min(l.mn, min(r.mn, root.val))
            ret.mx = max(r.mx, max(l.mx, root.val))
            ret.ans = ret.sz
            ret.isBST = True
            return ret

        ret.ans = max(l.ans, r.ans)
        ret.isBST = False
        return ret


# 3 : Check for BST with One Child

# Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.

# Input Format

# First and only argument is an integer array denoting the preorder traversal of binary tree.



# Output Format

# Return a string "YES" if true else "NO".


# Example Input

# Input 1: A : [4, 10, 5, 8]
# Input 2: A : [1, 5, 6, 4]


# Example Output

# Output 1: "YES"
# Output 2: "NO"


# Example Explanation

# Explanation 1:

#  The possible BST is:
#             4
#              \
#              10
#              /
#              5
#               \
#               8
# Explanation 2:

#  There is no possible BST which have the above preorder traversal.

class Solution:
    def solve(self, A):
        n = len(A)
        root = A[0]
        leftMin = float('-inf')
        rightMax = float('inf')

        for i in range(1, n):
            if A[i] > root:
                leftMin = root
            else:
                rightMax = root

            
            if A[i] < leftMin or A[i] > rightMax:
                return 'NO'
            
            root = A[i]
        
        return 'YES'

