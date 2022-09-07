from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random
import time
import datetime

root = Tk()

path = 'members.txt'
index = 0
target = 100
now = StringVar()

members = []
labels = []
scores = []
texts = []
records = []

def lottery():
	random.seed()
	
	slow = False
	end = False
	while end != True:
		num = random.randint(0, index - 1)
		records.append(str(num))
		
		print(num, end=" ")
		scores[num] = scores[num] + 1
		
		texts[num].set("{} {} : {}/{}".format(num, members[num], scores[num], target))
		now.set(num)
		
		if scores[num] == target:
			end = True
		elif scores[num] >= target - 3:
		    slow = True

		root.update()

		if slow == True:
		    time.sleep(0.5)

	out = "{}.txt".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
	with open(out, "w", encoding="utf-8") as f:
		for r in records:
			f.write(r + " ")


with open(path, "r", encoding="utf-8") as f:
	for i in f:
		members.append(i.rstrip('\n'))
		index = index + 1
	print(members)

print("index={}".format(index))

root.title('Lottery')

frame1 = ttk.Frame(root)

my_font = font.Font(root, family="System", size=32, weight="bold")

i = 0
for m in members:
	scores.append(0)
	texts.append(StringVar())
	texts[i].set("{} {} : {}/{}".format(i, m, scores[i], target))

	labels.append(ttk.Label(frame1, textvariable=texts[i], font=my_font))

	i = i + 1

blink = ttk.Label(frame1, textvariable=now, font=my_font)
button = ttk.Button(frame1, text='Start', command=lottery)

frame1.grid(row=0,column=0,sticky=(N,E,S,W))

i = 0
for l in labels:
	l.grid(row=i, column=0, sticky=W)
	i = i + 1

button.grid(row=i,column=0, sticky=W)
blink.grid(row=i, column=1)

for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
