import time
from datetime import datetime

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
					print("Enter Y for yes and N for no")
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
					print("Enter Y for yes and N for no")
		elif teacherAttendence[name]==2:
			print("{} is already marked on leave".format(name))
		else:
			teacherAttendence[name]=2
			print("{} marked on leave at {}".format(name,datetime.now().strftime("%H:%M:%S")))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def showCurrentAtt():
	for i in teacherAttendence:
		if teacherAttendence[i]==1:
			c="Present"
		elif teacherAttendence[i]==2:
			c="On Leave"
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
		else:
			f.write("{} is absent".format(i))
		f.write("\n")
	f.close()

subjects={"Chemistry":"Sadhvi Gautam","Physics":"Liji Davis","Maths":"Vipin Kumar","CS":"Halina Gupta","English":"Sudhi Bhatia"}
teacherAttendence={"Sadhvi Gautam":0,"Liji Davis":0,"Vipin Kumar":0,"Halina Gupta":0,"Sudhi Bhatia":0}

CSG={"Monday":[1,1,0,0,1,1,0,0],"Tuesday":[0,0,1,1,1,1,0,0],"Wednesday":[1,1,1,1,0,0,1,1],"Thursday":[1,1,0,0,1,1,1,1],"Friday":[0,0,1,1,1,1,0,0]}
PLD={"Monday":[1,1,1,1,0,0,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,0,0,1,1,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[0,0,0,0,1,1,1,1]}
MVK={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[0,0,1,1,0,0,1,1],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[1,1,0,0,1,1,1,1]}
CSHG={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[1,1,0,0,1,1,0,0],"Wednesday":[0,0,1,1,0,0,1,1],"Thursday":[1,1,0,0,0,0,1,1],"Friday":[1,1,1,1,1,1,0,0]}
ESB={"Monday":[1,1,0,0,1,1,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[0,0,1,1,0,0,1,1],"Friday":[0,0,1,1,0,0,1,1]}

print()
print(">>> School Management System <<<")
print()
print(">>> "+datetime.now().strftime("%B %d, %Y %H:%M:%S")+" <<<")

while True:
	print()
	print("1. Add your attendence")
	print("2. Show today's current attendence")
	print("3. Mark a teacher on leave")
	print("4. Show a teacher's status")
	print("5. Show a teacher's timetable")
	print("6. Add subsitution")
	print("7. Exit")
	print()
	tin=input("Type the option to proceed: ")
	print()
	if datetime.now().strftime("%H:%M")=="12:00":
		writeAttendence()
	elif int(datetime.now().strftime("%H%M"))>1200:
		if tin=="1":
			print("Cannot mark attendence after 12:00")
		elif tin=="2":
			showCurrentAtt()
		elif tin=="3":
			print("Cannot mark on leave after 12:00")
		elif tin=="4":
			name=input("Enter name: ")
			print()
			checkTeacherStatus(name)
		elif tin=="7":
			print("Terminating program")
			break
		else:
			print("Enter a valid option from 1 to 7")
	elif int(datetime.now().strftime("%H%M"))<600:
		print("Attendence and other status cannot be shown now, try after 6:00 AM")
	else:
		if tin=="1":
			name=input("Enter name: ")
			print()
			attendence(name)
		elif tin=="2":
			showCurrentAtt()
		elif tin=="3":
			name=input("Enter name: ")
			print()
			onLeave(name)
		elif tin=="4":
			name=input("Enter name: ")
			print()
			checkTeacherStatus(name)
		elif tin=="7":
			print("Terminating program")
			break
		else:
			print("Enter a valid option from 1 to 7")