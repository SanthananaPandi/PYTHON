# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:24:35 2024

@author: santh
"""

# Assuming A2nos from pgm422 looks something like this:
class A2nos:
    def __init__(self, x, y):
        self._x = x  # Protected attribute so it can be accessed in subclasses
        self._y = y

    def display(self):
        # Print values directly
        print(self._x, self._y)

class point(A2nos):
    
    def __init__(self, x=10, y=20):
        # Initialize parent class (A2nos) with x and y values
        super().__init__(x, y)
        
    def display(self):
        # Display the values of _x and _y from the superclass
        print(self._x, self._y)
    
# main
c = point()  # Uses default values (x=10, y=20)
c.display()

d = point(15)  # Uses x=15, default y=20
d.display()

e = point(150, 100)  # Uses x=150, y=100
e.display()

f = point(y=1000)  # Uses default x=10, y=1000
f.display()

g = point(y=500, x=800)  # Uses x=800, y=500
g.display()
