def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")

course1 = input("Enter course 1: ")
marks1 = int(input("Enter marks 1: "))

course2 = input("Enter course 2: ")
marks2 = int(input("Enter marks 2: "))

course3 = input("Enter course 3: ")
marks3 = int(input("Enter marks 3: "))

total = marks1 + marks2 + marks3
average = total / 3

grade = calculate_grade(average)

print("\n--- Student Details ---")
print("Name:", name)
print("Department:", department)
print("Semester:", semester)
print(course1, ":", marks1)
print(course2, ":", marks2)
print(course3, ":", marks3)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)