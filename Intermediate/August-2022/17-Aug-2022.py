# 1 : Class Complex Number

# Construct a class called ComplexNumber which stores two properties

# real - The real part
# imaginary - The imaginary part

# The name of the properties should be strictly real and imaginary


# Implement the following functionalities inside this class :-

# add(ComplexNumber) -> Returns an object of ComplexNumber having sum of the two complex numbers.

# subtract(ComplexNumber) -> Returns an object of ComplexNumber having difference of the two complex numbers.

# multiply(ComplexNumber) -> Returns an object of ComplexNumber having multiplication of the two complex numbers.

# divide(ComplexNumber) -> Returns an object of ComplexNumber having division of the two complex numbers.
class ComplexNumber:

    real = 0 
    imaginary = 0
    
    # Define constructor here
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


    def add(self, x: "ComplexNumber")->"ComplexNumber":
        a = complex(self.real , self.imaginary)
        b =  complex(x.real , x.imaginary)
        s = a + b
        return ComplexNumber(s.real, s.imag)
     
    
    def subtract(self, x: "ComplexNumber")->"ComplexNumber":
        a = complex(self.real , self.imaginary)
        b =  complex(x.real , x.imaginary)
        s = a - b
        return ComplexNumber(s.real, s.imag)
        
        
    def multiply(self, x: "ComplexNumber")->"ComplexNumber":
        a = complex(self.real , self.imaginary)
        b =  complex(x.real , x.imaginary)
        s = a * b
        return ComplexNumber(s.real, s.imag)
    
    
    def divide(self, x: "ComplexNumber")->"ComplexNumber":
        a = complex(self.real , self.imaginary)
        b =  complex(x.real , x.imaginary)
        s = a / b
        return ComplexNumber(s.real, s.imag)


a = ComplexNumber(10, 5)
b = ComplexNumber(2, 3)

c1 = a.add(b)
c2 = a.subtract(b)
c3 = a.multiply(b)
c4 = a.divide(b)



# 2 : Class Circle

# Construct a class Circle that represents a Circle.


# The class should support the following functionalities:-
# perimeter() -> returns the perimeter of the circle
# area() -> returns the area of the circle


# Assume Π (pi) = 3.14 for calculations.
# You may define any properties in the class as you see appropriate.

class Circle:
    # Define properties here
    Radius = 0
    
    # Define constructor here
    def __init__(self, Radius):
        self.Radius = Radius


    def perimeter(self):
        # P = 2πr
        P = 2 * 3.14 * self.Radius
        return P
    
    
    def area(self):
        # A = πr2
        A = 3.14 * (self.Radius ** 2)
        return A
    
        
a = Circle(3)  # Radius = 3
a.perimeter() # 18.84
a.area() # 28.26


# 3 Class Rectangle
# Construct a class Rectangle that represents a rectangle.
# The class should support the following functionalities:-
# perimeter() -> returns the perimeter of the rectangle
# area() -> returns the area of the rectangle
# You may define any properties in the class as you see appropriate.
class Rectangle:
    # Define properties here
    Length = 0
    Breadth = 0
    
    
    # Define constructor here
    def __init__(self, Length, Breadth):
        self.Length = Length
        self.Breadth = Breadth


    def perimeter(self):
        P = 2 * (self.Length + self.Breadth)
        return P
       
    def area(self):
        A = self.Length * self.Breadth
        return A    
        
a = Rectangle(2, 3)  #// Length = 2, Breadth = 3
a.perimeter() #// Should give 10
a.area() #// Should give 6





# 4 : Class Fraction

# Construct a class Fraction which stores a fraction. It should contain the

# -Numerator
# -Denominator

# Assume denominator will never be 0.

# The class should support the following functionalities

# add(Fraction) -> Returns the sum of two fractions

# subtract(Fraction) -> Returns the difference of two fractions

# multiply(Fraction) -> Returns the product of two fractions

# The fraction returned needs to be in the simplest form. If the fraction is p/q then p and q must be co-prime.

# You may define any properties in the class as you see appropriate.
class Fraction:

    Numerator = None
    Denominator = None

    def computeGCD(self, numerator, denominator):
        # --Using Euclidean Algorithm 

        # while denominator:
        #     numerator, denominator = denominator, numerator % denominator
        # return numerator

        # --Using Recursion
        if(denominator == 0):
            return abs(numerator)
        else:
            return self.computeGCD(denominator, numerator % denominator)

    # Define constructor here
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, x):
        a = self.numerator 
        b = self.denominator
        c = x.numerator
        d = x.denominator

        Numerator = (a * d + b * c) 
        Denominator = b * d 
        gcd = self.computeGCD(Numerator , Denominator)

        Numerator //= gcd
        Denominator //= gcd 
        return Fraction(Numerator, Denominator)
        
    
    def subtract(self, x):
        a = self.numerator 
        b = self.denominator
        c = x.numerator
        d = x.denominator

        Numerator = (a * d - b * c) 
        Denominator = b * d 
        gcd = self.computeGCD(Numerator , Denominator)

        Numerator //= gcd
        Denominator //= gcd 
        return Fraction(Numerator, Denominator)
    
    def multiply(self, x):
        a = self.numerator 
        b = self.denominator
        c = x.numerator
        d = x.denominator

        Numerator = a * c 
        Denominator = b * d 
        gcd = self.computeGCD(Numerator , Denominator)

        Numerator //= gcd
        Denominator //= gcd 
        return Fraction(Numerator, Denominator)
    
        
x = Fraction(2, 3)  # 2/3
y = Fraction(4, 5) # 4/5
z = x.add(y) # 22/15
z = x.subtract(y) # -2/15
z = x.multiply(y) # 8/15


# 5 : Class Matrix
# Construct a class called Matrix which stores a 2D Array. It should store

# The number of rows

# The number of columns

# The 2D Array itself

# Implement the following functionalities inside this class :-

# input() -> Reads the input from the user. This method should read the input from the user and populate the entire array. Each row will be in a new line and all the elements in a row will be space-separated.

# add(Matrix) -> Returns the sum of two matrices. Assume the matrices provided have the same dimensions.

# subtract(Matrix) -> Returns the sum of two matrices. Assume the matrices provided have the same dimensions.

# transpose() -> Returns a new matrix containing the transpose of the given original matrix.

# print() -> prints the entire matrix row by row. Each row will be in a new line and values in each row should be separated by a single space.

# You may define any properties in the class as you see appropriate.

class Matrix:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.mat = [[0 for j in range(c)] for i in range(r)]

    def input(self):
        for i in range(self.row):
            self.mat[i] = list(map(int, input().split(' ')[:self.column]))
    
    def add(self, x: "Matrix") -> "Matrix":
        res = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                res.mat[i][j] = self.mat[i][j] + x.mat[i][j]
        return res
        
    def subtract(self, x: "Matrix") -> "Matrix":
        res = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                res.mat[i][j] = self.mat[i][j] - x.mat[i][j]
        return res
    
    def transpose(self) -> "Matrix":
        res = Matrix(self.column, self.row)
        for i in range(self.row):
            for j in range(self.column):
                res.mat[j][i] = self.mat[i][j]
        return res
    
    def print(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.mat[i][j] , end=" ")
            print()
