StudentNum= int(input("Number of Students: "))
Students=[]
for i in range(StudentNum):
	print(f"\nStudent {i+1}: ")

	StudentId=int(input("Id: "))
	StudentName=input("Name: ")
	StudentDoB=input("Date of Birth: ")

	Students.append([StudentId,StudentName,StudentDoB])

CourseDict={}
CourseNum= int(input("\nNumber of Courses: "))
Courses=[]
for i in range(CourseNum):
	print(f"\nCourse {i+1}: ")

	CourseId=int(input("Id: "))
	CourseName=input("Name: ")

	Courses.append([CourseId,CourseName])
	CourseDict.update({str(CourseName):[]})

for i in range(StudentNum):
	print(f"\nSelect Course for Student {i+1}: ")

	CourseName=input("Name: ")
	CourseMark=int(input("Mark: "))
	CourseDict[CourseName]+=[Students[i][0],Students[i][1],Students[i][2],CourseMark]	
	#Key: CourseName, Value: Students[i] (Id, Name, DoB, Mark)

print("\nList of Students: ")
print("ID\tName\tDoB")
for row in Students:
	for element in row:
		print(element,end="\t")
	print("")

print("\nList of Courses: ")
print("ID\tName")
for row in Courses:
	for element in row:
		print(element,end="\t")
	print("")

for i in range(CourseNum):
	print(f"\nCourse '{Courses[i][1]}': ")
	print("ID\tName\tDoB\tMark")
	for j in range(4):
		print(CourseDict[Courses[i][1]][j],end="\t")
	print("")