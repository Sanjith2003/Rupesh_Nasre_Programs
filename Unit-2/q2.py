x = int(input("Enter x in x**n: "))
n = int(input("Enter power n: "))
pow = 1
for i in range(n):
    pow = pow * x
print(x,"**",n,"=",pow)
