"""
Module: student.py
Description: Defines the Student class.
"""

class Student:
    """
    Represents a student with email, names, and GPA.
    
    Attributes:
        email (str): The email of the student.
        names (str): The names of the student.
        GPA (float): The GPA of the student.
        courses_registered (list): The list of courses the student is registered in.
    """
    
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.GPA = 0.0
        self.courses_registered = []
        self.status = "Active"
    
    def register_for_course(self, course, grade):
        """
        Register the student for a course with the given grade.
        
        Args:
            course (Course): The course to register in.
            grade (float): The grade obtained in the course.
        """
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})
        self.calculate_GPA()
    
    def calculate_GPA(self):
        """
        Calculate the GPA of the student.
        """
        total_grade_points = sum(c['grade'] * c['credits'] for c in self.courses_registered)
        total_credits = sum(c['credits'] for c in self.courses_registered)
        if total_credits > 0:
            self.GPA = round(total_grade_points / total_credits, 2)
        else:
            self.GPA = 0.0
