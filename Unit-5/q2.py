from django.shortcuts import render
from django.http import HttpResponse
from .academics import *

def processAcads(filename, rollno):
    htmlstr = f'<h2>Academic performance of Roll No. {rollno}</h2>'
    htmlstr += '<table border=1>\n'
    acadfile = open(f'{filename}.{rollno}')
    
    for line in acadfile:
        if line == '\n': # new semester
            htmlstr += gethtml()
            htmlstr += f'<tr><td colspan=3>This Sem CGPA: {cgpa():.2f}</td></tr>\n'
        else:
            cc, cr, ea = line.split()
            add(cc, int(cr), int(ea))
    
    acadfile.close()
    htmlstr += '</table><br>\n'
    return htmlstr

def index(request):
    rollno = request.GET.get('rollno', 'unknown')
    filename = '/home/rupesh/mydjango/acads/academics.txt'
    htmlstr = processAcads(filename, rollno)
    return HttpResponse(htmlstr)
