
### 18 May Assignment

# 1 : Calculator program

def main(a, b):
    A = a
    B = b 
    add = int(A+B)
    sub = int(A*B)
    mul = int(A-B)
    div = int(A/B)
    print(add, sub, mul, div)
    

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)


# 2 : calculate floor 

def main(A, B):
    if A > B:
        print(A)
    else:
        print(B)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)


 # 3 : Identify odd or even 

 def main(num):
    mod = num % 2
    if mod > 0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    a = int(input())
    main(a)

# 4 : Write a program to input a number(A) from user and print 1 if it is positive, -1 if it is negative, 0 if it's neither positive nor negative.

def main(num):
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    else:
        print(0)
        

if __name__ == '__main__':
    a = int(input())
    main(a)


### 18 May Homework

# 1 : 

'''
You are given 3 integer angles(in degrees) A, B and C of a triangle. 
You have to tell whether the triangle is valid or not.
A triangle is valid if sum of its angles equals to 180.
'''
def main(a, b, c):
    sum = int(a + b + c)
    if sum == 180:
        print(1)
    else:
        print(0)
        

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    main(a, b, c)

# 2 :

# You are given an integer A. You have to tell whether A is divible by both 5 and 11 or not.

def main(num):
    divible_by_5 = num % 5
    divible_by_11 = num % 11
    if divible_by_5 == 0:
        print(1)
    elif divible_by_11 == 0:
        print(1)
    else:
        print(0)
        
if __name__ == '__main__':
    a = int(input())
    main(a)

# 3 : 

# Write a program to input two numbers(A & B) from user and print the minimum element among A & B in each line.

def main(A, B):
    if A < B:
        print(A)
    else:
        print(B)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)


# 4 :

''' You are given the Cost Price C and Selling Price S of a Product. 
You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss.
NOTE: It is guaranteed that Cost Price and Selling Price are not equal. '''

def main(C, S):

    profit = int(S - C)

    if profit > 0:
        print(1)
        print(profit)
    else:
        print(-1)
        print(int(profit * -1)) '''OR'''  print(abs(profit))

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)

# 5 :

''' Given an integer A representing a year, print 1 if it is a leap year else print 0. 
A year is a leap year if either of the following conditions is satisfied:
Year is multiple of 400.
Year is multiple of 4 and not multiple of 100.
'''

def leap_year(yr):
    if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
        print(1)
    else:
        print(0)




