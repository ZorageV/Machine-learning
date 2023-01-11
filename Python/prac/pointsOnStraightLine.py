x,y = (input("enter the two values")).split()
x1 = float(x)
y1 = float(y)
print(x1,y1)

x,y = (input("enter the two values")).split()
x2 = float(x)
y2 = float(y)
print(x2,y2)

x,y = (input("enter the two values")).split()
x3 = float(x)
y3 = float(y)
print(x3,y3)

m1 = (x2-x1)/(y2-y1)
m2 = (x3-x2)/(y3-y2)
if m1==m2:
    print("The points lie on staight line")
else:
    print("Not on straight line")
