import re

text = "My departmental email id is rupesh@cse.iitm.ac.in. This is what I use for all the official purposes. The institute also provides an id rupesh@iitm.ac.in. During PhD, I used to have a personal email id rupesh0something@gmail.com, which is still in use. When gmail was not around, id rupesh_something@usa.net was the one I used. I also own a twitter handle @rupeshsomething, which I hardly use. That's it from my side for now. See you in class @11."

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b(?!\.\w{2,})'
emails = re.findall(regex, text)
print(emails)
