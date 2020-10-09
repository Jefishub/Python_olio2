# base class, parent class, superclass,  yläluokka
class Person:
    def __init__(self, fname:str, lname:str):
        self.firstname = fname
        self.lastname = lname

    def printname(self) -> None:
        print(f'My name is {self.firstname}  {self.lastname}')

    def hello(self):
        print("Hello from Student")

person1 = Person(fname='John', lname='Doe')
#person1.printname()

# Child class, aliluokka
# Opiskelija
# Derived class inherits features from the base class 
# We want to add the __init__() function to the child class (instead of the pass keyword).
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# Python also has a super() function 
# that will make the child class inherit all the methods and properties from its parent:
# studentnumber
#school
# starting_year
# GPA
# department

class Teacher(Person):
    def __init__(self, fname:str, lname:str, salary:int):
        super().__init__(fname, lname)
        self.salary = salary
#teacher1 = Teacher('Matti', 'Korhonen', '500')
#print(teacher1.salary)

class Student(Person):
    def __init__(self, fname:str, lname:str, student_number:str, school:str, gpa:float, starting_year:str, graduationyear=None):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.student_number= student_number
        self.school = school
        self.gpa = gpa
        self.starting_year = starting_year
        self.graduationyear = graduationyear

    #Ylikirjoitetaan Student -luokan metodi hello()
    def hello(self):
        print("Hello from Student")

    def greet(self):
        print(f"Welcome {self.firstname} {self.lastname}")   

    def welcome(self):
        print('Welcome', self.firstname, self.lastname, 'to the class of ', self.graduationyear)

    def study_years(self):
        return int(self.graduationyear) - int(self.starting_year)

    def is_graduated(self):
        if self.graduationyear:
            return True
        else:
            return False

    def print_gpa(self):
        print(f"{self.firstname} {self.lastname} your gpa is: {self.gpa}")

    def __str__(self):
        return f'Student name: {self.firstname} {self.lastname}\
               \nStudent numer: {self.student_number}\nSchool: {self.school}\
               \nGPA: {self.gpa} \nStarting year: {self.starting_year} \nGraduation year: {self.graduationyear}'

student1 = Student(fname='Mike', lname='Olsen', student_number= '5577754', school='Taitotalo', gpa=4.7, starting_year= '2019',  graduationyear='2020')
student1.printname()
print(student1.graduationyear)
print(student1.student_number)
student1.welcome()
person1.printname()
student1.greet()
print(student1.study_years())
print(student1)
