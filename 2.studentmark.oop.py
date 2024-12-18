class Info:
	def __init__(self):
		self.id= int(input("Id: "))
		self.name= input("Name: ")
		
	def list(self, type):
		if type== "Student":
			print(f"{self.id}\t{self.name}\t{self.dob}")
		if type== "Course":
			print(f"{self.id}\t{self.name}")
			
class Course(Info):
	def __init__(self):
		super().__init__()
		CourseDict.update({str(self.name):[]})

	def list(self):
		super().list("Course")

	def studentList(self):
		print(f"\nCourse '{self.name}': ")
		print("ID\tName\tDoB\tMark")	
		for j in range(4):
			print(CourseDict[self.name][j],end="\t")


class Student(Info):
	def __init__(self):
		super().__init__()
		self.dob= input("Date of Birth: ")

	def selectCourse(self):
		self.course= input("Name: ")
		self.mark= float(input("Mark: "))
		CourseDict[self.course]+=[self.id, self.name, self.dob, self.mark]
	
	def list(self):
		super().list("Student")


Students=[]
Courses=[]
CourseDict={}

for i in range (int(input("\nNumber of Students: "))):
	Students.append(Student())
for i in range (int(input("\nNumber of Courses: "))):
	Courses.append(Course())

print(f"\nList of Students: ")
print("ID\tName\tDoB")
for obj in Students:
	obj.list()

print(f"\nList of Courses: ")
print("ID\tName")
for obj in Courses:
	obj.list()

for obj in Students:
	print(f"\nSelect Course for Student ID {obj.id}: ")
	obj.selectCourse()

for obj in Courses:
	obj.studentList()
