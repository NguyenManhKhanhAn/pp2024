class Info:
	def __init__(self):
		self.__id= int(input("ID: "))
		self.__name= input("Name: ")

	def list(self):
		print(f"{self.__id}\t{self.__name}")

	def get_id(self):
		return self.__id
	def get_name(self):
		return self.__name

class Course(Info):
	def list(key, value):
		print(f"{key}\t{value}")

class Student(Info):
	def __init__(self):
		super().__init__()
		self.__dob= input("Date of Birth: ")
		self.__course=""
		self.__mark=0

	def get_course(self):
		return self.__course
	def get_mark(self):
		return self.__mark
	def list(self):
		print(f"{self.__id}\t{self.__name}\t{self.__dob}")
	
	def selectCourse(self):
		self.__course= input("Course ID: ")
		self.__mark= float(input("Mark: "))


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
			case 1: #Add Student
				Students.append(Student())
			case 2: #Add Course
				temp=Course()
				Courses.update({(temp.get_id()):temp.get_name()})
			case 3: #Select Course
				StID= int(input("\nSelect Course for Student ID: "))
				for obj in Students:
					if obj.get_id()==StID:
						obj.selectCourse()
			case 4: #Display Courses
				print(f"\nList of Courses: ")
				print("ID\tName")
				for key, value in Courses.items():
					Course.list(key, value)
			case 5: #Display Students
				print(f"\nList of Students: ")
				print("ID\tName\tDoB")
				for obj in Students:
					obj.list()
			case 6: #Display Student in a Course
				CourseID=int(input("\nEnter Course ID: "))
				for obj in Students:
					if int(obj.get_course())==(CourseID):
						print (f"{obj.get_id()}\t{obj.get_name()}\t{obj.get_dob()}\t{obj.get_mark()}")
			case 7: 
				print("Exiting...")
				break
			case _: 
				print("Invalid Option")