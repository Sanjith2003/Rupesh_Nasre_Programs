def isPalindrome(bstring):
    bstring = ''.join(c for c in bstring if c.isalnum()).lower() # remove non-alphanumeric characters and convert to lowercase
    blen = len(bstring)
    first = bstring[:blen // 2] # integer division to get the index
    second = bstring[(blen + 1) // 2:]
    
    if first == second[::-1]: # extended range, for reversing
        return True
    
    return False

if isPalindrome("step on no pets!") == True:
    print(True)
else:
    print(False)
