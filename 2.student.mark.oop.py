class Info:
	def __init__(self):
		self.id= int(input("ID: "))
		self.name= input("Name: ")
	def list(self):
		print(f"{self.id}\t{self.name}")
	def get_id(self):
		return self.id
	def get_name(self):
		return self.name

class Course(Info):
	def list(key, value):
		print(f"{key}\t{value}")

class Student(Info):
	def __init__(self):
		super().__init__()
		self.dob= input("Date of Birth: ")
		self.course=""
		self.mark=0
	def get_course(self):
		return self.course
	def get_mark(self):
		return self.mark
	def selectCourse(self):
		self.course= input("Course ID: ")
		self.mark= float(input("Mark: "))
	def list(self):
		print(f"{self.id}\t{self.name}\t{self.dob}")


if __name__=="__main__":
	Students=[]
	Courses={}

	while True:
		print ("\nSelect one:")
		print ("1. Add Student")
		print ("2. Add Course")
		print ("3. Select Course")
		print ("4. Display Courses")
		print ("5. Display Students")
		print ("6. Display Students in a Course")
		print ("7. Exit\n")
		action= int(input())
		match action:
			case 1:
				Students.append(Student())
			case 2: 
				temp=Course()
				Courses.update({(temp.id):temp.name})
			case 3: #
				StID= int(input("\nSelect Course for Student ID: "))
				for obj in Students:
					if obj.id==StID:
						obj.selectCourse()
						obj.course=obj.get_course()
						obj.mark=obj.get_mark()
			case 4:
				print(f"\nList of Courses: ")
				print("ID\tName")
				for key, value in Courses.items():
					Course.list(key, value)
			case 5:
				print(f"\nList of Students: ")
				print("ID\tName\tDoB")
				for obj in Students:
					obj.list()
			case 6: #
				CourseID=int(input("\nEnter Course ID: "))
				for obj in Students:
					if int(obj.course)==(CourseID):
						print (f"{obj.id}\t{obj.name}\t{obj.dob}\t{obj.mark}")
			case 7: 
				print("Exiting...")
				break
			case _: 
				print("Invalid Option")
				for obj in Students:
					print(f"{obj.id}\t{obj.name}\t{obj.dob}\t{obj.course}\t{obj.mark}")