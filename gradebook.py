"""
Module: gradebook.py
Description: Defines the GradeBook class and its associated methods.
"""

import json
from student import Student
from course import Course

class GradeBook:
    """
    Manages the records of students and courses.
    
    Attributes:
        student_list (list): The list of students.
        course_list (list): The list of courses.
    """
    
    def __init__(self, student_file='data/students.json', course_file='data/courses.json'):
        self.student_list = []
        self.course_list = []
        self.student_file = student_file
        self.course_file = course_file
        self.load_data()
    
    def add_student(self, email, names):
        """
        Add a new student to the grade book.
        
        Args:
            email (str): The email of the student.
            names (str): The name of the student.
        """
        student = Student(email, names)
        self.student_list.append(student)
        self.save_data()
    
    def add_course(self, name, trimester, credits):
        """
        Add a new course to the grade book.
        
        Args:
            name (str): The name of the course.
            trimester (str): The trimester of the course.
            credits (int): The number of credits of the course.
        """
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_data()
    
    def register_student_for_course(self, student_email, course_name, grade):
        """
        Register a student for a course with the given grade.
        
        Args:
            student_email (str): The email of the student.
            course_name (str): The name of the course.
            grade (float): The grade obtained in the course.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        
        if student and course:
            student.register_for_course(course, grade)
            self.save_data()
        else:
            print("Student or course not found.")
    
    def calculate_GPA(self):
        """
        Calculate the GPA for all students.
        """
        for student in self.student_list:
            student.calculate_GPA()
    
    def calculate_ranking(self):
        """
        Calculate and return the ranking of students based on GPA.
        
        Returns:
            list: The list of students sorted by GPA in descending order.
        """
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
    
    def search_by_grade(self, min_grade, max_grade):
        """
        Search for students within a specified GPA range.
        
        Args:
            min_grade (float): The minimum GPA.
            max_grade (float): The maximum GPA.
        
        Returns:
            list: The list of students whose GPA falls within the specified range.
        """
        return [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
    
    def generate_transcript(self, student_email):
        """
        Generate the transcript for a specific student.
        
        Args:
            student_email (str): The email of the student.
        
        Returns:
            dict: The transcript of the student.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            return {
                'email': student.email,
                'names': student.names,
                'GPA': student.GPA,
                'courses': [{'course': {'name': c['course'].name, 'trimester': c['course'].trimester, 'credits': c['course'].credits},
                             'grade': c['grade'], 'credits': c['credits']} for c in student.courses_registered]
            }
        return None

    def save_data(self):
        """
        Save students and courses to JSON files.
        """
        students_data = [{'email': student.email, 'names': student.names, 'GPA': student.GPA,
                          'courses_registered': [{'course': {'name': c['course'].name, 'trimester': c['course'].trimester, 'credits': c['course'].credits},
                                                 'grade': c['grade'], 'credits': c['credits']} for c in student.courses_registered]} for student in self.student_list]
        courses_data = [{'name': course.name, 'trimester': course.trimester, 'credits': course.credits} for course in self.course_list]
        
        with open(self.student_file, 'w') as f:
            json.dump(students_data, f, indent=4)
        
        with open(self.course_file, 'w') as f:
            json.dump(courses_data, f, indent=4)
    
    def load_data(self):
        """
        Load students and courses from JSON files.
        """
        try:
            with open(self.student_file, 'r') as f:
                students_data = json.load(f)
                for s in students_data:
                    student = Student(s['email'], s['names'])
                    student.GPA = s['GPA']
                    student.courses_registered = [{'course': Course(c['course']['name'], c['course']['trimester'], c['course']['credits']),
                                                   'grade': c['grade'], 'credits': c['credits']} for c in s['courses_registered']]
                    self.student_list.append(student)
            
            with open(self.course_file, 'r') as f:
                courses_data = json.load(f)
                for c in courses_data:
                    course = Course(c['name'], c['trimester'], c['credits'])
                    self.course_list.append(course)
        except FileNotFoundError:
            # If the files do not exist, no data will be loaded.
            pass
    
    def remove_student(self, student_email):
        """
        Remove a student from the grade book.
        
        Args:
            student_email (str): The email of the student to remove.
        """
        self.student_list = [student for student in self.student_list if student.email != student_email]
        self.save_data()

    def remove_course(self, course_name):
        """
        Remove a course from the grade book.
        
        Args:
            course_name (str): The name of the course to remove.
        """
        self.course_list = [course for course in self.course_list if course.name != course_name]
        self.save_data()

    def record_drop_out_or_withdraw(self, student_email):
        """
        Record that a student has dropped out or withdrawn from the trimester.
        
        Args:
            student_email (str): The email of the student.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            # Generate the withdrawal statement
            print(f"Name - {student.names}")
            print(f"Email - {student.email}")
            print("The above mentioned student has withdrawn or dropped out of this trimester.")
        else:
            print("Student not found.")

