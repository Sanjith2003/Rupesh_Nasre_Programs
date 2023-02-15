n = int(input("Enter number of friends: "))
d = {}
for i in range(n):
    name = input("Enter name: ")
    state = input("Enter state: ")
    d[name] = state

for i in d:
    if d[i] == "Telangana":
        print(i)
