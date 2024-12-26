class Info:
	CourseDict={}
	def __init__(self, id, name):
		self.id= id
		self.name= name
		
	def list(self, type):
		if type== "Student":
			print(f"{self.id}\t{self.name}\t{self.dob}")
		if type== "Course":
			print(f"{self.id}\t{self.name}")
			
class Course(Info):
	Courses=[]
	def __init__(self, id, name):
		super().__init__(id, name)
		Course.Courses.append(self)
		Info.CourseDict.update({str(self.name):[]})
		print("")

	def list(self):
		super().list("Course")

	def studentList(self):
		print(f"\nCourse '{self.name}': ")
		print("ID\tName\tDoB\tMark")	
		for i in range(1,Info.CourseDict[self.name][0]+1):
			for j in range(4):
				print(Info.CourseDict[self.name][i][j],end="\t")
			print("")


class Student(Info):
	Students=[]
	def __init__(self, id, name, dob):
		super().__init__(id, name)
		self.dob= dob
		Student.Students.append(self)
		print("")

	def selectCourse(self):
		self.course= input("Name: ")
		self.mark= float(input("Mark: "))
		if bool(not Info.CourseDict[self.course]): Info.CourseDict[self.course]+=[1]
		else: Info.CourseDict[self.course][0]+=1
		Info.CourseDict[self.course]+=[[self.id, self.name, self.dob, self.mark]]
	
	def list(self):
		super().list("Student")


for i in range (int(input("\nNumber of Students: "))):
	Student(int(input("Id: ")), input("Name: "), input("Date of Birth: "))
for i in range (int(input("\nNumber of Courses: "))):
	Course(int(input("Id: ")), input("Name: "))

print(f"\nList of Students: ")
print("ID\tName\tDoB")
for obj in Student.Students:
	obj.list()

print(f"\nList of Courses: ")
print("ID\tName")
for obj in Course.Courses:
	obj.list()

for obj in Student.Students:
	print(f"\nSelect Course for Student ID {obj.id}: ")
	obj.selectCourse()

for obj in Course.Courses:
	obj.studentList()
