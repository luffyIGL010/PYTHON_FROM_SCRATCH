class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        
        
    def sum(self,p):
        return Vector((self.x+p.x),(self.y+p.y))
    
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")
        
p1=Vector(4,5)
p2=Vector(5,4)

p=p1.sum(p2)

p.print_point()