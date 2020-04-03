#This a package of mensuration
#It contains classes like circle,
#rectangle, square and triangle etc.
#does all the mathematical opertaions

class Circle():

    Pi = 3.141

    def __init__(self, radius = 1):
        self.radius = radius

    #rest of the methods of the class
    def get_radius(self):
        return self.radius
    def area(self):
        return Circle.Pi * self.radius * self.radius

    def circumference(self):
        return 2 * Circle.Pi * self.radius

#end of Circle
class Rectangle():

    def __init__(self, length = 1, breadth = 1):
        self.length = length
        self.breadth = breadth

    def get_length(self):
        return self.length

    def get_breadth(self):
        return self.breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 *(self.length + self.breadth)

#end of Rectangle
class Square(Rectangle):

    def __init__(self,side = 1):
                
