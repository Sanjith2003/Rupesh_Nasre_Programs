import re

filename = input("Enter file name: ")
pattern = input("Enter pattern: ")
with open(filename, 'r') as f:
    for line in f:
        if re.search(pattern, line):
            print(line)
