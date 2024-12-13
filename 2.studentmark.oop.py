class Info:
	def __init__(self):
		Id= int(input("Id: "))
		Name= input("Name: ")
		self.id= Id
		self.name= Name
		
	def list(self, type):
		print(f"\nList of {type}: ")
		if type== "Student":
			print("ID\tName\tDoB")
			print(f"{self.id}\t{self.name}\t{self.dob}")
		if type== "Course":
			print("ID\tName")
			print(f"{self.id}\t{self.name}")
			

class Student(Info):
	def __init__(self):
		super().__init__()
		self.dob= input("Date of Birth: ")
	def selectCourse(self):
		self.course= input("Name: ")
		self.mark= int(input("Mark: "))
	def list(self):
		super().list("Student")

class Course(Info):
	def list(self):
		super().list("Course")

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

StudentNum= int(input("\nNumber of Students: "))
for i in range (StudentNum):
	Students.append(Student())
CourseNum= int(input("\nNumber of Courses: "))
for i in range (CourseNum):
	Courses.append(Course())

for object in Students:
	object.list()