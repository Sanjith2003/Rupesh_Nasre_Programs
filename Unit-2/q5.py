n = int(input("Enter a number: "))

def isPrime(i):
    if i == 1:
        return False
    for j in range(2,int(i**0.5)+1): #note that checking till sqrt(i) is enough.
        if i % j == 0:
            return False
    else:
        return True

for i in range(2,n+1):
    if isPrime(i) == True:
        print(i)