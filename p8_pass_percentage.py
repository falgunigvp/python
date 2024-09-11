''' 8 find out pass_percentage of a class. A teacher is enterig the marks of students.
a student passes a course if the marks are atleast 40(out 0f 100).teacher wants to know the percentage of student passed.'''

passed_students = 0


num_students = int(input("Enter the number of students: "))

marks = []


for i in range(num_students):
    mark = int(input(f"Enter mark of student {i+1}: "))
    marks.append(mark)
    if mark >= 40:
        passed_students += 1


pass_percentage = (passed_students / num_students) * 100

print(f"Pass percentage: {pass_percentage:.2f}%")