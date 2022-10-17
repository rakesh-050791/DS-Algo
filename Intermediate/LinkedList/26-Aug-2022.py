# 1 : Design Linked list

# Given a matrix A of size Nx3 representing operations. Your task is to design the linked list based on these operations.

# There are four types of operations:

# 0 x -1: Add a node of value x before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# 1 x -1: Append a node of value x to the last element of the linked list.
# 2 x index: Add a node of value x before the indexth node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# 3 index -1: Delete the indexth node in the linked list, if the index is valid.
# A[i][0] represents the type of operation.

# A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.

# Note: Indexing is 0 based.

# Output Format
# Return the pointer to the starting of the linked list.


# Example Input
# Input 1:
#     A = [   [0, 1, -1]
#             [1, 2, -1]
#             [2, 3, 1]   ]

# Example Output
# Output 1:
#     1->3->2->NULL
 

#Default 
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# class Solution:
#     # @param A : list of list of integers
#     # @return the head node in the linked list
#     def solve(self, A):




# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkedList :
    def __init__(self) :
        self.head = None

llist = LinkedList()

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):
        llist.head = None
        for x in A :
            if x[0] == 0 :
                newNode = Node(x[1])
                if llist.head == None :
                    llist.head = newNode
                else :
                    newNode.next = llist.head
                    llist.head = newNode
            elif x[0] == 1 :
                newNode = Node(x[1])
                if llist.head == None :
                    llist.head = newNode
                else :
                    current = llist.head
                    while current.next != None :
                        current = current.next
                    current.next = newNode
            elif x[0] == 2 :
                current = llist.head
                pos = 0
                newNode = Node(x[1])
                if x[2] == 0 :
                    newNode.next = llist.head
                    llist.head = newNode
                else :
                    current = llist.head
                    pos = 0
                    while current :
                        if pos == x[2] - 1 :
                            newNode.next = current.next
                            current.next = newNode
                            break
                        else :
                            pos = pos +1
                            current = current.next
            elif x[0] == 3 :
                if x[1] == 0 :
                    llist.head = llist.head.next
                else :
                    current = llist.head
                    prev = None
                    pos = 0
                    while current :
                        if pos == x[1]   :
                            prev.next = current.next
                            break
                        else :
                            pos = pos + 1
                            prev = current
                            current = current.next

        return llist.head