class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

x = 7
y = 8
w1 = Weird(x,y)
#print(w1.getY())

w2 = Wild(x,y)
#print(w2.getY())
w3 = Wild(17,18)
#print(w3.getY())
w4 = Wild(x, 18)
X = w4.getX() + w3.getX() + w2.getX()
#print(X)
print(w4.getX())



