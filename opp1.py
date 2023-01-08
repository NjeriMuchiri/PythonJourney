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
import csv
class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity = 0):
        #Run validations to the received arguments
        assert price >= 0 
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
       
    def calculate_total_price(self):
          return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r')as f:
            reader = csv.DictReader(f) #reads content as a dictionary
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
         )
    @staticmethod         
    def is_integer(num):
        #we will count out the floats that are point zeroi.e 10.0 etc
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
       
print(Item.is_integer(7.0))
# print(Item.__dict__) #All the attribute for class level
# print(item2.__dict__)#All the attribute for instance level



