# Student Result Management System

students = []

# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 75:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 40:
        return 'C'
    else:
        return 'Fail'

# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    sub1 = float(input("Enter Marks of Subject 1: "))
    sub2 = float(input("Enter Marks of Subject 2: "))
    sub3 = float(input("Enter Marks of Subject 3: "))

    total = sub1 + sub2 + sub3
    percentage = total / 3
    grade = calculate_grade(percentage)

    student = {
        "Roll": roll,
        "Name": name,
        "Subject1": sub1,
        "Subject2": sub2,
        "Subject3": sub3,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    students.append(student)
    print("Student Record Added Successfully!")

# Function to display all students
def display_students():
    if len(students) == 0:
        print("No Records Found!")
    else:
        for s in students:
            print("\n---------------------------")
            print("Roll Number :", s["Roll"])
            print("Name :", s["Name"])
            print("Subject 1 :", s["Subject1"])
            print("Subject 2 :", s["Subject2"])
            print("Subject 3 :", s["Subject3"])
            print("Total :", s["Total"])
            print("Percentage :", round(s["Percentage"], 2))
            print("Grade :", s["Grade"])

# Function to search student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    found = False

    for s in students:
        if s["Roll"] == roll:
            print("\nStudent Found!")
            print("Name :", s["Name"])
            print("Total :", s["Total"])
            print("Percentage :", round(s["Percentage"], 2))
            print("Grade :", s["Grade"])
            found = True
            break

    if not found:
        print("Student Not Found!")

# Function to update student record
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for s in students:
        if s["Roll"] == roll:
            print("Enter New Marks")

            s["Subject1"] = float(input("Subject 1: "))
            s["Subject2"] = float(input("Subject 2: "))
            s["Subject3"] = float(input("Subject 3: "))

            s["Total"] = s["Subject1"] + s["Subject2"] + s["Subject3"]
            s["Percentage"] = s["Total"] / 3
            s["Grade"] = calculate_grade(s["Percentage"])

            print("Record Updated Successfully!")
            return

    print("Student Not Found!")

# Function to delete student record
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Record Deleted Successfully!")
            return

    print("Student Not Found!")

# Main Menu
while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        display_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        update_student()

    elif choice == '5':
        delete_student()

    elif choice == '6':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")