# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
    
#     def get_grade(self):
#         return self.grade
    
# class Course:
#     def __init__(self,course_name, max_students):
#         self.course_name = course_name
#         self.max_students = max_students
#         self.students = []
    
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
    
# s1 = Student("Kashee", 23, 97 )
# s2 = Student("Kaggy", 20, 90)
# s3 = Student("Kashii", 27, 87 )
   
# course = Course("Informatics", 2)
# course.add_student(s1)
# course.add_student(s2)         
      
# print(course.get_average_grade())     

# oop2
class Item:
    def calculate_total_price(self, x, y):
          return x * y
    
    
    
    
    
item1 = Item()
item1.name = "IPhone"
item1.price = 140000
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2= Item()
item2.name = "laptop"
item2.price = 100000
item2.quantity = 5
print(item2.calculate_total_price(item2.price, item2.quantity))
