#Write a python program that have a class named point.
#This class should have a method that can calculate the distance between two
#points. The methods should be called by a class.

class point():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    def calculate_distance(self):
        dist = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print("Distance between TWO points:")
        print(dist)

p1 = point()
p1.x1 = 2
p1.x2 = 3

p1.y1 = 5
p1.y2 = 8

p1.calculate_distance()
