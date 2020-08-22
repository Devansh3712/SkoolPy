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
	textbox.config(state='normal')
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
				textbox.config(state='normal')
				if ans.get()=="Y":
					teacherAttendence[name]=1
					textbox.insert(INSERT,"{} is now marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked on leave".format(name))
				else:
						textbox.insert(INSERT,"Invalid Option")
				textbox.config(state='disabled')
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
				textbox.config(state='normal')
				if ans.get()=="Y":
					teacherAttendence[name]=1
					textbox.insert(INSERT,"{} is now marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked on half day".format(name))
				else:
						textbox.insert(INSERT,"Invalid Option")
				textbox.config(state='disabled')
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
	att.set("")
	textbox.config(state='disabled')

def onLeave():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	name=str(leave.get())
	if name in subjects.values():
		if teacherAttendence[name]==1:
			new=Toplevel(root)
			new.title("SkoolPy")
			new.resizable(False,False)
			isPresent=name+' is marked as present, do you want to mark it on leave?\n \'Y\' for yes, \'N\' for no'
			ans=StringVar(new)
			def test():
				textbox.config(state='normal')
				if ans.get()=="Y":
					teacherAttendence[name]=2
					textbox.insert(INSERT,"{} is now marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked as present".format(name))
				else:
						textbox.insert(INSERT,"Invalid Option")
				textbox.config(state='disabled')
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
			isPresent=name+' is marked as on half day, do you want to mark it as on leave?\n \'Y\' for yes, \'N\' for no'
			ans=StringVar(new)
			def test():
				if ans.get()=="Y":
					textbox.config(state='normal')
					teacherAttendence[name]=3
					textbox.insert(INSERT,"{} is now marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
				elif ans.get()=="N":
					textbox.insert(INSERT,"{} is marked on half day".format(name))
				else:
						textbox.insert(INSERT,"Invalid Option")
				textbox.config(state='disabled')
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
	leave.set("")
	textbox.config(state='disabled')

def onHalfDay():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	name=str(half.get())
	if int(datetime.now().strftime("%H%M"))>=1200:
		if name in subjects.values():
			if teacherAttendence[name]==1:
				new=Toplevel(root)
				new.title("SkoolPy")
				new.resizable(False,False)
				isPresent=name+' is marked as present, do you want to mark it as on half day?\n \'Y\' for yes, \'N\' for no'
				ans=StringVar(new)
				def test():
					textbox.config(state='normal')
					if ans.get()=="Y":
						teacherAttendence[name]=3
						textbox.insert(INSERT,"{} is now marked on half day at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					elif ans.get()=="N":
						textbox.insert(INSERT,"{} is marked as present".format(name))
					else:
						textbox.insert(INSERT,"Invalid Option")
					textbox.config(state='disabled')
					new.destroy()
				newLabel1=Label(new,text=str(isPresent))
				newEntry1=Entry(new,textvariable=ans)
				newButton1=Button(new,text="Enter",command=test)
				newLabel1.grid(row=0,column=0,sticky=W)
				newEntry1.grid(row=0,column=1)
				newButton1.grid(row=1,columnspan=2)
			elif teacherAttendence[name]==2:
				new=Toplevel(root)
				new.title("SkoolPy")
				new.resizable(False,False)
				isPresent=name+' is marked on leave, do you want to mark it as on half day?\n \'Y\' for yes, \'N\' for no'
				ans=StringVar(new)
				def test():
					textbox.config(state='normal')
					if ans.get()=="Y":
						teacherAttendence[name]=3
						textbox.insert(INSERT,"{} is now marked on half day at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					elif ans.get()=="N":
						textbox.insert(INSERT,"{} is marked on leave".format(name))
					else:
						textbox.insert(INSERT,"Invalid Option")
					textbox.config(state='disabled')
					new.destroy()
				newLabel1=Label(new,text=str(isPresent))
				newEntry1=Entry(new,textvariable=ans)
				newButton1=Button(new,text="Enter",command=test)
				newLabel1.grid(row=0,column=0,sticky=W)
				newEntry1.grid(row=0,column=1)
				newButton1.grid(row=1,columnspan=2)
			else:
				teacherAttendence[name]=3
				textbox.insert(INSERT,"{} marked on half day at {}".format(name,datetime.now().strftime("%H:%M:%S")))
		else:
			textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
	else:
		textbox.insert(INSERT,"Cannot mark on half day before 12:00 PM")
	half.set("")
	textbox.config(state='disabled')

def showCurrentAtt():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	for i in teacherAttendence:
		if teacherAttendence[i]==1:
			c="Present"
		elif teacherAttendence[i]==2:
			c="On Leave"
		elif teacherAttendence[i]==3:
			c="On Half Day"
		else:
			c="Absent"
		textbox.insert(INSERT,"{} is {}\n".format(i,c))
	textbox.config(state='disabled')

def quitSP():
	textbox.config(state='normal')
	new=Toplevel(root)
	new.title("Quit")
	new.resizable(False,False)
	passwd=StringVar(new)
	def checkPass():
		if passwd.get()=="amity@123":
			new.destroy()
			root.destroy()
		else:
			textbox.config(state='normal')
			textbox.insert(INSERT,"Password incorrect, access denied")
			textbox.config(state='disabled')
	newLabel1=Label(new,text="Enter Password: ")
	newEntry1=Entry(new,textvariable=passwd,show="")
	newButton1=Button(new,text="Enter",command=checkPass)
	newLabel1.grid(row=0,column=0,sticky=W)
	newEntry1.grid(row=0,column=1)
	newButton1.grid(row=1,columnspan=2)
	textbox.config(state='disabled')

att=StringVar(root)
leave=StringVar(root)
half=StringVar(root)

textbox=Text(root,height=20,width=50)
label1=Label(root,text="AMITY INTERNATIONAL SCHOOL")
label2=Label(root)
space=Label(root,text=" ")

label3=Label(root,text="1. Add your attendence: ")
entry1=Entry(root,textvariable=att)
button1=Button(root,text="Mark",command=attendence)

label4=Label(root,text="2. Mark a teacher on leave: ")
entry2=Entry(root,textvariable=leave)
button2=Button(root,text="Mark",command=onLeave)

label5=Label(root,text="3. Mark a teacher on half day: ")
entry3=Entry(root,textvariable=half)
button3=Button(root,text="Mark",command=onHalfDay)

label6=Label(root,text="4. Show current attendence")
button4=Button(root,text="Show",command=showCurrentAtt)

quitButton=Button(root,text="Quit",command=quitSP)

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
space.grid(row=2,columnspan=8)
textbox.grid(row=3,column=3,rowspan=10,columnspan=5)

label3.grid(row=3,column=0,sticky=W)
entry1.grid(row=3,column=1)
button1.grid(row=3,column=2)

label4.grid(row=4,column=0,sticky=W)
entry2.grid(row=4,column=1)
button2.grid(row=4,column=2)

label5.grid(row=5,column=0,sticky=W)
entry3.grid(row=5,column=1)
button3.grid(row=5,column=2)

label6.grid(row=6,column=0,sticky=W)
button4.grid(row=6,column=1,sticky=W+E)

quitButton.grid(row=14,column=7,columnspan=2)

mainloop()