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
    
    for i in range(position - 1):
        currentNode = currentNode.next
        
    newNode.next = currentNode.next
    currentNode.next = newNode
    return llist


# 5 : Delete a Node
def deleteNode(llist, position):
    currentNode = llist
    
    if position==0:
        llist=llist.next
    
    for i in range(position - 1):
        currentNode = currentNode.next
        
    currentNode.next = currentNode.next.next
    
    return llist
    

# 6 : Get Node Value
def getNode(llist, positionFromTail):
    currentNode = llist
    count = 0
    while currentNode:
        count += 1
        currentNode = currentNode.next
    
    positionFromHead = count - positionFromTail - 1
    
    currentNode = llist
    for i in range(positionFromHead):
        currentNode = currentNode.next 
        
    return currentNode.data


# 7 : Print LinkedList in Reverse
def reversePrint(llist):
    elements = []
    while llist:
        elements.append(llist.data)
        llist = llist.next
    
    for i in elements[::-1]:
        print(i)


# 8 : compare two Linked lists 
# You’re given the pointer to the head nodes of two linked lists. 
# Compare the data in the nodes of the linked lists to check if they are equal. 
# If all data attributes are equal and the lists are the same length, return 1. Otherwise, return 0.

# Function Description

# Complete the compare_lists function in the editor below.

# compare_lists has the following parameters:

# SinglyLinkedListNode llist1: a reference to the head of a list
# SinglyLinkedListNode llist2: a reference to the head of a list
# Returns

# int: return 1 if the lists are equal, or 0 otherwise

# Input Format

# The first line contains an integer t, the number of test cases.

# Each of the test cases has the following format:
# The first line contains an integer n, the number of nodes in the first linked list.
# Each of the next n lines contains an integer, each a value for a data attribute.
# The next line contains an integer m, the number of nodes in the second linked list.
# Each of the next m lines contains an integer, each a value for a data attribute.

# Output Format

# Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.

# The output is handled by the code in the editor and it is as follows:

# For each test case, in a new line, print 1 if the two lists are equal, else print 0.

def compare_lists(llist1, llist2):
        if (llist1 is None or llist2 is None):
            return 0
        else:
            while(llist1 and llist2):
                if llist1.data!=llist2.data:
                    return 0
                llist1=llist1.next
                llist2=llist2.next
            
        if llist1 is None and llist2 is None:
            return 1
        else:
            return 0  


