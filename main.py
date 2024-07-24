"""
Module: main.py
Description: Main program to interact with the GradeBook application.
"""

from gradebook import GradeBook
import re

def get_valid_email():
    """
    Prompt for a valid email address.
    
    Returns:
        str: The valid email address entered by the user.
    """
    while True:
        email = input("Enter email: ").strip()
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return email
        print("Invalid email address. Please enter a valid email.")

def get_valid_name():
    """
    Prompt for a valid name.
    
    Returns:
        str: The valid name entered by the user.
    """
    while True:
        name = input("Enter name: ").strip()
        if not any(char.isdigit() for char in name):
            return name
        print("Invalid name. Please enter a name with alphabets only.")

def get_valid_integer(prompt):
    """
    Prompt for a valid integer input.
    
    Args:
        prompt (str): The prompt message for user input.
    
    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_float(prompt):
    """
    Prompt for a valid float input.
    
    Args:
        prompt (str): The prompt message for user input.
    
    Returns:
        float: The valid float entered by the user.
    """
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Application")
        print()
        print(" 1. Add Student")
        print(" 2. Add Course")
        print(" 3. Register Student for Course")
        print(" 4. Calculate GPA for All Students")
        print(" 5. Calculate Ranking")
        print(" 6. Search by Grade Range")
        print(" 7. Generate Transcript")
        print(" 8. Remove Student or Course")
        print(" 9. Record Drop Out or Withdraw")
        print("10. Exit")
        print()

        choice = input("Choose an action: ").strip()

        if choice == '1':
            print()
            print("Adding a student")
            print()
            email = get_valid_email()
            name = get_valid_name()
            gradebook.add_student(email, name)
            print()
            print("New Student added!")
            print()
        elif choice == '2':
            print()
            print("Adding a course")
            print()
            name = input("Enter course name: ").strip()
            trimester = input("Enter course trimester: ").strip()
            credits = get_valid_integer("Enter course credits: ")
            gradebook.add_course(name, trimester, credits)
            print()
            print("Course Added!")
            print()

        elif choice == '3':
            print()
            print("Registering student for course")
            print()
            student_email = get_valid_email()
            course_name = input("Enter course name: ").strip()
            grade = get_valid_float("Enter course grade: ")
            gradebook.register_student_for_course(student_email, course_name, grade)
            print()
            print("Student Registered for Course!")
            print()

        elif choice == '4':
            print()
            print("Calculating GPA for all students")
            print()
            gradebook.calculate_GPA()
            print()
            print("GPA Calculated for all students!")
            print()
            for student in gradebook.student_list:
                print(f"{student.names} ({student.email}) - GPA: {student.GPA}")
            print()
        elif choice == '5':
            print()
            print("Calculating Ranking")
            print()
            ranking = gradebook.calculate_ranking()
            for student in ranking:
                print(f"Student: {student.names}, Email: {student.email}, GPA: {student.GPA}")
            print()

        elif choice == '6':
            print()
            print("Searching by Grade Range")
            print()
            min_grade = get_valid_float("Enter minimum grade: ")
            max_grade = get_valid_float("Enter maximum grade: ")
            students = gradebook.search_by_grade(min_grade, max_grade)
            for student in students:
                print(f"Student: {student.names}, Email: {student.email}, GPA: {student.GPA}")
            print()

        elif choice == '7':
            print()
            print("Generating Transcript")
            print()
            student_email = get_valid_email()
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"Transcript for {transcript['names']} ({transcript['email']})")
                print(f"GPA: {transcript['GPA']}")
                for course in transcript['courses']:
                    print(f"Course: {course['course']['name']}, Grade: {course['grade']}, Credits: {course['credits']}")
                print()
            else:
                print("Student not found.")
                print()

        elif choice == '8':
            print()
            print("Removing a student or course")
            print()
            sub_choice = input("Enter 's' to remove a student or 'c' to remove a course: ").strip().lower()
            if sub_choice == 's':
                student_email = get_valid_email()
                gradebook.remove_student(student_email)
                print("Student removed!")
            elif sub_choice == 'c':
                course_name = input("Enter course name: ").strip()
                gradebook.remove_course(course_name)
                print("Course removed!")
            else:
                print("Invalid option. Please enter 's' or 'c'.")
            print()

        elif choice == '9':
            print()
            print("Recording Drop Out or Withdraw")
            print()
            student_email = get_valid_email()
            gradebook.record_drop_out_or_withdraw(student_email)
            print("Drop out or withdraw recorded!")
            print()

        elif choice == '10':
            print()
            print("Exiting...")
            break

        else:
            print()
            print("Invalid choice. Please select a valid option.")
            print()

if __name__ == "__main__":
    main()

