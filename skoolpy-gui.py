from tkinter import *
from datetime import *
import getpass
import time

root=Tk()
root.title("SkoolPy")
root.resizable(False,False)

label1=Label(root,text="Amity International School")
label2=Label(root)

t=''
def timer():
	global t
	t2=datetime.now().strftime("%H:%M:%S")
	if t2!=t:
		t=t2
		label2.config(text=t2)
	label2.after(200,timer)

timer()
label1.grid(row=0,sticky=W+E+N+S)
label2.grid(row=1,sticky=W+E+N+S)
root.mainloop()