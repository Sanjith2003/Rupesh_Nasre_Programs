l = eval(input("Enter a list: "))
max1 = max2 = l[0] #let max and second max be the first element

for i in l:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i

print("Second Maximum: ",max2)
    