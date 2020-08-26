import time
from datetime import datetime
import getpass

def attendence(name):
	if name in subjects.values():
		if int(datetime.now().strftime("%H%M"))<=800 and int(datetime.now().strftime("%H%M"))>=600:
			if teacherAttendence[name]==1 or teacherAttendence[name]==4:
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
		elif int(datetime.now().strftime("%H%M"))<=1200 and int(datetime.now().strftime("%H%M"))>=800:
			if teacherAttendence[name]==1 or teacherAttendence[name]==4:
				print("{} is already marked present".format(name))
			elif teacherAttendence[name]==2:
				print("{} is marked as on leave, do you want to mark it as present?".format(name))
				cin=input("Y/N : ")
				while True:
					if cin.lower()=="y":
						teacherAttendence[name]=4
						print("{} is now marked present (late) at {}".format(name,datetime.now().strftime("%H:%M:%S")))
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
						teacherAttendence[name]=4
						print("{} is now marked present (late) at {}".format(name,datetime.now().strftime("%H:%M:%S")))
						break
					elif cin.lower()=="n":
						print("{} is marked on half day".format(name))
						break
					else:
						print("Enter Y for \'yes\' and N for \'no\'")
			else:
				teacherAttendence[name]=4
				print("{} marked present (late) at {}".format(name,datetime.now().strftime("%H:%M:%S")))
	else:
		print("Name not found in record, try capitalizing initials of your name")

def onLeave(name):
	if name in subjects.values():
		if teacherAttendence[name]==1 or teacherAttendence[name]==4:
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
			if teacherAttendence[name]==1 or teacherAttendence[name]==4:
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
		elif teacherAttendence[i]==4:
			c="Present (late)"
		else:
			c="Absent"
		print("{} is {}".format(i,c))


def checkTeacherStatus(name):
	if name in teacherAttendence:
		print("{} teaches {}".format(name,list(subjects.keys())[list(subjects.values()).index(name)]))
		if teacherAttendence[name]==1:
			print("{} is present".format(name))
		elif teacherAttendence[name]==2:
			print("{} is on leave".format(name))
		elif teacherAttendence[name]==3:
			print("{} is on half day".format(name))
		elif teacherAttendence[name]==4:
			print("{} is present (late)".format(name))
		else:
			print("{} is Absent".format(name))
		if teacherAttendence[name]==1 or teacherAttendence[name]==4:
			a=teacherCode[name]
			if a=="CSG":
				CSG={"Monday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Tuesday":[0,0,'12-C','12-C','12-A','12-A',0,0],"Wednesday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Thursday":['12-B','12-B',0,0,'12-A','12-A','12-C','12-C'],"Friday":[0,0,'12-A','12-A','12-B','12-B',0,0]}
				i=datetime.now().strftime("%A")
				if i in CSG:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						print("Period 1 in {}".format(CSG[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						print("Period 2 in {}".format(CSG[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						print("Period 3 in {}".format(CSG[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						print("Period 4 in {}".format(CSG[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						print("Period 5 in {}".format(CSG[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						print("Period 6 in {}".format(CSG[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						print("Period 7 in {}".format(CSG[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						print("Period 8 in {}".format(CSG[i][7]))
					else:
						print("Data for current time not available")
				else:
					print("Name not found in record, try capitalizing initials of your name")
			if a=="PLD":
				PLD={"Monday":['12-B','12-B','12-C','12-C',0,0,'12-A','12-A'],"Tuesday":['12-A','12-A','12-C','12-C',0,0,0,0],"Wednesday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Thursday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Friday":[0,0,0,0,'12-A','12-A','12-B','12-B']}
				i=datetime.now().strftime("%A")
				if i in PLD:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						print("Period 1 in {}".format(PLD[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						print("Period 2 in {}".format(PLD[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						print("Period 3 in {}".format(PLD[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						print("Period 4 in {}".format(PLD[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						print("Period 5 in {}".format(PLD[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						print("Period 6 in {}".format(PLD[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						print("Period 7 in {}".format(PLD[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						print("Period 8 in {}".format(PLD[i][7]))
					else:
						print("Data for current time not available")
				else:
					print("Name not found in record, try capitalizing initials of your name")
			if a=="MVK":
				MVK={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[0,0,1,1,0,0,1,1],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[1,1,0,0,1,1,1,1]}
				i=datetime.now().strftime("%A")
				if i in MVK:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						print("Period 1 in {}".format(MVK[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						print("Period 2 in {}".format(MVK[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						print("Period 3 in {}".format(MVK[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						print("Period 4 in {}".format(MVK[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						print("Period 5 in {}".format(MVK[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						print("Period 6 in {}".format(MVK[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						print("Period 7 in {}".format(MVK[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						print("Period 8 in {}".format(MVK[i][7]))
					else:
						print("Data for current time not available")
				else:
					print("Name not found in record, try capitalizing initials of your name")
			if a=="CSHG":
				CSHG={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[1,1,0,0,1,1,0,0],"Wednesday":[0,0,1,1,0,0,1,1],"Thursday":[1,1,0,0,0,0,1,1],"Friday":[1,1,1,1,1,1,0,0]}
				i=datetime.now().strftime("%A")
				if i in CSHG:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						print("Period 1 in {}".format(CSHG[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						print("Period 2 in {}".format(CSHG[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						print("Period 3 in {}".format(CSHG[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						print("Period 4 in {}".format(CSHG[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						print("Period 5 in {}".format(CSHG[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						print("Period 6 in {}".format(CSHG[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						print("Period 7 in {}".format(CSHG[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						print("Period 8 in {}".format(CSHG[i][7]))
					else:
						print("Data for current time not available")
				else:
					print("Name not found in record, try capitalizing initials of your name")
			if a=="ESB":
				ESB={"Monday":[1,1,0,0,1,1,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[0,0,1,1,0,0,1,1],"Friday":[0,0,1,1,0,0,1,1]}
				i=datetime.now().strftime("%A")
				if i in MVK:
					if int(datetime.now().strftime("%H%M"))>850 and int(datetime.now().strftime("%H%M"))<=925:
						print("Period 1 in {}".format(ESB[i][0]))
					elif int(datetime.now().strftime("%H%M"))>925 and int(datetime.now().strftime("%H%M"))<=1000:
						print("Period 2 in {}".format(ESB[i][1]))
					elif int(datetime.now().strftime("%H%M"))>1000 and int(datetime.now().strftime("%H%M"))<=1035:
						print("Period 3 in {}".format(ESB[i][2]))
					elif int(datetime.now().strftime("%H%M"))>1035 and int(datetime.now().strftime("%H%M"))<=1110:
						print("Period 4 in {}".format(ESB[i][3]))
					elif int(datetime.now().strftime("%H%M"))>1130 and int(datetime.now().strftime("%H%M"))<=1205:
						print("Period 5 in {}".format(ESB[i][4]))
					elif int(datetime.now().strftime("%H%M"))>1205 and int(datetime.now().strftime("%H%M"))<=1240:
						print("Period 6 in {}".format(ESB[i][5]))
					elif int(datetime.now().strftime("%H%M"))>1240 and int(datetime.now().strftime("%H%M"))<=1315:
						print("Period 7 in {}".format(ESB[i][6]))
					elif int(datetime.now().strftime("%H%M"))>1315 and int(datetime.now().strftime("%H%M"))<=1350:
						print("Period 8 in {}".format(ESB[i][7]))
					else:
						print("Data for current time not available")
				else:
					print("Name not found in record, try capitalizing initials of your name")
		else:
			print("{} is not available today at school".format(name))
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
		elif teacherAttendence[i]==4:
			f.write("{} is present (late)".format(i))
		else:
			f.write("{} is absent".format(i))
		f.write("\n")
	f.close()


def showTimetable(name):
	if name in teacherCode:
		a=teacherCode[name]
		if a=="CSG":
			CSG={"Monday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Tuesday":[0,0,'12-C','12-C','12-A','12-A',0,0],"Wednesday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Thursday":['12-B','12-B',0,0,'12-A','12-A','12-C','12-C'],"Friday":[0,0,'12-A','12-A','12-B','12-B',0,0]}
			i=datetime.now().strftime("%A")
			if i in CSG:
				b=1
				for j in CSG[i]:
					if j!=0:
						print("Period {} in class {}".format(b,j))
					else:
						print("Period {} is free".format(b))
					b=b+1
			else:
				print("Today is a weekend, timetable not available")
		elif a=="PLD":
			PLD={"Monday":['12-B','12-B','12-C','12-C',0,0,'12-A','12-A'],"Tuesday":['12-A','12-A','12-C','12-C',0,0,0,0],"Wednesday":['12-B','12-B',0,0,'12-C','12-C',0,0],"Thursday":['12-C','12-C','12-A','12-A',0,0,'12-B','12-B'],"Friday":[0,0,0,0,'12-A','12-A','12-B','12-B']}
			i=datetime.now().strftime("%A")
			if i in PLD:
				b=1
				for j in PLD[i]:
					if j!=0:
						print("Period {} in class {}".format(b,j))
					else:
						print("Period {} is free".format(b))
					b=b+1
			else:
				print("Today is a weekend, timetable not available")
		elif a=="MVK":
			MVK={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[0,0,1,1,0,0,1,1],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[1,1,1,1,0,0,1,1],"Friday":[1,1,0,0,1,1,1,1]}
			i=datetime.now().strftime("%A")
			if i in MVK:
				b=1
				for j in MVK[i]:
					if j!=0:
						print("Period {} in class {}".format(b,j))
					else:
						print("Period {} is free".format(b))
					b=b+1
			else:
				print("Today is a weekend, timetable not available")
		elif a=="CSHG":
			CSHG={"Monday":[1,1,0,0,0,0,1,1],"Tuesday":[1,1,0,0,1,1,0,0],"Wednesday":[0,0,1,1,0,0,1,1],"Thursday":[1,1,0,0,0,0,1,1],"Friday":[1,1,1,1,1,1,0,0]}
			i=datetime.now().strftime("%A")
			if i in CSHG:
				b=1
				for j in CSHG[i]:
					if j!=0:
						print("Period {} in class {}".format(b,j))
					else:
						print("Period {} is free".format(b))
					b=b+1
			else:
				print("Today is a weekend, timetable not available")
		elif a=="ESB":
			ESB={"Monday":[1,1,0,0,1,1,1,1],"Tuesday":[1,1,1,1,0,0,0,0],"Wednesday":[1,1,1,1,0,0,0,0],"Thursday":[0,0,1,1,0,0,1,1],"Friday":[0,0,1,1,0,0,1,1]}
			i=datetime.now().strftime("%A")
			if i in ESB:
				b=1
				for j in ESB[i]:
					if j!=0:
						print("Period {} in class {}".format(b,j))
					else:
						print("Period {} is free".format(b))
					b=b+1
			else:
				print("Today is a weekend, timetable not available")
		else:
			print("Name not found in record, try capitalizing initials of your name")
	else:
		print("Name not found in record, try capitalizing initials of your name")

subjects={"Chemistry":"Sadhvi Gautam","Physics":"Liji Davis","Maths":"Vipin Kumar","CS":"Halina Gupta","English":"Sudhi Bhatia"}
teacherAttendence={"Sadhvi Gautam":0,"Liji Davis":0,"Vipin Kumar":0,"Halina Gupta":0,"Sudhi Bhatia":0}
teacherCode={"Sadhvi Gautam":"CSG","Liji Davis":"PLD","Vipin Kumar":"MVK","Halina Gupta":"CSHG","Sudhi Bhatia":"ESB"}

print()
print('''
   _____ _               _ _____       
  / ____| |             | |  __ \      
 | (___ | | _____   ___ | | |__) |   _ 
  \___ \| |/ / _ \ / _ \| |  ___/ | | |
  ____) |   < (_) | (_) | | |   | |_| |
 |_____/|_|\_\___/ \___/|_|_|    \__, |
                                  __/ |
                                 |___/ 
                                 ''')
time.sleep(3)
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
print("8. SkoolPy Info")
print("9. Exit")
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
			print("Cannot mark on half day after 12:00 PM")
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
			print('''SkoolPy is a School Management System, made using python\nand is available as a CLI and a GUI.\n\nIt is an Open-Source software and free to use\nMade by Devansh Singh\n\nView the source code on: https://github.com/Devansh3712/SkoolPy\n''')
		elif tin=="9":
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
			print("Enter a valid option from 1 to 9")
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
			print('''SkoolPy is a School Management System, made using python\nand is available as a CLI and a GUI.\n\nIt is an Open-Source software and free to use\nMade by Devansh Singh\n\nView the source code on: https://github.com/Devansh3712/SkoolPy\n''')
		elif tin=="9":
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
			print("Enter a valid option from 1 to 9")
			print()
