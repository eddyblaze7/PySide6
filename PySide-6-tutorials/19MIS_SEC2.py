# SECTION TWO
# 1. Define a class Student which inherites from the Person class
# 2. Define extra attributes for student, such as hall of residence and courses
# 3. Create a student object from the Student class

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
        if courses == None:
            self.courses= []
        self.courses = courses
    
    pass

Student1 = Student("Bernard", "Amarh", 23, "James Mckeown", "Python")
print(Student1.full_name())
print(Student1.name_initials())
print(Student1.email)
print(Student1.hall)
print(Student1.courses)

