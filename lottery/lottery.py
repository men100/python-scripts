from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random
import time
import datetime

root = Tk()

path = 'members.txt'
index = 0
target = 50
now = StringVar()
seedOption = StringVar()
manualSeed = StringVar()
striked = 0

members = []
labels = []
scores = []
texts = []
records = []

def lottery():
	resetButton['state'] = 'disable'

	startTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	if seedOption.get() == 'Auto':
		seed = startTime
	else:
		seed = manualSeed.get()
	print('seed=' + seed)
	random.seed(seed)
	
	slow = False
	end = False
	while end != True:
		num = random.randint(0, index - 1)
		records.append(str(num + 1))
		
		print(num, end=" ")
		scores[num] = scores[num] + 1
		
		texts[num].set("{:2} {} : {:2}/{}".format(num + 1, members[num], scores[num], target))
		if scores[num] >= target:
			labels[num]['background'] = 'black'
		if scores[num] >= target - 3:
			labels[num]['foreground'] = 'red'
		
		now.set("{:2}".format(num + 1))
		
		if scores[num] == target:
			end = True
			striked = num
		elif scores[num] >= target - 3:
			slow = True

		root.update()

		if slow == True:
			time.sleep(0.5)
		else:
			time.sleep(0.003)

	out = "lottery_{}.txt".format(startTime)
	with open(out, "w", encoding="utf-8") as f:
		f.write('seed=' + seed + '\n')
		f.write('number=')
		for r in records:
			f.write(r + ' ')
		f.write('\n')
		f.write('striked=' + str(striked + 1) + ' ' + members[striked] + '\n')

def reset():
	i = 0
	for m in members:
		scores[i] = 0
		texts[i].set("{:2} {} : {:2}/{}".format(i + 1, m, scores[i], target))
		labels[i]['foreground'] = 'black'
		labels[i]['background'] = ''
		i = i + 1

def changeSeedOption():
	if seedOption.get() == 'Auto':
		textBox['state'] = 'disable'
	else:
		textBox['state'] = 'enable'

if __name__ == '__main__':

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
		texts[i].set("{:2} {} : {:2}/{}".format(i + 1, m, scores[i], target))

		labels.append(ttk.Label(frame1, textvariable=texts[i], font=my_font))

		i = i + 1

	startButton = ttk.Button(frame1, text='Start', command=lottery)
	resetButton = ttk.Button(frame1, text='Reset', command=reset)
	seedLabel = ttk.Label(frame1, text='Seed')
	radioButton1 = ttk.Radiobutton(frame1, text='Auto', value='Auto', variable=seedOption, command=changeSeedOption)
	radioButton2 = ttk.Radiobutton(frame1, text='Manual', value='Manual', variable=seedOption,  command=changeSeedOption)
	textBox = ttk.Entry(frame1, textvariable=manualSeed, width=20, state='disable')
	blink = ttk.Label(frame1, textvariable=now, font=my_font)

	frame1.grid(row=0,column=0,sticky=(N,E,S,W))

	i = 0
	for l in labels:
		l.grid(row=i, column=0, sticky=W)
		i = i + 1

	startButton.grid(row=i, column=0, sticky=W)
	resetButton.grid(row=i, column=1)

	seedLabel.grid(row=i+1, column=0, sticky=W)
	radioButton1.grid(row=i+1, column=1)
	radioButton2.grid(row=i+1, column=2)
	textBox.grid(row=i+1, column=3)
	blink.grid(row=i+1, column=4)

	seedOption.set('Auto')

	for child in frame1.winfo_children():
		child.grid_configure(padx=5, pady=5)

	root.mainloop()
