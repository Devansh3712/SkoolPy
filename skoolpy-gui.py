from tkinter import *
from tkinter.ttk import *
from datetime import *
import getpass
import time

root=Tk()
root.title("SkoolPy")
root.resizable(False,False)

subjects={"Chemistry":"Sadhvi Gautam","Physics":"Liji Davis","Maths":"Vipin Kumar","CS":"Halina Gupta","English":"Sudhi Bhatia"}
teacherAttendence={"Sadhvi Gautam":0,"Liji Davis":0,"Vipin Kumar":0,"Halina Gupta":0,"Sudhi Bhatia":0}

def attendence():
	textbox.delete(1.0,"end")
	name=str(att.get())
	if name in subjects.values():
		if teacherAttendence[name]==1:
			textbox.insert(INSERT,"{} is already marked present".format(name))
		elif teacherAttendence[name]==2:
			new=Toplevel(root)
			new.title("SkoolPy")
			new.resizable(False,False)
			isPresent=name+' is marked as on leave, do you want to mark it as present?\n \'Y\' for yes, \'N\' for no'
			ans=StringVar(new)
			def test():
				if ans.get()=="Y":
					teacherAttendence[name]=1
					textbox.insert(INSERT,"{} is now marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked on leave".format(name))
				new.destroy()
			newLabel1=Label(new,text=str(isPresent))
			newEntry1=Entry(new,textvariable=ans)
			newButton1=Button(new,text="Enter",command=test)
			newLabel1.grid(row=0,column=0,sticky=W)
			newEntry1.grid(row=0,column=1)
			newButton1.grid(row=1,columnspan=2)
		elif teacherAttendence[name]==3:
			new=Toplevel(root)
			new.title("SkoolPy")
			new.resizable(False,False)
			isPresent=name+' is marked as on half day, do you want to mark it as present?\n \'Y\' for yes, \'N\' for no'
			ans=StringVar(new)
			def test():
				if ans.get()=="Y":
					teacherAttendence[name]=1
					textbox.insert(INSERT,"{} is now marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked on half day".format(name))
				new.destroy()
			newLabel1=Label(new,text=str(isPresent))
			newEntry1=Entry(new,textvariable=ans)
			newButton1=Button(new,text="Enter",command=test)
			newLabel1.grid(row=0,column=0,sticky=W)
			newEntry1.grid(row=0,column=1)
			newButton1.grid(row=1,columnspan=2)
		else:
			teacherAttendence[name]=1
			textbox.insert(INSERT,"{} marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
	else:
		textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")

def onLeave():
	textbox.delete(1.0,"end")
	name=str(leave.get())
	if name in subjects.values():
		if teacherAttendence[name]==1:
			new=Toplevel(root)
			new.title("SkoolPy")
			new.resizable(False,False)
			isPresent=name+' is marked as present, do you want to mark it on leave? \'Y\' for yes, \'N\' for no'
			ans=StringVar(new)
			def test():
				if ans.get()=="Y":
					teacherAttendence[name]=2
					textbox.insert(INSERT,"{} is now marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked as present".format(name))
				new.destroy()
			newLabel1=Label(new,text=str(isPresent))
			newEntry1=Entry(new,textvariable=ans)
			newButton1=Button(new,text="Enter",command=test)
			newLabel1.grid(row=0,column=0,sticky=W)
			newEntry1.grid(row=0,column=1)
			newButton1.grid(row=1,columnspan=2)
		elif teacherAttendence[name]==2:
			textbox.insert(INSERT,"{} is already marked on leave".format(name))
		elif teacherAttendence[name]==3:
			new=Toplevel(root)
			new.title("SkoolPy")
			new.resizable(False,False)
			isPresent=name+' is marked as on half day, do you want to mark it as on leave? \'Y\' for yes, \'N\' for no'
			ans=StringVar(new)
			def test():
				if ans.get()=="Y":
					teacherAttendence[name]=3
					textbox.insert(INSERT,"{} is now marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked on half day".format(name))
				new.destroy()
			newLabel1=Label(new,text=str(isPresent))
			newEntry1=Entry(new,textvariable=ans)
			newButton1=Button(new,text="Enter",command=test)
			newLabel1.grid(row=0,column=0,sticky=W)
			newEntry1.grid(row=0,column=1)
			newButton1.grid(row=1,columnspan=2)
		else:
			teacherAttendence[name]=2
			textbox.insert(INSERT,"{} marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
	else:
		textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")

def onHalfDay():
	name=str(half.get())
	if int(datetime.now().strftime("%H%M"))>=1200:
		if name in subjects.values():
			if teacherAttendence[name]==1:
				print("{} was marked present previously, do you want to mark it on half day?".format(name))
				cin=input("Y/N : ")
				while True:
					if cin.lower()=="y":
						teacherAttendence[name]=3
						print("{} is now marked on half day at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					elif cin.lower()=="n":
						print("{} is marked present".format(name))
					else:
						print("Enter Y for \'yes\' and n for \'no\'")
			elif teacherAttendence[name]==2:
				print("{} is marked as on leave, do you want to mark it as on half day?".format(name))
				cin=input("Y/N : ")
				while True:
					if cin.lower()=="y":
						teacherAttendence[name]=3
						print("{} is now marked on half day at {}".format(name,datetime.now().strftime("%H:%M:%S")))
						break
					elif cin.lower()=="n":
						print("{} is marked on leave".format(name))
						break
					else:
						print("Enter Y for \'yes\' and N for \'no\'")
			else:
				teacherAttendence[name]=3
				print("{} marked on half day at {}".format(name,datetime.now().strftime("%H:%M:%S")))
		else:
			print("Name not found in record, try capitalizing initials of your name")
	else:
		print("Cannot mark on half day before 12:00 PM")

att=StringVar(root)
leave=StringVar(root)
half=StringVar(root)

textbox=Text(root)
label1=Label(root,text="Amity International School")
label2=Label(root)
label3=Label(root,text="1. Add your attendence:")
entry1=Entry(root,textvariable=att)
button1=Button(root,text="Mark",command=attendence)
label4=Label(root,text="2. Mark a teacher on leave:")
entry2=Entry(root,textvariable=leave)
button2=Button(root,text="Mark",command=onLeave)

t=''
def timer():
	global t
	t2=datetime.now().strftime("%B %d, %Y %H:%M:%S")
	if t2!=t:
		t=t2
		label2.config(text=t2)
	label2.after(200,timer)
timer()

label1.grid(row=0,columnspan=8)
label2.grid(row=1,columnspan=8)
label3.grid(row=2,column=0)
entry1.grid(row=2,column=1)
button1.grid(row=2,column=2)
textbox.grid(row=2,column=3,rowspan=10,columnspan=5)
label4.grid(row=3,column=0)
entry2.grid(row=3,column=1)
button2.grid(row=3,column=2)
mainloop()