class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        pass

    def check_angles(self):
        pass

class Equilateral(Triangle):
    def __init__(self):
        pass
    
#######################################
my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
my_equilateral = Equilateral()
print(my_equilateral.angle)
print(my_equilateral.angle1)
