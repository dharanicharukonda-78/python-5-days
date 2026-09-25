name = input("Enter name: ")
marks1 = int(input("Enter subject1 marks: "))
marks2 = int(input("Enter subject2 marks: "))
marks3 = int(input("Enter subject3 marks: "))
total = marks1 + marks2 + marks3
average = total / 3
print("Student name:", name)
print("Total marks:", total)
print("Average marks:", average)
if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 60:
    print("Grade C")
else:
    print("Fail")
