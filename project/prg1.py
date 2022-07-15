import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from moduleA import Rectangle


rect1 = Rectangle(10, 20)
rect2 = Rectangle(30, 40)

objects = [rect1, rect2]

for obj in objects:
    obj.get_area()
