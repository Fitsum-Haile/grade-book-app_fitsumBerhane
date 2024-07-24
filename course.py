"""
Module: course.py
Description: Defines the Course class.
"""

class Course:
    """
    Represents a course with its name, trimester, and credits.
    
    Attributes:
        name (str): The name of the course.
        trimester (str): The trimester the course is offered.
        credits (int): The number of credits the course is worth.
    """
    
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
"""
Module: course.py
Description: Defines the Course class.
"""

class Course:
    """
    Represents a course with a name, trimester, and credits.
    
    Attributes:
        name (str): The name of the course.
        trimester (str): The trimester the course is offered in.
        credits (int): The number of credits the course is worth.
    """
    
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
