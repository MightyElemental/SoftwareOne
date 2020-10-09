import graphics
import random, math

seed = 154
tree_definition = []

def tendToStart(start, end):
    base = abs(random.random() - random.random())
    return (end-start)*base+start

def tendToEnd(start, end):
    base = 1-abs(random.random() - random.random())
    return (end-start)*base+start


class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args)==0: self.values = (0,0)
        else: self.values = args
        
    def norm(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum( comp**2 for comp in self ))
        
    def argument(self):
        """ Returns the argument of the vector, the angle clockwise from +y."""
        arg_in_rad = math.acos(Vector(0,1)*self/self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0]<0: return 360 - arg_in_deg
        else: return arg_in_deg

    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.norm()
        normed = tuple( comp/norm for comp in self )
        return Vector(*normed)

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple( a * other for a in self )
            return Vector(*product)
    
    def __rmul__(self, other):
        """ Called if 4*self for instance """
        return self.__mul__(other)
            
    def __div__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple( a / other for a in self )
            return Vector(*divided)
    
    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple( a + b for a, b in zip(self, other) )
        return Vector(*added)
    
    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple( a - b for a, b in zip(self, other) )
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __repr__(self):
        return str(self.values)

    def toPoint(self):
        return graphics.Point(self.values[0]+500, 450-self.values[1])

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getPointOnLine(self, scalar):
        return (self.end-self.start)*scalar+self.start


def main():
    win = graphics.GraphWin("My Circle", 1000, 500)
    for obj in tree_definition:
        graphics.Line(obj.start.toPoint(), obj.end.toPoint()).draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done



def generateTree(seed):
    print("Generating tree with seed", seed)
    random.seed(seed)
    # Create base line for tree
    base_line = Line(Vector(0,0), Vector(0, tendToEnd(80,105)))
    tree_definition.append(base_line)
    off_shoots = int(tendToEnd(4,8))
    for i in range(off_shoots):
        ponline = base_line.getPointOnLine(tendToEnd(0.3,1))
        shift = Vector(random.randrange(-40,40), random.randrange(-10,40))
        # add random direction and random length rather than random point
        new_branch = Line(ponline, ponline + shift)
        tree_definition.append(new_branch)

generateTree(420)
main()