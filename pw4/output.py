#import input
import numpy as np

class Info:
	def list(self):
		print(f"{self.__id}\t{self.__name}")

	def get_id(self):
		return self.__id
	def get_name(self):
		return self.__name

class Course(Info):
	def list(key, value):
		print(f"{key}\t{value[0]}\t{value[1]}")

	def get_credit(self):
		return self.__credit

class Student(Info):
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

	def list(self):
		print(f"{self.__id}\t{self.__name}\t{self.__dob}\t{self.__credit}")

def List_Course(Courses):
	print(f"\nList of Courses: ")
	print("ID\tName")
	for key, value in Courses.items():
		input.Course.list(key, value)

def List_Student(Students):
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

def List_Students_Course(Students):
    CourseID=int(input("\nEnter Course ID: "))
    for obj in Students:
        for index in range(len(obj.get_course())):
            if int(obj.get_course()[index])==(CourseID):
                print("ID\tName\tDoB\tGPA")
                print (f"{obj.get_id()}\t{obj.get_name()}\t{obj.get_dob()}\t{obj.get_mark()[index]}")