# Inheritance and polymorphism
class Person:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def display(self):
        print(f'''First Name:{self.firstName}
Second Name:{self.lastName}''')
person1=Person('Elis','Kandel\n')
person1.display()
class Student(Person):
    def __init__(self,firstName,lastName,graduationYear):
        super().__init__(firstName,lastName)
        self.graduationYear=graduationYear
    def display(self):
        super().display()
        print(f'''Graduation Year: {self.graduationYear}''')
student1= Student("Elis","Kandel",2077)
student1.display()