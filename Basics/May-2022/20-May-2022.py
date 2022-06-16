# 1 :
# Write a program to print all Natural numbers from 1 to N where you have to take N as input from user

def main(num):
    for i in range(1, num + 1):
        print (i, end = ' ')

if __name__ == '__main__':
    N = int(input())
    main(N)

# 2 :

# Write a program to print all odd numbers from 1 to N where you have to take N as input from user.

def main(num):
    for i in range(1, num + 1):
        if i % 2 != 0:
            print (i, end = ' ')

if __name__ == '__main__':
    N = int(input())
    main(N)


# 3 : 

# Write a program to input an integer from user and print 1 if it is odd otherwise print 0.

def main(num):
    if num % 2 != 0:
        print (1)
    else:
        print (0)

if __name__ == '__main__':
    N = int(input())
    main(N)


# 4 : 

# Write a program to input an integer from user and print 1 if it is odd otherwise print 0.

def main(num):
    if num == 1:
        print ('January')
    elif num == 2:
        print ('February')
    elif num == 3:
        print ('March')
    elif num == 4:
        print ('April')
    elif num == 5:
        print ('May')
    elif num == 6:
        print ('June')
    elif num == 7:
        print ('July')
    elif num == 8:
        print ('August')
    elif num == 9:
        print ('September')
    elif num == 10:
        print ('October')
    elif num == 11:
        print ('November')
    elif num == 12:
        print ('December')
    else:
        print ('Please enter valid number only')

if __name__ == '__main__':
    N = int(input())
    main(N)


# 5 : 

# Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user

def main(num):
    sum = 0
    while(num > 0):  
       sum += num  
       num -= 1  
    print(sum)  

if __name__ == '__main__':
    N = int(input())
    main(N)

 # 6 :

 '''You are given an integer A, you need to find and 
 return the sum of all the even numbers between 1 and A.
Even numbers are those numbers that are divisible by 2.'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        sum = 0
        while(A > 0):
            if A % 2 == 0:
                sum += A  
            A -= 1  
        return sum 

# 7 : 
# You are given a positive integer A. You have to print the sum of all odd numbers in the range [1, A].

def main(num):
    sum = 0
    while(num > 0):
        if num % 2 != 0:
            sum += num  
        num -= 1  
    print(sum)

if __name__ == '__main__':
    num = int(input())
    main(num)

# 8 :

# Write a program to print all Natural numbers from N to 1 where you have to take N as input from user

def main(num):
    while(num > 0):  
       print (num, end = ' ')  
       num -= 1  

if __name__ == '__main__':
    N = int(input())
    main(N)

# 9 :

'''Write a program to print all even numbers from 1 to N where you have to take N as input from user.
Strictly use while loop.'''

def main(num):
    number = 1
    while number <= num:
        if(number % 2 == 0):
            print(number, end=' ')
        number += 1 

if __name__ == '__main__':
    num = int(input())
    main(num)




