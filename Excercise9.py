#Exercise 9
#Implement the code to get the following output.
# OUTPUT -> (1, 2, 3)


class Point3D(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
# YOUR CODE HERE
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

my_point=Point3D(1,2,3)
print(my_point)