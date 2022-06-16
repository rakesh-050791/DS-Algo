# 1 : 
# Create a class Bill and initialize it with details, previous meter reading and current meter reading. Create a function total_bill() inside Bill class which returns the total bill based on the following criteria:

# 1. For the first 100 units consumed: 3.5 rs/unit

# 2. For next 100 units consumed : 5 rs/unit

# 3. For remaining units consumed: 8 rs/unit

# 4. Meter Charges: 150 rs (It's included only once but is mandatory)

# Example input:

# 200 650

class Bill():

    def __init__(self, prev_read, cur_read):
        self.prev_read = prev_read
        self.cur_read = cur_read
        
    def total_bill(self):
        total=0.0

        current_units = self.cur_read - self.prev_read

        if 100 >= current_units:
            total += current_units * 3.5 
        elif 200 >= current_units:
            total += 100 * 3.5
            total += (current_units - 100) * 5
        elif 200 < current_units:
            total += 100 * 3.5
            total += 100 * 5
            total += (current_units - 200) * 8
        
        total += 150
        return total 


# 2 : 

# Create a class Student and initialize it with details marks in subject 1, credit of subject 1, marks in subject 2, and credit of subject 2.

# Create a function grade_point_average() for the Student class which computes the GPA rounded to two decimals, based on the following criteria of points in a subject :

# 1. If marks>=90:10 points
# 2. If 90>marks>=75: 9 points
# 3. If 75>marks>=60: 8 points
# 4. If 60>marks>=45: 7 points
# 5. If marks<45: 0 points

# GPA = (points in subject 1 * credit of subject 1+ points in subject 2 * credit of subject 2) / ( credit of subject 1 + credit of subject 2)

# The points in a subject should be calculated according to the criteria mentioned in the question.
# Also, implement a special zero case to handle when credits of both subjects are 0, return "Zero credits for both subjects".

# Input Example:

# # class Student takes (marks1,marks2,credits1,credits2)
# (85, 76, 3, 4)

class Student():
    
    def __init__(self, marks1,marks2,credits1, credits2):
        self.marks1, self.marks2   = marks1, marks2
        self.credits1, self.credits2  = credits1, credits2
    
    def grade_point_average(self):
        marks = [self.marks1, self.marks2]
        points = []

        if self.credits1 == 0 or self.credits2 == 0:
            return "Zero credits for both subjects"
        
        for mark in marks:
            if mark >= 90:
                points.append(10)
            elif 90 > mark >= 75:
                points.append(9)
            elif 75 > mark >= 60:
                points.append(8)
            elif 60 > mark >= 45:
                points.append(7)
            elif mark < 45:
                points.append(0)
        
        gpa = (points[0] * self.credits1 + points[1] * self.credits2) / (self.credits1 + self.credits2)
        return round(gpa, 2)