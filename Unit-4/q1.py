import sys
from academics import *

if len(sys.argv) < 2:
    print("Usage: python academic_records.py <student_file_1> [<student_file_2> ...]")
    sys.exit(1)

for student_file in sys.argv[1:]:
    with open(student_file) as acadfile:
        for line in acadfile:
            if line == '\n':
                # end of semester
                cprint()
                print("This Sem CGPA:", cgpa(), "\n")
            else:
                cc, cr, ea = line.split()
                add(cc, int(cr), int(ea))

    print(f"Student record for {student_file} processed.\n")
