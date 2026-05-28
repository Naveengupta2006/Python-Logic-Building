"""
TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public.
An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""

class instructor:

    def __init__(self):

        self.__name = ""
        self.__technology_skill = []
        self.__experience = 0
        self.__avg_feedback = 0.0

    # setter

    def set_name(self, name):
        self.__name = name 

    def set_technology_skill(self, technology):
        self.__technology_skill = technology
    
    def set_experience(self, experience):
        self.__experience = experience
    
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    
    # getter

    def get_name(self):
        return self.__name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience
    
    def get_avg_feedback(self):
        return self.__avg_feedback

    
    # method 1:
    def check_eligibility(self):
        """
        Returns True if:
          - experience > 3 years  AND  avg_feedback >= 4.5
          - experience <= 3 years AND  avg_feedback >= 4.0
        """
        if self.__experience > 3:
            return self.__avg_feedback >= 4.5
        
        else:
            return self.__avg_feedback >= 4.0
    
    # method 2:
    def allocate_course(self, technology):
        """
        Returns True if:
          1. Instructor is eligible
          2. Instructor has the required technology skill
        """
        if not self.check_eligibility():
            return False
        return technology.lower() in [s.lower() for s in self.__technology_skill]
    

    def display(self):
        print(f"  Name            : {self.__name}")
        print(f"  Skills          : {', '.join(self.__technology_skill)}")
        print(f"  Experience      : {self.__experience} years")
        print(f"  Avg Feedback    : {self.__avg_feedback}")
        print(f"  Eligible        : {'Yes' if self.check_eligibility() else 'No'}")

    #  TEST — Creating Instructor Objects

def test_allocation(instructor, course):
    result = instructor.allocate_course(course)
    status = " ALLOCATED" if result else " NOT ALLOCATED"
    print(f"  Course [{course}] → {status}")

sep = "=" * 45


if __name__ == "__main__":
    # ── Instructor 1
    i1 = instructor()
    i1.set_name("Alice")
    i1.set_technology_skill(["Python", "Machine Learning", "SQL"])
    i1.set_experience(5)
    i1.set_avg_feedback(4.7)

    print(sep)
    print("  INSTRUCTOR 1")
    print(sep)
    i1.display()
    print()
    test_allocation(i1, "Python")
    test_allocation(i1, "Java")         # skill missing
    print()

