import math


x,y = input("enter the coordfiantes of center of circle").split()
x1 = float(x)
y1 = float(y)
radius = float(input("Enter the radius of circle"))

x,y = input("enter the coordfiantes of points").split()
x2 = float(x)
y2 = float(y)

#equation of circle
circle = (x1-x2)**2 + (y1-y2)**2 - radius**2

#check position of point
if circle==0:
    print("on circle")
elif circle>0:
    print("outside")
else:
    print("Inside")
