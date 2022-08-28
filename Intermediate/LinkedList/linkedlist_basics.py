# 1 :  This is an to practice traversing a linked list. Given a pointer to the head node of a linked list, 
# print each node's data element, one per line. If the head pointer is null (indicating the list is empty), 
# there is nothing to print.

# Function Description

# Complete the printLinkedList function in the editor below.

# printLinkedList has the following parameter(s):

# SinglyLinkedListNode head: a reference to the head of the list
# Print

# For each node, print its data value on a new line (console.log in Javascript).
# Input Format

# The first line of input contains , the number of elements in the linked list.
# The next  lines contain one element each, the  values for each node.

def printLinkedList(head):
    # print("HEAD = ", head.next.data)
    currentNode = head 
    while currentNode is not None:
        print(currentNode.data)
        currentNode = currentNode.next


# 2 : Insert a node at the head of a linked list


# Given a pointer to the head of a linked list, insert a new node before the head. 
# The next value in the new node should point to head and the data value should be replaced with a given value. 
# Return a reference to the new head of the list. The head pointer given may be null meaning that the initial list is empty.

# Function Description

# Complete the function insertNodeAtHead in the editor below.

# insertNodeAtHead has the following parameter(s):

# SinglyLinkedListNode llist: a reference to the head of a list
# data: the value to insert in the data field of the new node
# Input Format

# The first line contains an integer n, the number of elements to be inserted at the head of the list.
# The next n lines contain an integer each, the elements to be inserted, one per function call.


# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    newNode = SinglyLinkedListNode(data)
    newNode.next = llist
    llist = newNode
    
    return llist


# 3 : Insert a Node at the Tail of a Linked List 

def insertNodeAtTail(head, data):
    newNode = SinglyLinkedListNode(data)
    if head is None:
        head = newNode
    else:
        currentNode = head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
    
    return head

# 4 : Insert a node at a specific position in a linked list

# Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its data attribute, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    newNode = SinglyLinkedListNode(data)
    currentNode = llist
    count = 0 
    
    for i in range(position - 1):
        count += 1
        currentNode = currentNode.next
        
    newNode.next = currentNode.next
    currentNode.next = newNode
    return llist

