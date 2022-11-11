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


