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
    pay_rate = 0.8 #pay rate after 20% discount
    def __init__(self,name: str, price: float, quantity = 0):
           #Run validations to the received arguments
        assert price >= 0
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
       
    def calculate_total_price(self):
          return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
       
item1 = Item('Iphone',1000,5)
item2 = Item('laptop',10000,2)
item3 = Item('cable',100,4)
item4 = Item('Mouse',160,3)
item5= Item('keyboard',150,4)


# print(Item.__dict__) #All the attribute for class level
# print(item2.__dict__)#All the attribute for instance level



