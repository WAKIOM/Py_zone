#!/usr/bin/python3
"""Module contains one class"""


class Student:
    """
    class defines students admission,
    first name, last name and year of birth
    Two functions
    """
    def __init__(self, adm, first_name, last_name, yob):
        """ insantiating """
        self.adm = adm
        self.first_name = first_name
        self.last_name = last_name
        self.yob = yob

    def print_details(self):
        """ method takes the attributes and creates a dictionary
        out of them.
        returns the dictionary
        """
        if type(self.first_name) is not str:
            raise TypeError("first name must be a string")
        if type(self.last_name) is not str:
            raise TypeError("last name must be a string")
        if type(self.adm) is not int:
            raise TypeError("admission number must be an integer")
        if type(self.yob) is not int:
            raise TypeError("year of birth must be an integer")
        deets = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "admission-no": self.adm,
            "YOB": self.yob
        }
        return deets

 
student1 = Student(10309, "Jane", "Doe", 2004)
student2 = Student(10422, "James", "Joe", 2001)
student3 = Student(10688, "Carl", "Toes", 2002)
students = [student1, student2, student3]
for student in students:
    for key, value in student.print_details().items():
        print("{}: {}".format(key, value))
    print("#######")
