import math
import numpy as np


class Info:
	def __init__(self):
		self._id= int(input("\nID: "))
		self._name= input("Name: ")
	def get_id(self):
		return self._id
	def get_name(self):
		return self._name

class Course(Info):
	def __init__(self):
		super().__init__()
		self.__credit= int(input("Credit: "))
		fCourse = open("courses.txt", "a")
		fCourse.write(f"{self._id}\t{self._name}\t{self.__credit}\n")
		fCourse.close()
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
		fStudent = open("students.txt", "a")
		fStudent.write(f"{self._id}\t{self._name}\t{self.__dob}\n")
		fStudent.close()

	def selectCourse(self, Courses):
		CourseID=int(input("Course ID: "))
		self.__course.append(CourseID)
		self.__credit.append(Courses[CourseID][1])
		self.__mark.append(int(input("Mark: ")))
		self.calculate_GPA()
		fMark = open("marks.txt", "a")
		fMark.write(f"{self._id}\t{self._name}\t{self.__course}\t{self.__credit}\t{self.__mark}{self.__gpa}\n")
		fMark.close()

	def calculate_GPA(self):
		total_credit= sum(self.__credit)
		if total_credit == 0:
			self.__gpa= 0
		else:
			weighted_marks= np.array(self.__mark)*np.array(self.__credit) 		#Equal array of products
			self.__gpa= math.floor(sum(weighted_marks)*10/total_credit)/10.0	#Round down to 1-digit decimal place
	
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