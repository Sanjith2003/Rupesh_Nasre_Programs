from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if 'mode' in request.GET:
        mode = request.GET['mode']
    else:
        mode = 'home'

    folder = '/home/rupesh/mydjango/myweb/'
    header = 'header.html'
    footer = 'footer.html'
    filename = folder + mode + '.html'

    htmlstr = ''
    fp = open(folder + header) # display header
    htmlstr = htmlstr + fp.read()
    fp.close()

    # Menu items
    menu_items = ['Home', 'Academics', 'Projects', 'Contact']

    # Display menu
    htmlstr += '<div id="menu">'
    for item in menu_items:
        if item.lower() == mode:
            htmlstr += item
        else:
            htmlstr += '<a href="?mode=' + item.lower() + '">' + item + '</a>'
        htmlstr += ' || '
    htmlstr += '</div>'

    fp = open(filename) # display mode file
    htmlstr = htmlstr + fp.read()
    fp.close()

    fp = open(folder + footer) # display footer
    htmlstr = htmlstr + fp.read()
    fp.close()

    return HttpResponse(htmlstr)
