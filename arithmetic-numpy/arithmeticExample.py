import numpy as np


class ArithExample:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_operation(self):
        print("Add operator", self.a + 2)

    def add_function(self):
        print("Add function ", np.add(self.a, self.b))


aa = np.array([10,20,30])
bb = np.array([1,2,3])
a = ArithExample(aa,bb)
a.add_operation()
a.add_function()
