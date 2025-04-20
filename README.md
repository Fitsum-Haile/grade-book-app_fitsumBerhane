Grade Book Application


Overview

The Grade Book Application is a console-based system for managing student records, course registrations, grades, and more. It is designed to facilitate the administration of academic records in an educational institution.


Features

Add Student: Add new students to the system.
Add Course: Add new courses to the system.
Register Student for Course: Register students for courses and record their grades.
Calculate GPA: Compute the GPA for all registered students.
Calculate Ranking: Determine student rankings based on GPA.
Search by Grade Range: Find students within a specific GPA range.
Generate Transcript: Produce a transcript for a selected student.
Remove Student or Course: Delete a student or a course from the system.
Record Drop Out or Withdraw: Record when a student drops out or withdraws from a trimester.


Project Structure

course.py: Defines the Course class.
data/: Contains JSON files for storing student and course data.
courses.json: Stores course data.
students.json: Stores student data.
gradebook.py: Defines the GradeBook class and its associated methods.
main.py: Main program file for the Grade Book application.
student.py: Defines the Student class.
README.md: Documentation file for the project.


Installation

Clone the Repository:
git clone https://github.com/Fitsum-Haile/grade-book-app_fitsumBerhane
cd grade-book-app_fitsumBerhane

Install Dependencies:

Ensure you have Python 3.8 or higher installed. No additional dependencies are required.


Run the Application:

python main.py


Usage


When you run the application, you will be presented with a menu of options. Follow the prompts to perform various operations such as adding students, registering courses, calculating GPAs, and more.

Data Persistence


The application uses JSON files to store data persistently. Data is loaded from data/students.json and data/courses.json at startup and saved back to these files when changes are made.


Contact

For questions or support, please contact:

Author: Fitsum Berhane
Email: f.haile@alustudent.com
