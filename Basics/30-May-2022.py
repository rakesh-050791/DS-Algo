# 1 : Given two numbers A & B. Return their sum.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sum = A + B
        return sum

# 2 : Given two numbers A & B. Return their product.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        product = A * B
        return product


# 3 Given two integers A and B, where A is divisible by B. Print the value of quotient of A divided by B.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        quotient = A / B
        return int(quotient)

# 4 Given a number A. Return square root of the number if it is perfect square otherwise return -1.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        root = A ** (1/2)
        if int(root + 0.5) ** 2 == A:
            return int(root)
        else:
            return int(-1)

# 5 Given a number A. Return 1 if it is perfect square otherwise return 0.
def issquare(num):
    ans  = None
    # YOUR CODE GOES HERE
    root = num ** (1/2)
    if int(root + 0.5) ** 2 == num:
        return int(1)
    else:
        return int(0)

 # 6 You are given a positive integer A denoting the side of a square. You have to calculate the area of the square.

# Area of a square having side S is given by (S * S).

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        area_of_square = A * A 
        return area_of_square

# 7 You are given an integer A, You have to tell whether it is a perfect cube or not.
# A perfect cube is an integer that is equal to some other integer raised to the third power. If X is a perfect cube of Y, then X = Y3.

class Solution:
    # @param A : integer
    # @return an integer
    def isPerfectCube(self, A):
        if round(A ** (1 / 3)) ** 3 == A:
            return(1)
        else:
            return(0)


# 8 You are given two integers A and B. You have to find the value of AB.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self, A, B):
        power = A ** B 
        return power

# 9 You are given an integer A. You have to find the value of cube of A i.e, A3.

class Solution:
    # @param A : integer
    # @return an integer
    def cube(self, A):
        cube = A ** 3
        return(cube)

# 10 You are given a positive integer A denoting the radius of a sphere. You have to calculate the volume of the sphere.

# Volume of a sphere having radius R is given by (4 * π * R3) / 3.

# NOTE: Since, the answer can be a real number, you have to return the ceil value of the volume. Ceil value of a real number X is the smallest integer that is greater than or equal to X.

import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A): 
        pi = 3.1415926535897931
        r = float(A)
        volume_of_sphere = 4.0/3.0*pi* r**3
        return math.ceil(volume_of_sphere) 

# 11 You are given a positive integer A denoting the radius of a circle. You have to calculate the area of the circle.

# Arae of a circle having radius R is given by (π * R2).

# NOTE: Since, the answer can be a real number, you have to return the ceil value of the area. Ceil value of a real number X is the smallest integer that is greater than or equal to X.

# import math
from math import ceil
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        pi = 3.1415926535897931
        r = float(A)
        area_of_circle = pi * r**2
        return ceil(area_of_circle)
