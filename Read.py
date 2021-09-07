import json
from tkinter import messagebox as mb
import os
import time

lines = 'lines'

file = open('C:\Workspace\Experiment\Reminder\json.txt', 'rb+')
seenTips = open('C:\Workspace\Experiment\Reminder\seenTips.txt', 'rb+')

data = json.load(file)
file.close()

emptyFile = os.stat(
      'C:\Workspace\Experiment\Reminder\seenTips.txt').st_size == 0

sourceEmptyFile = os.stat(
       'C:\Workspace\Experiment\Reminder\json.txt').st_size == 0

if(emptyFile != True):
        seenData = json.load(seenTips)
else:
        seenData = []

if(sourceEmptyFile == True):
        file = open('C:\Workspace\Experiment\Reminder\json.txt', 'w')
        json.dump(seenData, file)
        file.close()

        seenData = []
        seenTips = open('C:\Workspace\Experiment\Reminder\seenTips.txt', 'w')
        seenTips.close()

tipsList = []

count = 0
tipsShownCount = 2

for i in data:
        print(type(i))
        mb.showinfo('Message', i['lines'])
        seenData.append(i)
        count += 1
        if(count == tipsShownCount):
            break

for i in range(0, count):
        text = data.pop(0)
        print(text)

seenTips = open('C:\Workspace\Experiment\Reminder\seenTips.txt', 'w')
json.dump(seenData, seenTips)

file = open('C:\Workspace\Experiment\Reminder\json.txt', 'w')
json.dump(data, file)

seenTips.close()
file.close()
