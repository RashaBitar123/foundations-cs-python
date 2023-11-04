"""
You need to create a simple data frame to represent information about students and their exam
scores. Your data frame should be a list of dictionaries, where each dictionary represents a
student's information. Each student's information should include the following fields:
• 'Name' (string): The student's name.
• 'Age' (integer): The student's age.
• 'Scores' (tuple of integers): A tuple containing three exam scores (out of 100) for the
student.

"""
data_frame = [
    {
        "Name": "Aline",
        "Age": 20,
        "Scores": (85, 92, 78)
    },
    {
        "Name": "Razan",
        "Age": 21,
        "Scores": (78, 89, 95)
    },
    {
        "Name": "Sally",
        "Age": 19,
        "Scores": (90, 88, 92)
    },
    {
        "Name": "Rasha",
        "Age": 22,
        "Scores": (80, 85, 88)
    },
    {
        "Name": "Lilian",
        "Age": 20,
        "Scores": (92, 91, 96)
    }
]

# Function to calculate the average score for each student
def get_average_scores(data_frame):
    average_scores = {}
    for student in data_frame:
        name = student["Name"]
        scores = student["Scores"]
        average = sum(scores) / len(scores)
        average_scores[name] = average
    return average_scores

# Function to get the name of the youngest student
def get_youngest_student(data_frame):
    youngest = min(data_frame, key=lambda student: student["Age"])
    return youngest["Name"]

# Function to get the name of the student with the highest total score
def get_highest_score(data_frame):
    highest = max(data_frame, key=lambda student: sum(student["Scores"]))
    return highest["Name"]

# Function to add a new student to the data frame
def add_student(data_frame, name, age, scores):
    new_student = {
        "Name": name,
        "Age": age,
        "Scores": scores
    }
    data_frame.append(new_student)

# Function to remove a student from the data frame
def remove_student(data_frame, name):
    data_frame[:] = [student for student in data_frame if student["Name"] != name]

# Function to find common students in two data frames
def find_common_students(data_frame1, data_frame2):
    names1 = {student["Name"] for student in data_frame1}
    names2 = {student["Name"] for student in data_frame2}
    common_students = names1.intersection(names2)
    return common_students

# Function to find students with consistent improvement in scores
def find_consistent_improvement(data_frame):
    consistent_improvement = []
    for student in data_frame:
        scores = student["Scores"]
        if scores[0] < scores[1] < scores[2]:
            consistent_improvement.append(student["Name"])
    return tuple(consistent_improvement)

# Main menu
while True:
    print("- - - - - - - - - - - - - - -")
    print("1. Get Average Score")
    print("2. Get Youngest Student")
    print("3. Get Highest Score")
    print("4. Add Student")
    print("5. Remove Student")
    print("6. Get Common Students")
    print("7. Find Students with Consistent Improvement")
    print("8. Exit")
    choice = input("Enter a choice: ")

    if choice == "1":
        average_scores = get_average_scores(data_frame)
        print("Average Scores:")
        for name, average in average_scores.items():
            print(f"{name}: {average:.2f}")

    elif choice == "2":
        youngest = get_youngest_student(data_frame)
        print(f"Youngest Student: {youngest}")

    elif choice == "3":
        highest_score = get_highest_score(data_frame)
        print(f"Student with Highest Total Score: {highest_score}")

    elif choice == "4":
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        scores = tuple(int(x) for x in input("Enter three exam scores (separated by spaces): ").split())
        add_student(data_frame, name, age, scores)
        print(f"{name} added to the data frame.")

    elif choice == "5":
        name = input("Enter the name of the student to remove: ")
        remove_student(data_frame, name)
        print(f"{name} removed from the data frame.")

    elif choice == "6":
        data_frame2 = [
            {
                "Name": "Lilian",
                "Age": 22,
                "Scores": (76, 88, 91)
            },
            {
                "Name": "Lamees",
                "Age": 20,
                "Scores": (92, 91, 96)
            }
        ]
        common_students = find_common_students(data_frame, data_frame2)
        print("Common Students:", common_students)

    elif choice == "7":
        consistent_students = find_consistent_improvement(data_frame)
        if consistent_students:
            print("Students with Consistent Improvement:", ", ".join(consistent_students))
        else:
            print("No students with consistent improvement found.")

    elif choice == "8":
        break

    else:
        print("Invalid choice. Please enter a valid option.")
11 
