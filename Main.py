import tkinter as tk
import json
from tkinter import messagebox as mb
import random


class tips:
    def __init__(self, category, text):
        self.category = category
        self.text = text

        



match_text = '-----'

with open('C:\Workspace\Experiment\Reminder\Tips.txt') as file:
    lines = file.readlines()



category=''
tipLines=''


tipsList =[]

for line in lines:
    if(category=='' and not(line.__contains__(match_text))):
        category = line
        continue

    if(line.__contains__(match_text) and category != ''):
        temp ={}
        temp['category'] = category
        temp['lines'] = tipLines
        tipsList.append(temp)
        category=''
        tipLines=''
        continue

    if(category!='' and line!= ''):
        tipLines = tipLines + line
        continue

temp ={}
temp['category'] = category
temp['lines'] = tipLines
tipsList.append(temp)

random.shuffle(tipsList)

file = open('C:\Workspace\Experiment\Reminder\json.txt', 'w')

file.write(json.dumps(tipsList))

file.close()

