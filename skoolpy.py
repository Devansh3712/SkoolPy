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
					print("{} is now marked present".format(name))
					break
				elif cin.lower()=="n":
					print("{} is marked on leave".format(name))
					break
				else:
					print("Enter Y for yes and N for no")
		else:
			teacherAttendence[name]=1
			print("{} marked present".format(name))
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
					print("{} is now marked on leave".format(name))
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
			print("{} marked on leave".format(name))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def showCurrentAtt():
	if i in teacherAttendence:
		for i in teacherAttendence:
			if teacherAttendence[i]==1:
				c="Present"
			elif teacherAttendence[i]==2:
				c="On Leave"
			else:
				c="Absent"
			print("{} is {}".format(i,c))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def checkTeacherStatus(name):
	if i in teacherAttendence:
		for i in teacherAttendence:
			if i==name:
				print("{} teaches {}".format(name,list(subjects.keys())[list(subject.values()).index(i)]))
				if teacherAttendence[i]==1:
					print("{} is present".format(name))
				elif teacherAttendence[i]==2:
					print("{} is on leave".format(name))
				else:
					print("{} is Absent".format(name))
	else:
		print("Name not found in record, try capitalizing initials of your name")

subjects={"Chemistry":"Sadhvi Gautam","Physics":"Liji Davis","Maths":"Vipin Kumar","CS":"Halina Gupta","English":"Sudhi Bhatia"}
teacherAttendence={"Sadhvi Gautam":0,"Liji Davis":0,"Vipin Kumar":0,"Halina Gupta":0,"Sudhi Bhatia":0}


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
