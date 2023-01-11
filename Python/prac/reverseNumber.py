number = int(input("Enter the number:"))

# reversing the number
reverse = 0 
while(number>0):
    reverse = number%10 +reverse*10
    number = int(number/10)
print(reverse)   