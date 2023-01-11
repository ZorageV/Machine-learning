number = int(input("ENTER THE NUBMER:"))
n = number 
i = 1 
while(number>0):
    i = i*number
    number -= 1
print("the factorial of {} is {}".format(n,i))
