n = int(input("Enter the no of subjects : = "))

student = {}

for i in range(n):
    subject = input("Enter the subjects :")
    marks = int(input("Enter the marks :"))
    
    student[subject] = marks
print(student)    
    