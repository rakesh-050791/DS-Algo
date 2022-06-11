# 1 :  Write a program to print all negative numbers from input array A of size
# N where you have to take integer N and further N elements as input from user.


# elements_size = 0
elements = input().split()
elements.pop(0)
result = []


for element in elements:
        result.append(int(element))

for element in result:
    if element < 0:
        print(element, end= ' ')



 # 2 Write a program to print sum of elements of the 
 # input array A of size N where you have to take integer N and further N elements as input from user. 

# elements_size = 0
elements = input().split()
elements.pop(0)
result = []
sum = 0


for element in elements:
        result.append(int(element))
 
for element in result:
    sum += element
print(sum)



# 3 Write a program to input N numbers array from user and delete an element from it at specified position X.

no_of_elements = int(input())
elements = input().split()
element_to_remnove = int(input())
result = []
elements.pop(element_to_remnove - 1)


for element in elements:
    print(element, end= ' ')



 # 4 Write a program to input N numbers array from user and insert an element Y in it at specified position X.

no_of_elements = int(input())
elements = input().split()
position_at_element_to_add = int(input())
element_to_add = int(input())
elements.insert(position_at_element_to_add - 1, element_to_add)

for element in elements:
    
    print(element, end= ' ')


# 5 Write a program to print the input array A of size N in 
# reverse order where you have to take integer N and further N elements as input from user.
elements = input().split()
elements.remove(elements[0])
result = []


result = []


for element in elements:
        result.append(int(element))

for element in range(len(result)-1, -1, -1):
    print(result[element], end=' ')


# 6 : Write a program to check if the input list has consecutive duplicate elements or not.
 # Return True if there are consecutive duplicate elements in the list else return False.

def duplicate(ls,n):
    elements = ls
    previous_element = None
    consecutive_duplicates = []

    for element in elements:
        if element == previous_element:
            consecutive_duplicates.append(element)
            # print('Inside IF, Before % s' % previous_element)
            previous_element = element
            # print('Inside IF, After % s' % previous_element)
        else:
            previous_element = element
            # print('Inside Else % s' % consecutive_duplicates)
        
    if len(consecutive_duplicates) >= 1:
        return True
    else:
        return False

# 7 : Write a program to find the difference between the sum 
# of all even elements and sum of all odd elements from the given list.

def even_odd(lst):
    diff = 0
    sum_of_evens = 0 
    sum_of_odds = 0

    for element in lst:
        if element % 2 == 0:
            sum_of_evens += element
        else:
            sum_of_odds += element
    
    return int(sum_of_evens - sum_of_odds)


# 8 : Write a program for a given integer x and a list ls to return the first multiple of x 
# that occurs in the list, and if there isn’t any multiple of x in the list then return -1.

def first_multiple(ls,x):

    multiples_of_x = []

    for element in ls:
        if element % x == 0:
            multiples_of_x.append(element)

    if len(multiples_of_x) > 0:
        return(multiples_of_x[0])
    else:
        return(-1)

