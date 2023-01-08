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
    def __init__(self,name,price,quantity = 0):
        print(f" An instance created:{name}")
        self.name = name
        self.price = price
        self.quantity = quantity
       
    def calculate_total_price(self):
          return self.price * self.quantity
    
       
item1 = Item('Iphone',100,3)
item2= Item('laptop',100,4)

print(item1.calculate_total_price())
print(item2.calculate_total_price())



