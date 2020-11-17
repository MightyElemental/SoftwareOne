# WEEK 7 – PRACTICAL 6

class Vector:
    def __init__(self, *data):
        self._vector = []
        if len(data)>0:
            if type(data[0]) is int:
                self._vector = [float(x) for x in data]
            elif type(data[0]) is list:
                self._vector = [float(x) for x in data[0]]

    def __str__(self):
        return f"<{', '.join(str(x) for x in self._vector)}>"

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]
    
    def set(self, index, value):
        self._vector[index] = value

    def scalar_product(self, scalar):
        result = Vector([scalar*x for x in self._vector])
        return result

    def add(self, vector):
        if(not isinstance(vector, Vector)): raise TypeError()
        if(vector.dim() != self.dim()): raise ValueError()
        return Vector([self._vector[i]+vector._vector[i] for i in range(self.dim())])

    def equals(self, vector):
        if(not isinstance(vector, Vector)): return False
        return self._vector == vector._vector

    def __eq__(self, vector):
        return self.equals(vector)

    def __ne__(self, vector):
        return not self.equals(vector)

    def __add__(self, vector):
        return self.add(vector)

    def __iadd__(self, vector):
        if(not isinstance(vector, Vector)): raise TypeError()
        if(vector.dim() != self.dim()): raise ValueError()
        self._vector = [self._vector[i]+vector._vector[i] for i in range(self.dim())]
        return self

    def __rmul__(self, scalar):
        return self.scalar_product(scalar)

    def __imul__(self, scalar):
        if(not isinstance(scalar, (float,int))): raise TypeError
        self._vector = [scalar*x for x in self._vector]
        return self

    def __getitem__(self, index):
        return self._vector[index]

    def __setitem__(self, index, value):
        self.set(index,value)