def AddStudent(StudentNum, Students):
	for i in range(StudentNum):
		print(f"\nStudent {i+1}: ")

		StudentId=int(input("Id: "))
		StudentName=input("Name: ")
		StudentDoB=input("Date of Birth: ")

		Students.append([StudentId,StudentName,StudentDoB])

def AddCourse(CourseNum, Courses, CourseDict):
	for i in range(CourseNum):
		print(f"\nCourse {i+1}: ")

		CourseId=int(input("Id: "))
		CourseName=input("Name: ")

		Courses.append([CourseId,CourseName])
		CourseDict.update({str(CourseName):[]})

def SelectCourse(StudentNum, CourseName, Students, CourseDict):
	for i in range(StudentNum):
		print(f"\nSelect Course for Student {i+1}: ")

		CourseName=input("Name: ")
		CourseMark=int(input("Mark: "))
		CourseDict[CourseName]+=[Students[i][0],Students[i][1],Students[i][2],CourseMark]	
		#Key: CourseName, Value: Students[i] (Id, Name, DoB, Mark)

def DisplayList(List, name):
	print(f"\nList of {name}: ")

	if name=="Students": 
		print("ID\tName\tDoB")
	if name=="Courses":
		print("ID\tName")

	for row in List:
		for element in row:
			print(element,end="\t")
		print("")

def DisplayStudentInCourses(CourseNum, Courses, CourseDict):
	for i in range (CourseNum):
		CourseName = Courses[i][1]
		print(f"\nCourse '{CourseName}': ")
		print("ID\tName\tDoB\tMark")	

		for j in range(4):
			print(CourseDict[CourseName][j],end="\t")
		print("")


Students=[]
Courses=[]
CourseDict={}

StudentNum= int(input("Number of Students: "))
AddStudent(StudentNum, Students)
CourseNum= int(input("\nNumber of Courses: "))
AddCourse(CourseNum, Courses, CourseDict)

SelectCourse(StudentNum, CourseNum, Students, CourseDict)

DisplayList(Students, "Students")
DisplayList(Courses, "Courses")

DisplayStudentInCourses(CourseNum, Courses, CourseDict)