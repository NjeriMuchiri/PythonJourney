class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self,course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        pass
    
s1 = Student("Kahsee", 23, 97 )
s2 = Student("Kaggy", 20, 90)
s3 = Student("Kashii", 27, 87 )
   
course = Course("Informatics", 2)
course.add_student(s1)
course.add_student(s2)         

print(course.students)       
        