# 1 : Linked List insert, delete and print operations

# Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes - an integer value and a pointer to the next node. It should support the following operations:

# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space.
# Note:

# If an input position does not satisfy the constraint, no action is required.
# Each print query has to be executed in a new line.


# Example Input
# 5
# i 1 23
# i 2 24
# p
# d 1
# p


# Example Output
# 23 24
# 24


# Example Explanation
# After first two cases linked list contains two elements 23 and 24.
# At third case print: 23 24.
# At fourth case delete value at first position, only one element left 24.
# At fifth case print: 24.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

ll = LinkedList()

def insert_node(position, value):
    newNode = Node(value)

    if position == 1:
        newNode.next = ll.head
        ll.head = newNode
    else:
        currentNode = ll.head
        currentPosition = 1
        while currentNode:
            if currentPosition == position-1:
                tempNode = currentNode.next
                currentNode.next = newNode
                newNode.next = tempNode
                return
            else:
                currentNode = currentNode.next
                currentPosition += 1


def delete_node(position):
    if position == 1:
        ll.head = ll.head.next
    else:
        currentNode = ll.head
        currentPosition = 1

        while currentNode.next:
            if currentPosition == position-1:
                currentNode.next = currentNode.next.next
                return
            else:
                currentNode = currentNode.next
                currentPosition += 1
        return

def print_ll():
    if ll.head == None:
        return
    else:
        currentNode = ll.head
        while currentNode.next:
            print(currentNode.data, end=' ')
            currentNode = currentNode.next
        
        print(currentNode.data)


# 2 : Delete middle node of a Linked List

# Given a singly linked list, delete middle of the linked list.

# For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5

# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.

# For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

# Return the head of the linked list after removing the middle node.

# If the input linked list has 1 node, then this node should be deleted and a null node should be returned.


# Input Format

# The only argument given is the node pointing to the head node of the linked list


# Solution using slow, fast approach 

class Solution:
    def solve(self, A):
        if not A or not A.next:
            return None

        slow = A 
        fast = A
        previous = None

        # while(fast.next != None and fast.next.next != None):
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = slow.next

        return A


# 3 : Middle element of linked list

# Given a linked list of integers, find and return the middle element of the linked list.

# NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.


# Input Format
# The only argument given head pointer of linked list.

# Output Format
# Return the middle element of the linked list.

# Example Input
# Input 1:

#  1 -> 2 -> 3 -> 4 -> 5
# Input 2:

#  1 -> 5 -> 6 -> 2 -> 3 -> 4

# Example Output
# Output 1: 3

# Output 2: 2

# Example Explanation
# Explanation 1:

#  The middle element is 3.
# Explanation 2:

#  The middle element in even length linked list of length N is ((N/2) + 1)th element which is 2.


# Solution Hint :

# One way is to traverse the whole linked list and calculate the length and then traverse half the length to find the middle element.

# We can do it in one traversal by maintaining a slow and fast pointer.

# The fast pointer moves twice as the slow pointer does. When the fast pointer is at the end of the linked list, the slow pointer will point to the middle element.

# Return the element at which the slow pointer points.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        if not A or not A.next:
            return A

        slow = fast = A 
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.val


# 4 : Reverse Linked List

# You are given a singly linked list having head node A. You have to reverse the linked list and return the head node of that reversed list.

# NOTE: You have to do it in-place and in one-pass.

# Input Format
# First and only argument is a linked-list node A.

# Output Format
# Return a linked-list node denoting the head of the reversed linked list.



# Example Input
# Input 1: A = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 

# Example Output
# Output 1: 5 -> 4 -> 3 -> 2 -> 1 -> NULL 


# Example Explanation
# Explanation 1:

# The linked list has 5 nodes. After reversing them, the list becomes : 5 -> 4 -> 3 -> 2 -> 1 -> NULL 


# # Solution Approach
# ITERATIVE SOLUTION
# Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.
# While you are traversing the list, change the current node's next pointer to point to its previous element. 
# Since a node does not have reference to its previous node, you must store its previous element beforehand. 
# You also need another pointer to store the next node before changing the reference. 
# Do not forget to return the new head reference at the end!


# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:

    #idea here is to keep adding head at the start of the new Linkedlist

    def reverseList(self, A):
        head = A
        temp =  head 
        headOfReverseLL = None

        while head != None:
            temp =  head 
            head = head.next
            temp.next = None #breaking link from existing linkedList 
            temp.next = headOfReverseLL #adding link to a new linkedList 
            headOfReverseLL = temp
        
        return headOfReverseLL


# 5 : Reverse Link List II || Revervse Linked List between two points

# Reverse a linked list A from position B to C.

# NOTE: Do it in-place and in one-pass.


# Input Format
# The first argument contains a pointer to the head of the given linked list, A.

# The second arugment contains an integer, B.

# The third argument contains an integer C.

# Output Format
# Return a pointer to the head of the modified linked list.

# Example Input
# Input 1:

#  A = 1 -> 2 -> 3 -> 4 -> 5
#  B = 2
#  C = 4

# Example Output
# Output 1:

#  1 -> 4 -> 3 -> 2 -> 5


# Example Explanation
# Explanation 1:

#  In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
#  Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, A, B, C):
        head = A
        current = A

        first = last = fromm = to = None
        count = 0

        while current != None:
            count += 1

            if count < B:
                first = current
            
            if count == B:
                fromm = current
            
            if count == C:
                to = current
                last = to.next
            
            current = current.next

        
        to.next = None #break link from existing LinkedList 

        self.reverseList(fromm)

        if first != None:
            first.next = to
        else:
            head = to

        fromm.next = last

        return head

    def reverseList(self, fromm):
        head = fromm
        temp =  head 
        headOfReverseLL = None

        while head != None:
            temp =  head 
            head = head.next
            temp.next = None #breaking link from existing linkedList 
            temp.next = headOfReverseLL #adding link to a new linkedList 
            headOfReverseLL = temp


# 6 : K reverse linked list

# Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return the modified linked list.



# Problem Constraints
# 1 <= |A| <= 103

# B always divides A



# Input Format
# The first argument of input contains a pointer to the head of the linked list.

# The second arugment of input contains the integer, B.



# Output Format
# Return a pointer to the head of the modified linked list.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5, 6]
#  B = 2
# Input 2:

#  A = [1, 2, 3, 4, 5, 6]
#  B = 3


# Example Output
# Output 1:

#  [2, 1, 4, 3, 6, 5]
# Output 2:

#  [3, 2, 1, 6, 5, 4]


# Example Explanation
# Explanation 1:

#  For the first example, the list can be reversed in groups of 2.
#     [[1, 2], [3, 4], [5, 6]]
#  After reversing the K-linked list
#     [[2, 1], [4, 3], [6, 5]]
# Explanation 2:

#  For the second example, the list can be reversed in groups of 3.
#     [[1, 2, 3], [4, 5, 6]]
#  After reversing the K-linked list
#     [[3, 2, 1], [6, 5, 4]]

sys.setrecursionlimit(10**6)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, A, B):
        if not A:
            return 

        originalHead = A # preserving original head, so that we can link the initial B reversed elements with next b elements using recursion
        head = A
        temp = head
        reverseListHead = None 
        count = B

        while (count > 0 and head != None):
            count -= 1
            temp = head
            head = head.next
            temp.next = None # breaking link from existing Linked ListNode
            temp.next = reverseListHead
            reverseListHead = temp

        
        newHead = self.reverseList(head, B) # newHead after B elements

        originalHead.next = newHead

        return reverseListHead


# 7 : Remove Nth Node from List End

# Given a linked list **A**, remove the **B-th** node from the end of the list and return its head. For example, Given linked list: `1->2->3->4->5`, and `B = 2`. After removing the second node from the end, the linked list becomes `1->2->3->5`. **NOTE:** If **B** is greater than the size of the list, remove the first node of the list. **NOTE:** Try doing it using constant additional space.
# Problem Constraints

# 1 <= |A| <= 106
# Input Format

# The first argument of input contains a pointer to the head of the linked list. The second argument of input contains the integer B.
# Output Format

# Return the head of the linked list after deleting the B-th element from the end.
# Example Input

# Input 1:
# A = 1->2->3->4->5
# B = 2
# Input 2:
# A = 1
# B = 1
# Example Output

# Output 1:
# 1->2->3->5
# Output 2:
  
# Example Explanation

# Explanation 1:
# In the first example, 4 is the second last element.
# Explanation 2:
# In the second example, 1 is the first and the last element.

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        current=A
        remove=A
        previous=A
        count=1
        while current.next:
            count+=1
            if count>B:
                remove=remove.next
            if count>(B+1):
                previous=previous.next
            current=current.next
        if count<=B:
            A=A.next
            return A

        if current.next is None and count==1:
            return
        previous.next=remove.next
        return A
        