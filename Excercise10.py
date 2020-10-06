#Exercise 10
#Delete the name property of the employee1 object
#Delete the employee2 object as a whole


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

emp1 = Employee("Sam", 36)
emp2 = Employee("Mark", 28)

# YOUR CODE HERE
print(emp1.name)
print(emp2)

del emp1.name
del emp2

print(emp1.name)
print(emp2)