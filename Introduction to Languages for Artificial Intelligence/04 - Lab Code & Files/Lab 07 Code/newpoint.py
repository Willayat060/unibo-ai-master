class Point:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def whoareyou (self):
        return self.x,self.y
    def move(self,delta):
        self.x+=delta
        self.y+=delta
    def __str__(self):
        return "P("+str(self.x)+","+str(self.y)+")"

class NewPoint(Point):
    def origin(self):
        self.x,self.y=0,0 

p = NewPoint(1,2)  #__init__ in NewPoint not found, so that of Point is called
print(p)   #__str__ is inherited (try: define it in NewPoint only, or add one in NewPoint)
print(isinstance(p,Point)) # True