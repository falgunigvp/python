#3   extracting field of a roll number using string indexing and slicing.


roll_number = input("Please Enter 6 digit Roll number: ")
print("-----------------------------")


print("your department is computer science:",roll_number[0:2])
print("your Roll number is :",roll_number[2:4])
print("Admission year is:",roll_number[4:])