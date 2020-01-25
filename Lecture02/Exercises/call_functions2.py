import functions2 as f
from numpy import *

x = r_[-10:10]/3.0
y1 = f.sinc(x)
y2 = f.step(x)

print("x: ", x)
print("y1: ", y1)
print("y2: ", y2)
