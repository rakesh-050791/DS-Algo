# 1 : Double Character Trouble
# You are given a string A.

# An operation on the string is defined as follows:

# Remove the first occurrence of the same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".

# Therefore the string after this operation will be "acd".

# Keep performing this operation on the string until there are no more occurrences of the same consecutive characters and return the final string.


# Example Input
# Input 1: A = abccbc
# Input 2: A = ab


# Example Output
# Output 1: "ac"
# Output 2: "ab"


# Example Explanation
# Explanation 1:

# Remove the first occurrence of same consecutive characters. eg for a string "abbc", 
# the first occurrence of same consecutive characters is "bb".
# Therefore the string after this operation will be "ac".

# Explanation 2: No removals are to be done.

# Solution Approach

# Consider an example string abba.
# When we remove the “bb”, the remaining string is “aa” which has to be removed as well.
# So we need to keep track of the characters before the first occurrence of similar consecutive characters.
# We can do this using a stack.
# We keep pushing the characters in a stack, if the current character is equal to the top of the stack,
# we pop from the stack since they represent
# a pair of similar characters.
# Finally, we print the stack in reverse.

from collections import deque

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        myStack = deque()

        for i in range(n):
            if len(myStack) == 0:
                myStack.append(A[i])
            else:
                if A[i] == myStack[-1]:
                    myStack.pop()
                else:
                    myStack.append(A[i])
        print("myStack = ", myStack)
        result = ''.join(myStack)
        return result


# 2 : Evaluate Expression

# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each string may be an integer or an operator.


# Input Format
# The only argument given is string array A.


# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.


# Example Input
# Input 1:
#     A =   ["2", "1", "+", "3", "*"]
# Input 2:
#     A = ["4", "13", "5", "/", "+"]

# Example Output
# Output 1: 9
# Output 2: 6


# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     13 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6


#Solution Approach : 
# When you encounter an operator, that is when you need the top 2 numbers on the stack, perform the operation on them, and put them on the stack.

from collections import deque

class Solution:
    def evalRPN(self, A):
        if len(A) == 1:
            return A[0]

        myStack = deque()
        operators = ['+', '-', '*', '/']

        for i in A:
            if i not in operators:
                myStack.append(i)
            else:
                if (len(myStack) < 2):
                    return -1
                
                # pop the top two elements from the stack, perform the operation 
                # and push that back into the stack

                operand1 = int(myStack.pop())

                operand2 = int(myStack.pop())

                operator = i 

                if operator =='+':
                    myStack.append(operand1 + operand2)
                elif operator =='-':
                    myStack.append(operand2 - operand1)
                elif operator =='*':
                    myStack.append(operand1 * operand2)
                elif operator =='/':
                    myStack.append(int(operand2) / (int(operand1)))

        return int(myStack[0])


# 3 : Infix to Postfix

# Given string A denoting an infix expression. Convert the infix expression into a postfix expression.

# String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.

# Find and return the postfix expression of A.

# NOTE:

# ^ has the highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.


# Problem Constraints
# 1 <= length of the string <= 500000



# Example Input
# Input 1: A = "x^y/(a*z)+b"

# Input 2: A = "a+b*(c^d-e)^(f+g*h)-i"


# Example Output
# Output 1: "xy^az*/b+"

# Output 2: "abcd^e-fgh*+^*+i-"


# Solution Approach
# Algorithm:

# 1 Scan the infix expression from left to right.
# 2 If the scanned character is an operand, output it.
# 3 Else,
# 3.1 If the precedence of the scanned operator is greater than that of the operator in the stack(or the stack is empty, or the stack contains a ‘(‘ ), push it.
# 3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that, Push the scanned operator to the stack. (If you encounter parenthesis while popping, stop there and push the scanned operator in the stack.)
# 4 If the scanned character is an ‘(‘, push it to the stack.
# 5 If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered, and discard both the parenthesis.
# 6 Repeat steps 2-6 until infix expression is scanned.
# 7 Print the output
# 8 Pop and output from the stack until it is not empty.


from collections import deque

class Solution:
    def solve(self, A):

        myStack = deque()
        operators = ['^', '/', '*', '+', '-']

        output = ''

        for char in A:
            #If the char is an operand, add it to output string.
            if char.isalpha():
                output += char

            #If the char is an operator
            elif char in operators:
                if not myStack:
                    myStack.append(char)
                else:
                    while myStack and (myStack[-1] != '(') and (self.checkPrecedence(myStack[-1]) >= (self.checkPrecedence(char))):
                        output += myStack[-1]
                        myStack.pop()
                    myStack.append(char)

            #If the char is an ‘(‘, append it to the stack.
            elif char == '(':
                myStack.append(char)
                
            # If the char is an ‘)’, pop and to output string from the stack
            # until an ‘(‘ is encountered.
            elif char == ')':
                while myStack[-1] != '(':
                    output += myStack[-1]
                    myStack.pop()
                myStack.pop() #removing the ‘(’ bracket from stack

        #finally add all the remaining operators from stack to output
        while myStack:
            output += myStack[-1]
            myStack.pop()
        

        return output

    def checkPrecedence(self, char):
        if ((char == '+') or (char == '-')):
            return 1
        
        if ((char == '*') or (char == '/')):
            return 2

        if char == '^':
            return 3


# 4 : Passing game

# There is a football event going on in your city. In this event, you are given A passes and players having ids between 1 and 106.

# Initially, some player with a given id had the ball in his possession. You have to make a program to display the id of the player who possessed the ball after exactly A passes.

# There are two kinds of passes:

# 1) ID

# 2) 0

# For the first kind of pass, the player in possession of the ball passes the ball "forward" to the player with id = ID.

# For the second kind of pass, the player in possession of the ball passes the ball back to the player who had forwarded the ball to him.

# In the second kind of pass "0" just means Back Pass.

# Return the ID of the player who currently possesses the ball.


# Input Format
# The first argument of the input contains the number A.

# The second argument of the input contains the number B ( id of the player possessing the ball in the very beginning).

# The third argument is an array C of size A having (ID/0).


# Output Format
# Return the "ID" of the player who possesses the ball after A passes.

# Example Input
# Input 1: A = 10, B = 23, C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]

# Input 2: A = 1, B = 1, C = [2]

# Example Output
# Output 1: 63
# Output 2: 2


# Example Explanation
# Explanation 1:

#  Initially, Player having  id = 23  posses ball. 
#  After pass  1,  Player having  id = 86  posses ball. 
#  After pass  2,  Player having  id = 63  posses ball. 
#  After pass  3,  Player having  id = 60  posses ball. 
#  After pass  4,  Player having  id = 63  posses ball. 
#  After pass  5,  Player having  id = 47  posses ball. 
#  After pass  6,  Player having  id = 63  posses ball. 
#  After pass  7,  Player having  id = 99  posses ball. 
#  After pass  8,  Player having  id = 9   posses ball. 
#  After pass  9,  Player having  id = 99  posses ball. 
#  After pass  10, Player having  id = 63   posses ball.

# Explanation 2:
#  Ball is passed to 2.

from collections import deque

class Solution:
    def solve(self, A, B, C):

        if A == 0:
            return 0

        myStack = deque()
        myStack.append(B)

        for element in C:
            if element == 0 and myStack:
                myStack.pop()
            else:
                myStack.append(element)

        return myStack[-1]


# 5 : Balanced Paranthesis
# Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

# Refer to the examples for more clarity.

# Input Format
# The first and the only argument of input contains the string A having the parenthesis sequence.



# Output Format
# Return 0 if the parenthesis sequence is not balanced.

# Return 1 if the parenthesis sequence is balanced.



# Example Input
# Input 1: A = {([])}
# Input 2: A = (){
# Input 3: A = ()[] 


# Example Output
# Output 1: 1 
# Output 2: 0 
# Output 3: 1 


# Example Explanation
# You can clearly see that the first and third case contain valid paranthesis.

# In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.


from collections import deque

class Solution:
    def solve(self, A):

        n = len(A)
        myStack = deque()

        for i in A:
            if (i == '{' or i == '(' or i == '['):
                myStack.append(i)
            else:
                if len(myStack) == 0:
                    return 0
                
                top = myStack[-1]

                if ((top == '{' and i == '}') or \
                   (top == '(' and i == ')') or \
                   (top == '[' and i == ']')):
                    myStack.pop()
                
        return 1 if len(myStack) == 0 else 0
        