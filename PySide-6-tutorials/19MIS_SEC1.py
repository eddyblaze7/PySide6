# This is part one
#SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object


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

        
    
Person1 = PERSON("Edmund", "Amarh", 28)
Person2 = PERSON("Mary","Lamptey", 25)
# print(Person1.firstName)
# print(Person1.lastName)
# print(Person1.age)

print(Person1.full_name())
print(Person1.name_initials())
print(Person2.full_name())
print(Person2.email)