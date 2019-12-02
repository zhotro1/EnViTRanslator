import os, sys
from googletrans import Translator

import ctypes
import time
import pyperclip
import pyautogui as pag
import multiprocessing

from tkinter import Tk, mainloop, TOP, BOTTOM, Label
from tkinter.ttk import Button


datafile = "envi.ico" 
if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), datafile) 
else: 
    datafile = os.path.join(sys.prefix, datafile)


translator = Translator()
data = 'ok'

user32 = ctypes.windll.user32

previous_timestamp = None
double_click_threshold = 0.300
detect_time = 0.0

list_process = []

sign = True

def get_key_press():
    if user32.GetAsyncKeyState(0x01) == 32768:
        time.sleep(0.2)
        if user32.GetAsyncKeyState(0x01) != 32768:
            return time.time()

def get_double_click():
	global previous_timestamp
	global double_click_threshold
	global detect_time
	while 1:
	    keypress_time = get_key_press()
	    if keypress_time is not None and previous_timestamp is not None:
	        elapsed = keypress_time - previous_timestamp
	        if (elapsed <= double_click_threshold) and (user32.GetAsyncKeyState(0x01) != 32768):
	            if (keypress_time - detect_time) > 0.20*5:
	                detect_time = time.time()
	                pag.hotkey('ctrl', 'c')
	        previous_timestamp = keypress_time
	    elif keypress_time is not None:
	        previous_timestamp = keypress_time

		
def main():
	recent_value = ''
	while 1:
		tmp_value = pyperclip.paste()
		if tmp_value != recent_value:
			recent_value = tmp_value
			sign = True
		else:
			sign = False
		time.sleep(0.1)

		if sign:
			data = str(pyperclip.paste())
			dich = translator.translate(data, dest='vi').text
			list_word = dich.split(' ')
			list_word = [x.replace("\r\n", "") for x in list_word]
			if len(list_word) > 6:
				for i in range(len(list_word)):
					if ((i+1)%6) == 0:
						list_word[i] +='\n'
			dich = ' '.join(list_word)
			label = Label(text=dich, font=('Times','28'), fg='cyan', bg='gray')
			label.master.overrideredirect(True)
			label.master.geometry("+700+50")
			label.master.lift()
			label.master.wm_attributes("-topmost", True)
			label.master.wm_attributes("-disabled", True)
			label.master.wm_attributes("-transparentcolor", "white")
			label.pack()
			label.after(3000, lambda: label.master.destroy())
			label.mainloop()

def start():
	global list_process
	for i in range(len(list_process)):
		list_process[i].terminate()
	x = multiprocessing.Process(target=get_double_click, daemon=True)
	y = multiprocessing.Process(target=main, daemon=True)
	try:
		x.start()
		list_process.append(x)
		y.start()
		list_process.append(y)
	except KeyboardInterrupt:
		sys.exit(1)


def stop():
	for i in range(len(list_process)):
		list_process[i].terminate()
def quit():
	sys.exit(0)


def make_windows():
	root = Tk()
	root['bg'] = '#6ad4af'
	root.title('English Vietnam Translator') 

	# creating fixed geometry of the 
	# tkinter window with dimensions 400x150 
	root.geometry('400x150') 
	root.iconbitmap(default=datafile)

	label = Label(text='Program designed by NGOC HIEU', font=('Times','20'))
	label1 = Label(text='Hướng dẫn: copy từ cần dịch hoặc nháy đúp vào từ cần\n dịch trong văn bản để dịch từ đó sang tiếng việt.\nChú ý: Cần có kết nối mạng!', font=('Times','12'))
	button1 = Button(root, text = 'Start', command=start)
	button2 = Button(root, text = 'Stop', command=stop)
	button3 = Button(root, text = 'Quit', command=quit)
	label.pack(side = TOP)
	label1.pack(side = BOTTOM)
	button1.place(x= 50, y= 50)
	button2.place(x= 150, y= 50)
	button3.place(x= 250, y= 50)
	root.mainloop()
	

if __name__ == '__main__':
	multiprocessing.freeze_support()
	make_windows()


	


