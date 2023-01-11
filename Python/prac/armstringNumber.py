number = int(input("Enter the number: "))
numberCopy = number
sum = 0
while(number>0):
    sum = sum + (number%10)**3
    number = int(number/10)

print(sum , numberCopy)

if sum==numberCopy:
    print("Armstrong")
else:
    print("Not Armstrong")