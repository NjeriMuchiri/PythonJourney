#welcome quotes.
print(("Hello Kashee, Welcome to Python!"))

#function of a newline
def new_line():
    print('\n')
new_line()
#variables , and are case sensitive
x = "Kashee"
x = 23
print(x)

new_line()
#naming variables #camelCase
myNameIs = "Kashee"
print(myNameIs)
#PascalCase
MyNameIs = "Kashee"
print(MyNameIs)
#Snake__Case
my_name_is = "Kashee"
print(my_name_is)
new_line()
#casting
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

new_line()
#Get the type
x = 5
y = "John"
print(type(x))
print(type(y))
new_line()
#Assigning multiple values
x, y, z = "Bananas", "Kiwi", "Ovacados"
print(x)
print(y)
print(z)
new_line()
#One value to multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
new_line()
#Unpack a collection
friends = ['Ken', 'Cynthie', 'Karimi']
x, y, z = friends
print(x)
print(y)
print(z)
new_line()
x = "Kashee"
y = "is"
z = "awesome"
print(x, y, z) #comma supports different data types
print(x + y + z)
#print(x, y, z == z + y + x)
new_line()
#Global variable - Variable outside of a function and use it inside a function
x = "Awesome"
def mydefau():
    x = "Fantastic"
    print("Kashee is", x)
    print("Kashee is " + x)
mydefau()

print("Kashee is " + x)
new_line()
#to change a value of a global variable iside a function refer the global variable
x = "Awesome"
def mydefau():
    global x
    x = "Fantastic"
    print("Kashee is", x)
    print("Kashee is " + x)
mydefau()

print("Kashee is " + x)
new_line()
#Creating a local variable using global keyword to make it global
def myfunc():
    global x
    x = "Vital"
myfunc()

print("Kashee is defined as being " + x)
print("Kashee is defined as being", x)
new_line()
#datatype
x = ("apple", "banana", "kiwi") #tuple
print(type(x))
new_line()
x = ["apple", "banana", "kiwi"] #list
print(type(x))
new_line()
x = {"apple", "banana", "kiwi"} #set
print(type(x))
new_line()
x = frozenset({"apple", "banana", "kiwi"}) #frozenset
print(type(x))
new_line()
x = {"name": "John", "age": 57} #dict
print(type(x))
new_line()
x = 5j #complex
print(type(x)) 
new_line()
x = range(6) #range
print(type(x))
new_line()
x = b"Hello"
print(type(x)) #bytes
new_line()
x = bytearray(6) #bytearray
print(type(x))
new_line()
x = memoryview(bytes(5)) #memoryview
print(type(x))
new_line()
x = None
print(type(x)) #NoneType
new_line()
# float with scientific e to specify to power 10
x = 35e3 #float
print(type(x))
new_line()
x = 1
y = 2.8
z = 5j

print(x == z) #false
new_line()
x = 3 + 5j
y = 1j
z = -6j

print(x)
print(type(x))
print(type(y))
print(type(z))
new_line()
#conversion  #complex cant be converted into other numbers type
x = 5j
y = 2.8
z = 7

b = int(y)
print(y)
c = complex(y)
print(y)
d = float(z)
print(z)

print(type(b))
print(type(c))
print(type(d))
new_line()
#random numbers, In python we use a built in module called random
import random
print(random.randrange(1, 10))
new_line()
#strings #getting a specific array in the string
a = "Hello Kashee!"
print(a[12]) #!
new_line()
#loop thru a string,since strings are arrays
for x in "Kashee":
    print(x)
#string length
a  = "Kashee,Welcome to Python gal!"
print(len(a))
new_line()
#checking if a character is present with in keyword
sentence = "The best things that happen in life,happen randomly"
if "randomly" in sentence:
    print("Am Present!!!") 
else:
    print("Am Absent!")
new_line()
#not in keywords
sent = "Commitment and Dedication and Consistency award you with what you want in life! "
if "Kashee" not in sent:
    print("Am Invisible!") 
new_line()
#Slicing - returns a range of characters
b = "Hello, Kashee!!!"
print(b[2:5]) #returns position 2 to 5(not included,5)
print(b[:5]) #returns characters from the start to position 5(not included)
print(b[:-5]) #returns characters from end to start (the 5th being the first letter)
print(b[:-6])
new_line()
#slice to the end
b = "Hello Python"
print(b[2:]) #slices from the start without the 2nd array included
#Modify Strings
q = " Enjoying Python Syntax "
print(q.upper()) #uppercase
print(q.lower()) #lowercase
print(q.strip()) #removes the whitespace
print(q.replace("Enjoying", "Fun")) #replaces a string with another
print(q.split(",")) #splits strings
new_line()
#string Conactenation
a = "Availability"
b = "is not"
c = "reliability"
z = a +  " " + b + " " + c

print(z)
new_line()
#we can combine str and int with the the format() method
#format()
age = 23
quo = "NjeriMuchiri is Consistent,Dedicated and Committed to achieve her goals at {}"
print(quo.format(age))
new_line()

quantity = 1
item = "car"
price = 2,000,000
mygoal = "I want to own {} Volvo {}, which costs {} "
print(mygoal.format(quantity,item,price))
new_line()
# \ backslash is an escape character
txt = " \"Philipians 1:3\" I thank my God anytime I remember You"
print(txt)

print("How old are you?", end= ' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy.")






