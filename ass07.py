# STUDENT INFORMATION
student_record = []
for i in range(1,3):
    print("Enter information for student: ")
    name= input("Enter your full name > ")
    level= int(input("Enter your level > "))
    location= input("Enter your address > ")
    dept= input("Enter your department > ")
    student ={"name":name, "level":level, "location":location, "dept":dept}
    student_record["name"] = student
print(student_record)

