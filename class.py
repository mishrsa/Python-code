from tokenize import cookie_re

class Coordinate (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance (self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.x-other.x)** 2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x-other.x, self.y - other.y)
c = Coordinate(3,4)
origin = Coordinate (0,0)
#bar = c - origin
#print(bar)

#print(c.x)
#print(c.y)
print(c.distance(origin))
print (Coordinate.distance(c,origin))
print (25)
'''
both sentence are same
'''
#print(Coordinate.distance(c, origin))
#print(c)
#print(type(c))
#print(isinstance(c, Coordinate))


#class clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self):
#           time = '06:30'
#           print(self.time)
#clock = clock('5:30')
#print(clock.print_time())
#class Weird(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return x
#    def getY(self):
#        return y

#class Wild(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return self.x 
#    def getY(self):
#        return self.y

#X = 7
#Y = 8
#w1= Weird(X,Y)
#print(w1.getX())