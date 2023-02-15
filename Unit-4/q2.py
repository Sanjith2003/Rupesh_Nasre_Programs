phones = {} # name is the key
githubs = {} # name is the key
ages = {} # name is the key
datafile = "friends.txt"

def add(name, phone, github, age):
    phones[name] = phone
    githubs[name] = github
    ages[name] = age

def remove(name):
    del phones[name]
    del githubs[name]
    del ages[name]

def updatePhone(name, phone):
    phones[name] = phone

def updateGithub(name, github):
    githubs[name] = github

def updateAge(name, age):
    ages[name] = age

def get(name):
    return [name, phones[name], githubs[name], ages[name]]

def printOne(name, phone, github, age):
    print(name, phone, github, age)

def printOneList(npga):
    printOne(*npga)

def printByName(name):
    printOneList(get(name))

def printAll():
    for name in phones:
        printOneList(get(name))

def writeAll():
    global datafile

    df = open(datafile, 'w')
    for name in phones:
        print(name, phones[name], githubs[name], ages[name], file=df, sep='\t')
    df.close()

def readAll():
    phones = {}
    githubs = {}
    ages = {}
    global datafile
    df = open(datafile)
    line = df.readline()
    while not line == '':
        name, phone, github, age = line.strip().split('\t')
        add(name, phone, github, age)
        line = df.readline()
    df.close()
