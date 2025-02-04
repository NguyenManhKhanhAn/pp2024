import input as inp
import output as out

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
				temp=inp.Student()
				Students.append(temp)
			case 2: #Add Course
				temp=inp.Course()
				Courses.update({int(temp.get_id()):[temp.get_name(), temp.get_credit()]})
			case 3: #Select Course
				StID= int(input("\nSelect Course for Student ID: "))
				for obj in Students:
					if obj.get_id()==StID:
						obj.selectCourse(Courses)
			case 4: #Display Courses
				out.List_Course(Courses)
			case 5: #Display Students
				out.List_Student(Students)
			case 6: #Display Student in a Course
				out.List_Students_Course(Students)
			case 7: 
				print("Exiting...")
				break
			case _: 
				print("Invalid Option") 