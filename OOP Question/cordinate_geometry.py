'''
Write OOP classes to handle the following scenarios:
A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line

'''

class point:

    # This is parameterised Construtor
    def __init__(self,x,y): 
        self.x_cod = x
        self.y_cod = y
    
    # A user can create and view 2D coordinates.
    def __str__(self):
        return '<{},{}>'.format(self.x_cod, self.y_cod)
    
    # A user can find out the distance between 2 coordinates.
    def enclidean_distance(self, other): # (self is x1, y1) and (other is x2, y2)
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    # A user can find the distance of a coordinates from origin
    def distance_from_origin(self):
        return self.enclidean_distance(point(0,0))
    
    # A user can check if a point lies on a given line
    # can define the user (Ax + Bx + c)


class line:
    
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C    

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)

    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lie on the line"

    
    



l1 = line(1,1,-2)
p1 = point(1,1)

print(l1)
print(p1)

print(l1.point_on_line(p1))