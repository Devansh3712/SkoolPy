import time
from datetime import datetime
import getpass

def attendence(name):
	if name in subjects.values():
		if teacherAttendence[name]==1:
			print("{} is already marked present".format(name))
		elif teacherAttendence[name]==2:
			print("{} is marked as on leave, do you want to mark it as present?".format(name))
			cin=input("Y/N : ")
			while True:
				if cin.lower()=="y":
					teacherAttendence[name]=1
					print("{} is now marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					break
				elif cin.lower()=="n":
					print("{} is marked on leave".format(name))
					break
				else:
					print("Enter Y for \'yes\' and N for \'no\'")
		elif teacherAttendence[name]==3:
			print("{} is marked as on half day, do you want to mark it as present?".format(name))
			cin=input("Y/N : ")
			while True:
				if cin.lower()=="y":
					teacherAttendence[name]=1
					print("{} is now marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					break
				elif cin.lower()=="n":
					print("{} is marked on half day".format(name))
					break
				else:
					print("Enter Y for \'yes\' and N for \'no\'")
		else:
			teacherAttendence[name]=1
			print("{} marked present at {}".format(name,datetime.now().strftime("%H:%M:%S")))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def onLeave(name):
	if name in subjects.values():
		if teacherAttendence[name]==1:
			print("{} was marked present previously, do you want to mark it on leave?".format(name))
			cin=input("Y/N : ")
			while True:
				if cin.lower()=="y":
					teacherAttendence[name]=2
					print("{} is now marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					break
				elif cin.lower()=="n":
					print("{} is marked present".format(name))
					break
				else:
					print("Enter Y for \'yes\' and N for \'no\'")
		elif teacherAttendence[name]==2:
			print("{} is already marked on leave".format(name))
		elif teacherAttendence[name]==3:
			print("{} is marked as on half day, do you want to mark it on leave?".format(name))
			cin=input("Y/N : ")
			while True:
				if cin.lower()=="y":
					teacherAttendence[name]=2
					print("{} is now marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
					break
				elif cin.lower()=="n":
					print("{} is marked on half day".format(name))
					break
				else:
					print("Enter Y for \'yes\' and N for \'no\'")
		else:
			teacherAttendence[name]=2
			print("{} marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def onHalfDay(name):
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

def showCurrentAtt():
	for i in teacherAttendence:
		if teacherAttendence[i]==1:
			c="Present"
		elif teacherAttendence[i]==2:
			c="On Leave"
		elif teacherAttendence[i]==3:
			c="On Half Day"
		else:
			c="Absent"
		print("{} is {}".format(i,c))


def checkTeacherStatus(name):
	if name in teacherAttendence:
		for i in teacherAttendence:
			if i==name:
				print("{} teaches {}".format(name,list(subjects.keys())[list(subjects.values()).index(i)]))
				if teacherAttendence[i]==1:
					print("{} is present".format(name))
				elif teacherAttendence[i]==2:
					print("{} is on leave".format(name))
				elif teacherAttendence[i]==3:
					print("{} is on half day".format(name))
				else:
					print("{} is Absent".format(name))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def writeAttendence():
	c=datetime.now().strftime("%d%B%y")+".txt"
	f=open(c,"w")
	for i in teacherAttendence:
		if teacherAttendence[i]==1:
			f.write("{} is present".format(i))
		elif teacherAttendence[i]==2:
			f.write("{} is on leave".format(i))
		elif teacherAttendence[i]==3:
			f.write("{} is on half day".format(i))
		else:
			f.write("{} is absent".format(i))
		f.write("\n")
	f.close()


def showTimetable(name):
	if name in teacherCode:
		a=teacherCode[name]
		if a=="CSG":
			CSG={"Monday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Tuesday":[0,0,'12-C','12-C','12-A','12-A',0,0],"Wednesday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Thursday":['12-B','12-B',0,0,'12-A','12-A','12-C','12-C'],"Friday":[0,0,'12-A','12-A','12-B','12-B',0,0]}
			for i in CSG:
				if i==datetime.now().strftime("%A") and (datetime.now().strftime("%A")!="Saturday" or datetime.now().strftime("%A")!="Sunday"):
					a=1
					for j in CSG[i]:
						if j!=0:
							print("Period {} in class {}".format(a,j))
						else:
							print("Period {} is free".format(a))
						a=a+1
				else:
					print("Today is a weekend, timetable not available")
					break
		elif a=="PLD":
			PLD={"Monday":[1,1,1,1,0,0,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,0,0,1,1,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[0,0,0,0,1,1,1,1]}
			for i in PLD:
				if i==datetime.now().strftime("%A") and (datetime.now().strftime("%A")!="Saturday" or datetime.now().strftime("%A")!="Sunday"):
					a=1
					for j in PLD[i]:
						if j!=0:
							print("Period {} in class {}".format(a,j))
						else:
							print("Period {} is free".format(a))
						a=a+1
				else:
					print("Today is a weekend, timetable not available")
					break
		elif a=="MVK":
			MVK={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[0,0,1,1,0,0,1,1],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[1,1,0,0,1,1,1,1]}
			for i in MVK:
				if i==datetime.now().strftime("%A") and (datetime.now().strftime("%A")!="Saturday" or datetime.now().strftime("%A")!="Sunday"):
					a=1
					for j in MVK[i]:
						if j!=0:
							print("Period {} in class {}".format(a,j))
						else:
							print("Period {} is free".format(a))
						a=a+1
				else:
					print("Today is a weekend, timetable not available")
					break
		elif a=="CSHG":
			CSHG={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[1,1,0,0,1,1,0,0],"Wednesday":[0,0,1,1,0,0,1,1],"Thursday":[1,1,0,0,0,0,1,1],"Friday":[1,1,1,1,1,1,0,0]}
			for i in CSHG:
				if i==datetime.now().strftime("%A") and (datetime.now().strftime("%A")!="Saturday" or datetime.now().strftime("%A")!="Sunday"):
					a=1
					for j in CSHG[i]:
						if j!=0:
							print("Period {} in class {}".format(a,j))
						else:
							print("Period {} is free".format(a))
						a=a+1
				else:
					print("Today is a weekend, timetable not available")
					break
		elif a=="ESB":
			ESB={"Monday":[1,1,0,0,1,1,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[0,0,1,1,0,0,1,1],"Friday":[0,0,1,1,0,0,1,1]}
			for i in ESB:
				if i==datetime.now().strftime("%A") and (datetime.now().strftime("%A")!="Saturday" or datetime.now().strftime("%A")!="Sunday"):
					a=1
					for j in ESB[i]:
						if j!=0:
							print("Period {} in class {}".format(a,j))
						else:
							print("Period {} is free".format(a))
						a=a+1
				else:
					print("Today is a weekend, timetable not available")
					break
		else:
			print("Name not found in record, try capitalizing initials of your name")
	else:
		print("Name not found in record, try capitalizing initials of your name")

subjects={"Chemistry":"Sadhvi Gautam","Physics":"Liji Davis","Maths":"Vipin Kumar","CS":"Halina Gupta","English":"Sudhi Bhatia"}
teacherAttendence={"Sadhvi Gautam":0,"Liji Davis":0,"Vipin Kumar":0,"Halina Gupta":0,"Sudhi Bhatia":0}
teacherCode={"Sadhvi Gautam":"CSG","Liji Davis":"PLD","Vipin Kumar":"MVK","Halina Gupta":"CSHG","Sudhi Bhatia":"ESB"}

print()
print(">>> School Management System <<<")
print()
print(">>> "+datetime.now().strftime("%B %d, %Y %H:%M:%S")+" <<<")
print()
print("1. Add your attendence")
print("2. Mark a teacher on leave")
print("3. Mark a teacher on half day")
print("4. Show today's current attendence")
print("5. Show a teacher's status")
print("6. Show a teacher's timetable")
print("7. Add subsitution")
print("8. Exit")
print()

while True:
	tin=input("Type the option to proceed: ")
	print()
	if datetime.now().strftime("%H:%M")=="12:00":
		writeAttendence()
	elif int(datetime.now().strftime("%H%M"))>1200:
		if tin=="1":
			print("Cannot mark attendence after 12:00 PM")
			print()
		elif tin=="4":
			showCurrentAtt()
			print()
		elif tin=="2":
			print("Cannot mark on leave after 12:00 PM")
			print()
		elif tin=="3":
			name=input("Enter name: ")
			print()
			onHalfDay(name)
			print()
		elif tin=="5":
			name=input("Enter name: ")
			print()
			checkTeacherStatus(name)
			print()
		elif tin=="6":
			name=input("Enter name: ")
			print()
			showTimetable(name)
			print()
		elif tin=="8":
			passwd=getpass.getpass(prompt="Enter Password: ")
			print()
			if passwd=="amity@123":
				print("Terminating program")
				time.sleep(3)
				break
			else:
				print("Password incorrect, access denied")
				print()
		else:
			print("Enter a valid option from 1 to 7")
			print()
	elif int(datetime.now().strftime("%H%M"))<600:
		print("Attendence and other status cannot be shown now, try after 6:00 AM")
		print()
	else:
		if tin=="1":
			name=input("Enter name: ")
			print()
			attendence(name)
			print()
		elif tin=="4":
			showCurrentAtt()
			print()
		elif tin=="2":
			name=input("Enter name: ")
			print()
			onLeave(name)
			print()
		elif tin=="3":
			name=input("Enter name: ")
			print()
			onHalfDay(name)
			print()
		elif tin=="5":
			name=input("Enter name: ")
			print()
			checkTeacherStatus(name)
			print()
		elif tin=="6":
			name=input("Enter name: ")
			showTimetable(name)
			print()
		elif tin=="8":
			passwd=getpass.getpass(prompt="Enter Password: ")
			print()
			if passwd=="amity@123":
				print("Terminating program")
				time.sleep(3)
				break
			else:
				print("Password incorrect, access denied")
				print()
		else:
			print("Enter a valid option from 1 to 8")
			print()