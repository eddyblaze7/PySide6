
"""
4. Write a add_course, drop_course, print_all_courses method to mimic 
a real-world use-case of activities of adding a course, 
deleting a course and printing registered courses respectively
a student will perform on the Student MIS 

"""

class PERSON:
    def __init__(self, firstName, lastName, age):
        self.firstName =firstName
        self.lastName =lastName
        self.age = age 
        #self.email = f"{firstName[0]}".upper()+ "."+"{lastName}.pentvars.edu.gh".lower()" # will have to work on joining upper and lower cases
        self.email = f"{firstName[0]}.{lastName}.pentvars.edu.gh".lower()

    def full_name(self):
        return f"{self.firstName} {self.lastName}"
    
    def name_initials(self):
        return f"{self.firstName[0]} {self.lastName[0]}"

        
class Student(PERSON):
    def __init__(self, firstName, lastName, age, hall, courses=None):
        super().__init__(firstName, lastName, age)
        self.hall = hall


        if courses is None:
            self.courses= []
        else:
            self.courses = courses

    #a method to add courses of the students
    # def add_course(self, course_item):
    #     if course_item not in self.courses:
    #         self.courses.append(course_item)
    def add_course(self, course_title):
        if course_title not in self.courses:
        #we have to write a logic to ensure that a course is not
        #registered twice or more by a student
            self.courses.append(course_title)

    def drop_course(self, course_title):
        #we have to write a logic to ensure that a course is dropped
        #by a student
        if course_title in self.courses:
            self.courses.remove(course_title)

    def print_all_courses(self):
        #using the for loop to position the courses in a presentable way
        print(f"{self.full_name()} has registered {len(self.courses)} courses")
        print("_" *40)
        for course in self.courses:
            print(course)

Student1 = Student("Joana", "Jones", 19, "Mensah Sabbah")
Student1.add_course("Python")  # adds python [Python]
Student1.add_course("Calculus") # adds Calculus to the list [Python, Calculus]
Student1.add_course("Calculus") # it elminates calculus because they already exist
Student1.add_course("Python") # it eliminates python because they already exist
Student1.add_course("African Studies")
Student1.add_course("Project Work")
#Student1.drop_course("Python")
#print(Student1.courses)

Student1.print_all_courses()