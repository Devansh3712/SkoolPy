from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import *
import getpass
import time
import webbrowser

root=Tk()
root.title("SkoolPy")
root.resizable(False,False)

subjects={"Chemistry":"Sadhvi Gautam","Physics":"Liji Davis","Maths":"Vipin Kumar","CS":"Halina Gupta","English":"Sudhi Bhatia"}
teacherAttendence={"Sadhvi Gautam":0,"Liji Davis":0,"Vipin Kumar":0,"Halina Gupta":0,"Sudhi Bhatia":0}
teacherCode={"Sadhvi Gautam":"CSG","Liji Davis":"PLD","Vipin Kumar":"MVK","Halina Gupta":"CSHG","Sudhi Bhatia":"ESB"}

def attendence():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	name=str(att.get())
	if int(datetime.now().strftime("%H%M"))<=1200:
		if int(datetime.now().strftime("%H%M"))<=800:
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
		elif int(datetime.now().strftime("%H%M"))>800:
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
							teacherAttendence[name]=4
							textbox.insert(INSERT,"{} is now marked present (late) at {}".format(name,datetime.now().strftime("%H:%M:%S")))
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
							teacherAttendence[name]=4
							textbox.insert(INSERT,"{} is now marked present (late) at {}".format(name,datetime.now().strftime("%H:%M:%S")))
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
					teacherAttendence[name]=4
					textbox.insert(INSERT,"{} marked present (late) at {}".format(name,datetime.now().strftime("%H:%M:%S")))
		elif name not in subjects.values():
			textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
	elif int(datetime.now().strftime("%H%M"))>1200:
		textbox.insert(INSERT,"Cannot mark attendence after 12:00 PM")
	elif int(datetime.now().strftime("%H%M"))<600:
		textbox.insert(INSERT,"Cannot mark attendence before 6:00 AM")
	att.set("")
	textbox.config(state='disabled')

def onLeave():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	name=str(leave.get())
	if name in subjects.values():
		if teacherAttendence[name]==1 or teacherAttendence[name]==4:
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
					teacherAttendence[name]=2
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
			if teacherAttendence[name]==1 or teacherAttendence[name]==4:
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
		elif teacherAttendence[i]==4:
			c="Present (late)"
		else:
			c="Absent"
		textbox.insert(INSERT,"{} is {}\n".format(i,c))
	textbox.config(state='disabled')

def quitSP():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
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
	newEntry1=Entry(new,textvariable=passwd,show="*")
	newButton1=Button(new,text="Enter",command=checkPass)
	newLabel1.grid(row=0,column=0,sticky=W)
	newEntry1.grid(row=0,column=1)
	newButton1.grid(row=1,columnspan=2)
	textbox.config(state='disabled')

def showInf():
	new=Toplevel(root)
	new.title("Information")
	new.resizable(False,False)
	def openWeb():
		new=1
		url="https://github.com/Devansh3712/SkoolPy"
		webbrowser.open(url,new=new)
	newLabel1=Label(new,text="SkoolPy v1.0")
	newLabel2=Label(new,text="Made by Devansh")
	newLabel3=Label(new,text="View project on Github:")
	emptyLabel=Label(new,text="")
	newButton1=Button(new,text="Visit",command=openWeb)
	newLabel1.grid(row=0,columnspan=2)
	newLabel2.grid(row=1,columnspan=2)
	emptyLabel.grid(row=2)
	newLabel3.grid(row=3,column=0)
	newButton1.grid(row=3,column=1)

def exportData():
	teacherAtt=datetime.now().strftime("%B%d%Y")+'.txt'
	f=open(teacherAtt,'w')
	for i in teacherAttendence:
		if teacherAttendence[i]==1:
			f.write("{} is present".format(i))
		elif teacherAttendence[i]==2:
			f.write("{} is on leave".format(i))
		elif teacherAttendence[i]==3:
			f.write("{} is on half day".format(i))
		elif teacherAttendence[i]==4:
			f.write("{} is present (late)".format(i))
		else:
			f.write("{} is absent".format(i))
		f.write("\n")
	f.close()
	def showMessage():
		messagebox.showinfo("Export", "Attendence exported succesfully in current directory")
	showMessage()

def checkTeacherStatus():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	name=str(stat.get())
	if name in teacherAttendence:
		textbox.insert(INSERT,"{} teaches {}\n".format(name,list(subjects.keys())[list(subjects.values()).index(name)]))
		if teacherAttendence[name]==1:
			textbox.insert(INSERT,"{} is present\n".format(name))
		elif teacherAttendence[name]==2:
			textbox.insert(INSERT,"{} is on leave\n".format(name))
		elif teacherAttendence[name]==3:
			textbox.insert(INSERT,"{} is on half day\n".format(name))
		elif teacherAttendence[name]==4:
			textbox.insert(INSERT,"{} is present (late)\n".format(name))
		else:
			textbox.insert(INSERT,"{} is Absent\n".format(name))
		if teacherAttendence[name]==1 or teacherAttendence[name]==4:
			a=teacherCode[name]
			if a=="CSG":
				CSG={"Monday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Tuesday":[0,0,'12-C','12-C','12-A','12-A',0,0],"Wednesday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Thursday":['12-B','12-B',0,0,'12-A','12-A','12-C','12-C'],"Friday":[0,0,'12-A','12-A','12-B','12-B',0,0]}
				i=datetime.now().strftime("%A")
				if i in CSG:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						if CSG[i][0]!=0:
							textbox.insert(INSERT,"Period 1 in {}".format(CSG[i][0]))
						else:
							textbox.insert(INSERT,"Period 1 is free")
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						if CSG[i][1]!=0:
							textbox.insert(INSERT,"Period 2 in {}".format(CSG[i][1]))
						else:
							textbox.insert(INSERT,"Period 2 is free")
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						if CSG[i][2]!=0:
							textbox.insert(INSERT,"Period 3 in {}".format(CSG[i][2]))
						else:
							textbox.insert(INSERT,"Period 3 is free")
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						if CSG[i][3]!=0:
							textbox.insert(INSERT,"Period 4 in {}".format(CSG[i][3]))
						else:
							textbox.insert(INSERT,"Period 4 is free")
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						if CSG[i][4]!=0:
							textbox.insert(INSERT,"Period 5 in {}".format(CSG[i][4]))
						else:
							textbox.insert(INSERT,"Period 5 is free")
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						if CSG[i][5]!=0:
							textbox.insert(INSERT,"Period 6 in {}".format(CSG[i][5]))
						else:
							textbox.insert(INSERT,"Period 6 is free")
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						if CSG[i][6]!=0:
							textbox.insert(INSERT,"Period 7 in {}".format(CSG[i][6]))
						else:
							textbox.insert(INSERT,"Period 7 is free")
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						if CSG[i][7]!=0:
							textbox.insert(INSERT,"Period 8 in {}".format(CSG[i][7]))
						else:
							textbox.insert(INSERT,"Period 8 is free")
					else:
						textbox.insert(INSERT,"Data for current time not available")
				else:
					textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
			if a=="PLD":
				PLD={"Monday":['12-B','12-B','12-C','12-C',0,0,'12-A','12-A'],"Tuesday":['12-A','12-A','12-C','12-C',0,0,0,0],"Wednesday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Thursday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Friday":[0,0,0,0,'12-A','12-A','12-B','12-B']}
				i=datetime.now().strftime("%A")
				if i in PLD:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						if PLD[i][0]!=0:
							textbox.insert(INSERT,"Period 1 in {}".format(PLD[i][0]))
						else:
							textbox.insert(INSERT,"Period 1 is free")
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						if PLD[i][1]!=0:
							textbox.insert(INSERT,"Period 2 in {}".format(PLD[i][1]))
						else:
							textbox.insert(INSERT,"Period 2 is free")
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						if PLD[i][2]!=0:
							textbox.insert(INSERT,"Period 3 in {}".format(PLD[i][2]))
						else:
							textbox.insert(INSERT,"Period 3 is free")
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						if PLD[i][3]!=0:
							textbox.insert(INSERT,"Period 4 in {}".format(PLD[i][3]))
						else:
							textbox.insert(INSERT,"Period 4 is free")
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						if PLD[i][4]!=0:
							textbox.insert(INSERT,"Period 5 in {}".format(PLD[i][4]))
						else:
							textbox.insert(INSERT,"Period 5 is free")
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						if PLD[i][5]!=0:
							textbox.insert(INSERT,"Period 6 in {}".format(PLD[i][5]))
						else:
							textbox.insert(INSERT,"Period 6 is free")
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						if PLD[i][6]!=0:
							textbox.insert(INSERT,"Period 7 in {}".format(PLD[i][6]))
						else:
							textbox.insert(INSERT,"Period 7 is free")
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						if PLD[i][7]!=0:
							textbox.insert(INSERT,"Period 8 in {}".format(PLD[i][7]))
						else:
							textbox.insert(INSERT,"Period 8 is free")
					else:
						textbox.insert(INSERT,"Data for current time not available")
				else:
					textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
			if a=="MVK":
				MVK={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[0,0,1,1,0,0,1,1],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[1,1,0,0,1,1,1,1]}
				i=datetime.now().strftime("%A")
				if i in MVK:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						textbox.insert(INSERT,"Period 1 in {}".format(MVK[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						textbox.insert(INSERT,"Period 2 in {}".format(MVK[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						textbox.insert(INSERT,"Period 3 in {}".format(MVK[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						textbox.insert(INSERT,"Period 4 in {}".format(MVK[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						textbox.insert(INSERT,"Period 5 in {}".format(MVK[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						textbox.insert(INSERT,"Period 6 in {}".format(MVK[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						textbox.insert(INSERT,"Period 7 in {}".format(MVK[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						textbox.insert(INSERT,"Period 8 in {}".format(MVK[i][7]))
					else:
						textbox.insert(INSERT,"Data for current time not available")
				else:
					textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
			if a=="CSHG":
				CSHG={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[1,1,0,0,1,1,0,0],"Wednesday":[0,0,1,1,0,0,1,1],"Thursday":[1,1,0,0,0,0,1,1],"Friday":[1,1,1,1,1,1,0,0]}
				i=datetime.now().strftime("%A")
				if i in CSHG:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						textbox.insert(INSERT,"Period 1 in {}".format(CSHG[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						textbox.insert(INSERT,"Period 2 in {}".format(CSHG[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						textbox.insert(INSERT,"Period 3 in {}".format(CSHG[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						textbox.insert(INSERT,"Period 4 in {}".format(CSHG[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						textbox.insert(INSERT,"Period 5 in {}".format(CSHG[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						textbox.insert(INSERT,"Period 6 in {}".format(CSHG[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						textbox.insert(INSERT,"Period 7 in {}".format(CSHG[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						textbox.insert(INSERT,"Period 8 in {}".format(CSHG[i][7]))
					else:
						textbox.insert(INSERT,"Data for current time not available")
				else:
					textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
			if a=="ESB":
				ESB={"Monday":[1,1,0,0,1,1,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[0,0,1,1,0,0,1,1],"Friday":[0,0,1,1,0,0,1,1]}
				i=datetime.now().strftime("%A")
				if i in ESB:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						textbox.insert(INSERT,"Period 1 in {}".format(ESB[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						textbox.insert(INSERT,"Period 2 in {}".format(ESB[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						textbox.insert(INSERT,"Period 3 in {}".format(ESB[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						textbox.insert(INSERT,"Period 4 in {}".format(ESB[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						textbox.insert(INSERT,"Period 5 in {}".format(ESB[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						textbox.insert(INSERT,"Period 6 in {}".format(ESB[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						textbox.insert(INSERT,"Period 7 in {}".format(ESB[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						textbox.insert(INSERT,"Period 8 in {}".format(ESB[i][7]))
					else:
						textbox.insert(INSERT,"Data for current time not available")
				else:
					textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
		else:
			textbox.insert(INSERT,"{} is not available today at school".format(name))
	else:
		text.insert(INSERT,"Name not found in record, try capitalizing initials of your name")
	stat.set("")
	textbox.config(state='disabled')

def showTimetable():
	textbox.config(state='normal')
	textbox.delete(1.0,"end")
	name=str(tt.get())
	if name in teacherCode:
		a=teacherCode[name]
		if a=="CSG":
			CSG={"Monday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Tuesday":[0,0,'12-C','12-C','12-A','12-A',0,0],"Wednesday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Thursday":['12-B','12-B',0,0,'12-A','12-A','12-C','12-C'],"Friday":[0,0,'12-A','12-A','12-B','12-B',0,0]}
			i=datetime.now().strftime("%A")
			if i in CSG:
				b=1
				for j in CSG[i]:
					if j!=0:
						textbox.insert(INSERT,"Period {} in class {}\n".format(b,j))
					else:
						textbox.insert(INSERT,"Period {} is free\n".format(b))
					b=b+1
			else:
				textbox.insert(INSERT,"Today is a weekend, timetable not available\n")
		elif a=="PLD":
			PLD={"Monday":[1,1,1,1,0,0,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,0,0,1,1,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[0,0,0,0,1,1,1,1]}
			i=datetime.now().strftime("%A")
			if i in PLD:
				b=1
				for j in PLD[i]:
					if j!=0:
						textbox.insert(INSERT,"Period {} in class {}\n".format(b,j))
					else:
						textbox.insert(INSERT,"Period {} is free\n".format(b))
					b=b+1
			else:
				textbox.insert(INSERT,"Today is a weekend, timetable not available\n")
		elif a=="MVK":
			MVK={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[0,0,1,1,0,0,1,1],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[1,1,0,0,1,1,1,1]}
			i=datetime.now().strftime("%A")
			if i in MVK:
				b=1
				for j in MVK[i]:
					if j!=0:
						textbox.insert(INSERT,"Period {} in class {}\n".format(b,j))
					else:
						textbox.insert(INSERT,"Period {} is free\n".format(b))
					b=b+1
			else:
				textbox.insert(INSERT,"Today is a weekend, timetable not available\n")
		elif a=="CSHG":
			CSHG={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[1,1,0,0,1,1,0,0],"Wednesday":[0,0,1,1,0,0,1,1],"Thursday":[1,1,0,0,0,0,1,1],"Friday":[1,1,1,1,1,1,0,0]}
			i=datetime.now().strftime("%A")
			if i in CSHG:
				b=1
				for j in CSHG[i]:
					if j!=0:
						textbox.insert(INSERT,"Period {} in class {}\n".format(b,j))
					else:
						textbox.insert(INSERT,"Period {} is free\n".format(b))
					b=b+1
			else:
				textbox.insert(INSERT,"Today is a weekend, timetable not available\n")
		elif a=="ESB":
			ESB={"Monday":[1,1,0,0,1,1,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[0,0,1,1,0,0,1,1],"Friday":[0,0,1,1,0,0,1,1]}
			i=datetime.now().strftime("%A")
			if i in ESB:
				b=1
				for j in ESB[i]:
					if j!=0:
						textbox.insert(INSERT,"Period {} in class {}\n".format(b,j))
					else:
						textbox.insert(INSERT,"Period {} is free\n".format(b))
					b=b+1
			else:
				textbox.insert(INSERT,"Today is a weekend, timetable not available\n")
		else:
			textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name\n")
	else:
		textbox.insert(INSERT,"Name not found in record, try capitalizing initials of your name\n")
	tt.set("")
	textbox.config(state='disabled')

att=StringVar(root)
leave=StringVar(root)
half=StringVar(root)
stat=StringVar(root)
tt=StringVar(root)

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

label8=Label(root,text="4. Check a teacher's status: ")
entry4=Entry(root,textvariable=stat)
button6=Button(root,text="Check",command=checkTeacherStatus)

label9=Label(root,text="5. Check a teacher's timetable: ")
entry5=Entry(root,textvariable=tt)
button7=Button(root,text="Check",command=showTimetable)

label6=Label(root,text="6. Show current attendence")
button4=Button(root,text="Show",command=showCurrentAtt)

label7=Label(root,text="7. Export today's attendence")
button5=Button(root,text="Export",command=exportData)

quitButton=Button(root,text="Quit",command=quitSP)
showInfo=Button(root,text="Info",command=showInf)

t=''
def timer():
	global t
	t2=datetime.now().strftime("%B %d, %Y %H:%M:%S")
	if t2!=t:
		t=t2
		label2.config(text=t2)
	label2.after(200,timer)
timer()

asciiArt='''
   _____ _               _ _____       
  / ____| |             | |  __ \      
 | (___ | | _____   ___ | | |__) |   _ 
  \___ \| |/ / _ \ / _ \| |  ___/ | | |
  ____) |   < (_) | (_) | | |   | |_| |
 |_____/|_|\_\___/ \___/|_|_|    \__, |
                                  __/ |
                                 |___/ 
                                 
 A School Management System GUI made
 using python and tkinter.

 SkoolPy is an open-source software
 and is free to use. 

 Copyright © Devansh Singh
                                 '''
textbox.insert(INSERT,asciiArt)
textbox.config(state="disabled")

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

label8.grid(row=6,column=0,sticky=W)
entry4.grid(row=6,column=1)
button6.grid(row=6,column=2)

label9.grid(row=7,column=0,sticky=W)
entry5.grid(row=7,column=1)
button7.grid(row=7,column=2)

label6.grid(row=8,column=0,sticky=W)
button4.grid(row=8,column=1,sticky=W+E)

label7.grid(row=9,column=0,sticky=W)
button5.grid(row=9,column=1,sticky=W+E)

quitButton.grid(row=14,column=7,columnspan=2)
showInfo.grid(row=14,sticky=W)

root.protocol("WM_DELETE_WINDOW",quitSP)
mainloop()
