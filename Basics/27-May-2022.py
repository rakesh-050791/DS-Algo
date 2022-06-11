# 1 : Given an integer N. Print N lines. The ith line having 2 * N - (i-1) * 2 stars and (i-1) * 2 spaces.

'''Input:-

5

Output:-

********** // 0 spaces

****__**** // 2 spaces

***____*** // 4 spaces

**______** // 6 spaces

*________* // 8 spaces

Here '_' is used to represent spaces. You have to print spaces in your code.'''

def main(n): 
    for row in range(1,n+1):
        for col in range(n-row + 1):
            print('*', end='')
        for col in range((row-1) * 2):
            if row == 1:
                break
            else:
                print(' ', end='')
        for col in range(n-row + 1):
            print('*', end='')
        
        print()

# 2 :

# Given an integer N. Print N lines. The ith line having i * 2 stars and 2 * (N-i) spaces.

# Input:-

# 5

# Output:-

# *________* // 8 spaces

# **______** // 6 spaces

# ***____*** // 4 spaces

# ****__**** // 2 spaces

# ********** // 0 spaces

def main(n): 
    for row in range(1,n+1):
        for col in range(row):
            print('*', end='')
        for col in range((n-row) * 2):
            print(' ', end='')
        for col in range(row):
            print('*', end='')
        
        print()

if __name__ == '__main__':
    n = int(input())
    main(n)

# 3 :

'''Given an integer N, print the corresponding pattern for N.

For example if N = 4 then pattern will be like: '''


# 1
# 1 2
# 1 2 3
# 1 2 3 4

def main(n):
    for i in range (n):
        for j in range(i+1):
            if (j<i):
                print (j+1, end=" ")
            else :
                print (j+1,end="")
        print("")

if __name__ == '__main__':
    n = int(input())
    main(n) 

# 4 : 
# Given an Integer N. Print an Inverse half pyramid of N lines using '*'.
# *****

# ****

# ***

# **

# *


def main(n):
    for row in range(1, n+1):
        for col in range(1, n - row + 2):
            print('*', end='')
        print()

if __name__ == '__main__':
    n = int(input())
    main(n)
# 5 :

# Given an integer N (N >= 2). Print N lines with two stars ('*') in each line with N - 2 spaces in between.

# *___*

# *___*

# *___*

# *___*

# *___*

def main(n):
    for row in range(n):
        print('*', end='')
        for col in range (1, n - 1):
            print(' ', end='')
        print('*')

if __name__ == '__main__':
    n = int(input())
    main(n)

# 6 :
# Given an integer N, print the corresponding Half Diamond pattern with 2*N - 1 rows.

# For example if N = 5 then pattern will be like:

# * 
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def main(n):
    for row in range(n):
        for col in range(0, row + 1):
            print('*', end='')
        print()
    for row in range(1, n):    
        for col in range(row, n):
            print('*', end='')
        print()



if __name__ == '__main__':
    n = int(input())
    main(n)

# 7 : Given an Integer N. Print N lines of Integers, each line has integers 1 to i where i is the line number. Replace all even numbers with a space.

# For example

# Input:-

# 5

# Output:-

# 1

# 1_

# 1_3

# 1_3_

# 1_3_5

# Here '_' represents space for explanation purpose only. You have to print space in your code.


def main(n):
    for row in range(1, n+1):
        for col in range(1, row+1):
            if col % 2 == 0:
                print(' ', end='') 
            else:
                print(col, end='')
        print()

if __name__ == '__main__':
    n = int(input())
    main(n)


# 8 : 
# Given an integer N. Print the following pattern of N lines.

# Input:-

# 5

# Output:-

# *_____*

# *____*

# *___*

# *__*

# *_*

def main(n):
    for row in range(1, n+1):
        print('*', end='')
        for col in range(n-row +1):
            print(' ', end='')
        print('*')

if __name__ == '__main__':
    n = int(input())
    main(n)

# 9 :
# Given an integer N. Print the following pattern.

# Input:-

# 5

# Output:-

# ____* // 4 spaces

# ___** // 3 spaces

# __*** // 2 spaces

# _**** // 1 space

# ***** // 0 space

def main(n):
    for row in range(1, n+1):
        for col in range(n-row):
            print(' ', end='')
        for col in range(row):
            print('*', end='')
        print()

if __name__ == '__main__':
    n = int(input())
    main(n)
