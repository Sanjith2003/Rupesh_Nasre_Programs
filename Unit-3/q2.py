courses = []
credits = []
earned = []
audit = []

def add(cc, cr, ea, is_audit=False):
    courses.append(cc)
    credits.append(cr)
    earned.append(ea)
    if is_audit:
        audit.append(len(courses) - 1)

def drop(cc):
    index = courses.index(cc)
    courses.pop(index)
    credits.pop(index)
    earned.pop(index)
    if index in audit:
        audit.remove(index)

def cprint():
    ii = 0
    print("course", "credits", "earned")
    for cc in courses:
        cr = credits[ii]
        ea = earned[ii]
        print(cc, cr, ea)
        ii = ii + 1
    print("Audit Courses:")
    for idx in audit:
        print(courses[idx], credits[idx], earned[idx])

def sgpa(courses_list):
    numerator = denominator = 0
    ii = 0
    for cc in courses_list:
        cr = credits[courses.index(cc)]
        ea = earned[courses.index(cc)]
        numerator = numerator + cr * ea
        denominator = denominator + cr
    return numerator / denominator

def cgpa():
    return sgpa(courses)

def sem_sgpa(sem_courses):
    return sgpa(sem_courses)

# main module begins
add("CS101", 4, 3, True)
add("CS102", 4, 2)
add("CS103", 3, 4)
add("CS104", 2, 2)
add("CS105", 3, 3)

cprint()

print("CGPA:", cgpa())
print("SGPA for Semester 2:", sem_sgpa(["CS102", "CS103", "CS104"]))
