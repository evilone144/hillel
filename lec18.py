#!/usr/bin/python3
import requests
import sys
from datetime import datetime

#general vars and first arg
arg1 = sys.argv[1]
link = 'https://baconipsum.com/api/?type=meat-and-filler.'
word = 'pancetta'
r_file = 'result.txt'
name = 'Vlad'

#request text from given url
def get_text(url):
    r = requests.get(url)
    response = r.text
    return response

#saving text to var
text = get_text(link)

#split text based on '","' delimiter
s_text = text.split('\",\"')

#save needed amount of paragraps to var
final = s_text[0:int(arg1)]

#find how many needed words in paragrp.
def check(w):
    x = 0
    for i in final:
        y = i.split()
        if w in y:
            x += 1
    return x

#Adding new line character
def space():
    new_list = []
    for i in final:
        new_list.append(i)
        new_list.append("\n")
    return new_list


#Writing all info to file.
with open(r_file, "w") as f:
    f.write(name + "\n" + str(datetime.now()) + "\n" + "Amout of matches: " + str(check(word)) + "\n" + str(space()))
