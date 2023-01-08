import math

a = int(input("enter the first side = "))
b = int(input("enter the second side = "))
c = int(input("enter the third side = "))
#nt(dir(math))
A = (b*b + c*c - a*a)/(2*c*b)
angle_a = math.acos(A)
print("the angle A in degrees is = ",180*angle_a/math.pi)

B = (a*a + c*c - b*b)/(2*a*c)
angle_b = math.acos(B)
print("the angle B in degrees is = ",180*angle_b/math.pi)

C = (b*b + a*a - c*c)/(2*a*b)
angle_c = math.acos(C)
print("the angle C in degrees is = ",180*angle_b/math.pi)
