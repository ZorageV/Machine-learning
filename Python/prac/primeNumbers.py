primeList = [2]

for i in range(2,101):
    residue = 1
    for j in primeList:
        residue = i%j
        if(residue==0):
            break
    if(residue!=0):
        primeList.append(i)
#primes = set(primeList)
print(f"List of primes = {primeList}")