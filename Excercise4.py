#Exercise 4
#Korja alla oleva koodi. (note. On hyvin epäselvästi määritetty mitä pitää korjata)
"""
class MyClass
    variable = blah
def function():
    print("This is a message inside the class.")
myobjectx = MyClass
myobjectx.variable()
"""


class MyClass:
    variable = "blah"
    #def __init__(self):
    #   self.variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
print(myobjectx.variable)