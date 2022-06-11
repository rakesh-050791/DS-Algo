# 1 : Given an array A and an integer B, find the number of occurrences of B in A.

class Solution():
    def solve(self, A, B):
        occurrences_of_B = 0
        list_of_values = A

        for element in list_of_values:
            if element == B:
                occurrences_of_B += 1
        return occurrences_of_B


# 2 : Write a program that returns the product of all elements present in the list.

def product(lst):
    result = 1
    for x in lst:
         result = result * x
    return result
 
# 3 : Write a program to print maximum and minimum elements of the input array A of size N 
# where you have to take integer N and other N elements as input from the user.

def main(lst):
    elements = lst
    elements.remove(elements[0])
    result = []
    
    for element in elements:
        result.append(int(element))

    maximum = result[0]
    minimum = result[0]

    for i in range(0, len(result)):
        if result[i] > maximum:
            maximum = result[i]
        elif result[i] < minimum:
            minimum = result[i]

    print(maximum,end = " ")
    print(minimum)
    


if __name__ == '__main__':
    lst = input().split()
    main(lst)



# 4 : Write a program that will keep track of items for a shopping list. 
# The program should keep asking for new items as input until “end” is entered and also print the full shopping list.

def shopping_list():
    shoplist=[]

    while True:
        new_item = input()
        if new_item == 'end':
            break
        shoplist.append(new_item)

    print(shoplist)
  

shopping_list() 



# 5 : Write a program that returns the list of elements that are present in the given list lst and are divisible by 5 and 7.
def divisible(lst):
    
    elements=[]

    for element in lst:
        if (element % 5 == 0) and (element % 7 == 0):
            elements.append(element)

    return elements



# 6 : You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        elements = A
        maximum = 1

        if len(elements) < 2:
            return(-1)

        for element in range(len(elements)):
            if elements[element] > elements[maximum]:
                maximum = element

        second_max = -1

        for element in range(len(elements)):
            if element != maximum:
                second_max = max(second_max, elements[element])

        return(second_max)


# 7 : You are given an integer T (number of test cases). 
# You are given array A and an integer B for each test case. 
# You have to tell whether B is present in array A or not.

def main():
    no_of_test_cases = int(input())
    
    while no_of_test_cases > 0:

        elements = input().split()

        elements.remove(elements[0])
        result = []
        
        for element in elements:
            result.append(int(element))

        number_to_check = int(input())

        if number_to_check in result:
            print(1)
        else:
            print(0)

        no_of_test_cases -= 1


if __name__ == '__main__':
    main()

# 8 : Write a program that will keep track of items for a shopping list. 
# The program should keep asking for new items as input until “end” is entered and also print the full shopping list.

def shopping_list():
    shoplist=[]

    while True:
        new_item = input()
        if new_item == 'end':
            break
        shoplist.append(new_item)

    print(shoplist)
  

shopping_list() 














