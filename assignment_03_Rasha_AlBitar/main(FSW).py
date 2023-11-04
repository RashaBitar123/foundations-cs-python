"""
Simulate student data by creating a list of dictionaries. Each dictionary represents a
student's information with the following fields:
• 'ID' (integer): The student's unique identifier.
• 'Name' (string): The student's name.
• 'Age' (integer): The student's age.
• 'Major' (string): The student's major.
• 'GPA' (float): The student's grade point average.
Implement functions that simulate API endpoints for retrieving student
information.
"""
student_data = [
    {
        "ID": 1,
        "Name": "Razan",
        "Age": 21,
        "Major": "Computer Science",
        "GPA": 3.7
    },
    {
        "ID": 2,
        "Name": "Christine",
        "Age": 21,
        "Major": "Computer Engineering",
        "GPA": 3.9
    },
    {
        "ID": 3,
        "Name": "Rasha",
        "Age": 22,
        "Major": "Computer Engineering",
        "GPA": 3
    }

]

# Function to get a student by ID
def get_student_by_id(student_data, student_id):
    for student in student_data:
        if student["ID"] == student_id:
            return student
    return None

# Function to get all students
def get_all_students(student_data):
    return student_data

# Function to get students by major
def get_students_by_major(student_data, major):
    students_in_major = [student for student in student_data if student["Major"] == major]
    return students_in_major

# Function to add a new student
def add_student(student_data, name, age, major, gpa):
    new_student_id = max(student["ID"] for student in student_data) + 1
    new_student = {
        "ID": new_student_id,
        "Name": name,
        "Age": age,
        "Major": major,
        "GPA": gpa
    }
    student_data.append(new_student)

# Function to find common majors in two lists
def find_common_majors(student_data1, student_data2):
    majors1 = set(student["Major"] for student in student_data1)
    majors2 = set(student["Major"] for student in student_data2)
    common_majors = majors1.intersection(majors2)
    return common_majors

# Function to delete a student by ID
def delete_student_by_id(student_data, student_id):
    for student in student_data:
        if student["ID"] == student_id:
            student_data.remove(student)
            return

# Function to calculate average GPA
def calculate_average_gpa(student_data):
    total_gpa = sum(student["GPA"] for student in student_data)
    average_gpa = total_gpa / len(student_data)
    return average_gpa

# Function to get top performers by GPA
def get_top_performers(student_data, num_top_performers):
    sorted_students = sorted(student_data, key=lambda student: student["GPA"], reverse=True)
    top_performers = [(student["Name"]) for student in sorted_students[:num_top_performers]]
    return top_performers

# Main menu
while True:
    print("- - - - - - - - - - - - - - -")
    print("1. Get Student by ID")
    print("2. Get All Students")
    print("3. Get Students by Major")
    print("4. Add Student")
    print("5. Find Common Majors")
    print("6. Delete Student")
    print("7. Calculate Average GPA")
    print("8. Get Top Performers")
    print("9. Exit")
    choice = input("Enter a choice: ")

    if choice == "1":
        student_id = int(input("Enter the student ID: "))
        student = get_student_by_id(student_data, student_id)
        if student:
            print(student)
        else:
            print("Student not found.")

    elif choice == "2":
        students = get_all_students(student_data)
        for student in students:
            print(student)

    elif choice == "3":
        major = input("Enter the major: ")
        students = get_students_by_major(student_data, major)
        for student in students:
            print(student)

    elif choice == "4":
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        major = input("Enter the student's major: ")
        gpa = float(input("Enter the student's GPA: "))
        add_student(student_data, name, age, major, gpa)
        print("Student added.")

    elif choice == "5":
        student_data2 = [
            {
                "ID": 3,
                "Name": "Aline",
                "Age": 22,
                "Major": "Computer Science",
                "GPA": 3.8
            }
        ]
        common_majors = find_common_majors(student_data, student_data2)
        print("Common majors:", common_majors)

    elif choice == "6":
        student_id = int(input("Enter the student ID to delete: "))
        delete_student_by_id(student_data, student_id)
        print("Student deleted.")

    elif choice == "7":
        average_gpa = calculate_average_gpa(student_data)
        print("Average GPA:", average_gpa)

    elif choice == "8":
        num_top_performers = int(input("Enter the number of top performers to retrieve: "))
        top_performers = get_top_performers(student_data, num_top_performers)
        print("Top Performers:", top_performers)

    elif choice == "9":
        break

    else:
        print("Invalid choice. Please enter a valid option.")
