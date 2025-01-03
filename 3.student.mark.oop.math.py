import math
import numpy as np
class Info:
	def __init__(self):
		self.__id= int(input("\nID: "))
		self.__name= input("Name: ")

	def list(self):
		print(f"{self.__id}\t{self.__name}")

	def get_id(self):
		return self.__id
	def get_name(self):
		return self.__name

class Course(Info):
	def __init__(self):
		super().__init__()
		self.__credit= int(input("Credit: "))

	def list(key, value):
		print(f"{key}\t{value[0]}\t{value[1]}")

	def get_credit(self):
		return self.__credit

class Student(Info):
	def __init__(self):
		super().__init__()
		self.__dob= input("Date of Birth: ")
		self.__course=[]
		self.__credit=[]
		self.__mark=[]
		self.__gpa=0

	def get_dob(self):
		return self.__dob
	def get_course(self):
		return self.__course
	def get_credit(self):
		return self.__credit
	def get_mark(self):
		return self.__mark
	def get_gpa(self):
		return self.__gpa
	
	def selectCourse(self):
		CourseID=int(input("Course ID: "))
		self.__course.append(CourseID)
		self.__credit.append(Courses[CourseID][1])
		self.__mark.append(int(input("Mark: ")))
		self.calculate_GPA()

	def calculate_GPA(self):
		total_credit= sum(self.__credit)
		if total_credit == 0:
			self.__gpa= 0
		else:
			weighted_marks= np.array(self.__mark)*np.array(self.__credit) 		#Equal array of products
			self.__gpa= math.floor(sum(weighted_marks)*10/total_credit)/10.0	#Round down to 1-digit decimal place

	def list(self):
		print(f"{self.__id}\t{self.__name}\t{self.__dob}\t{self.__credit}")

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
				temp=Student()
				Students.append(temp)
			case 2: #Add Course
				temp=Course()
				Courses.update({int(temp.get_id()):[temp.get_name(), temp.get_credit()]})
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
				order=1
				if len(Students)!=1:
					print("\nSort the list based on GPA?")
					print("1. Ascending\n2. Descending\n3. Unsorted")
					order=int(input())

				print(f"\nList of Students: ")
				print("ID\tName\tDoB\tGPA")
				#Add Student info into StudentArray
				StudentArray=np.array([[Students[0].get_id(), Students[0].get_name(), Students[0].get_dob(), Students[0].get_gpa()]])
				for i in range(1, len(Students[:])):
					temp=[Students[i].get_id(), Students[i].get_name(), Students[i].get_dob(), Students[i].get_gpa()]
					StudentArray=np.append(StudentArray,[temp],axis=0)

				if order==2: order=-1
				if order==abs(1): 
					StudentArray=StudentArray[StudentArray[:,3].argsort()[::order]]

				for row in StudentArray:
					print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

			case 6: #Display Student in a Course
				CourseID=int(input("\nEnter Course ID: "))
				for obj in Students:
					for index in range(len(obj.get_course())):
						if int(obj.get_course()[index])==(CourseID):
							print("ID\tName\tDoB\tGPA")
							print (f"{obj.get_id()}\t{obj.get_name()}\t{obj.get_dob()}\t{obj.get_mark()[index]}")
			case 7: 
				print("Exiting...")
				break
			case _: 
				print("Invalid Option") 