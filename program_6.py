#6 find a student from CS department

print("----------Find The Student----------")

stu =input("Enter Roll number: ")
if 'cs' in stu or 'Cs' in stu or 'CS' in stu or 'cS' in stu:
    print("From Computer Department")
else:
    print("Other department")