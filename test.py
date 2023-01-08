def listSkills(val, list=[]):
    list.append(val)
    return list
list1 = listSkills('nodeJs')
list2 = listSkills('Java', [])
list3 = listSkills('React')
print("%s" % list1)
print("%s" % list2)
print("%s" % list3)
# answer
# ['nodeJs', 'React']
# ['Java]
# ['nodeJS','React']
def new_line():
    print('\n')
new_line()


skills = ['Node', 'pyth', 'React', 'vue js']
skills.insert(3, 'Java') #answer
print(skills)
new_line()

print([i.lower() for i in "TURING"])
# ['t','u','r','i','n','g'] #answer
new_line()

a = [1,2,3,4]
b = [sum(a[0:x + 1]) for x in range(0, len(a))]
print(b)
# [1,3,6,10] #answer
new_line()

z = set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)
#{'p','b','q','san','c','a'} #answer
new_line()


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
        print(l)
f(2)
f(3, [3,2,1])
f(3)
# [0,1]
# [3,2,1,0,1,4]
# [0,1,0,1,4]    #answer
new_line()
# x = 'abcdef'
# i = 'a'
# while i in x[:-1]: 
#    print(i, end="")  #prints infinitely a
new_line()
data = [1,2,3]
def incr(x):
    return x + 1
print(list(map(incr, data)))
# [2,3,4] #answer
new_line()
# def func1():
#     x = 50
#     return x
# func1()
# print(x)
# answer is x is not defined 


f = None
for i in range(5):
    with open("app.log", "w") as f:
        if i > 2:
            break
print(f.closed) #answer is #True
new_line()

print(2**(3**2), (2**3)**2,(2**3)**3)
# answer is 512 64 512
new_line()

i = 'Welcome'
def welcome(i):
    i = i + ',Welcome to turing' 
    return i  
welcome('Developer')
print(i)
# answer is Welcome
new_line()
# 'The {} side {1} {2}'.format('funny','side','of','life')
# answer is value err
# inputs = ['nodejs','reactjs','vuejs']
# print(inputs)
# for i in inputs:
#     inputs.append(i.upper())
# print(inputs)
# new_line()

array = ('Welcome', 'To', 'Turing')
print("-".join(array) )
new_line()
# answer is Welcome-To-Turing

a = [1,2,3,4]
b = [sum(a[0: x + 1]) for x in range(0, len(a) )]
print (b)
new_line()
# answer is [1,3,6,10]

# def add(c, k):
#     c.test = c.test + 1
#     k = k + 1
# class Plus:
#     def __init__self(self):
#         self.test = 0
# def main():
#     p = Plus()
#     index = 0
    
#     for i in range(0, 25):
#           add(p, index)
#     print("p.test=", p.test)
#     print("index=", index)
# main()
#answer is attribute error

list = [10,20,30,40,50]
list.pop() #answer is [10,20,30,40]
print(list)
list.pop(2)
print(list)#answer is [10,20,40]
new_line()

t = '%(a)s %(b)s %(c)s'
print(t % dict(a ='welcome', b= 'to',c = 'turing'))
new_line() #welcome to turing is answer

class Hello:
    
    def __init__(self, a='welcome to'):
       self.a = a
    
    def welcome(self, x):
        print(self.a + x)
h = Hello()
h.welcome('Turing') #Welcome to turing is answer

alph = 'abcd'
for i in range(len(alph)):
    alph[i].upper()
print(alph) #abcd is answer
new_line()
import re
result = re.findall('Welcome to Turing', 'Welcome', 1)
print(result) # [] is answer
new_line()
# x = ['ab', 'cd']
# print(list(map(x.len,x)))

list1 = [1,2,6,12]
list2 = [12,6,2,1]
print(list1 == list2)
print(set(list1) == set(list2)) # false true is the answer
new_line()

class Developer:
    def __init__(self):
        self.seniority = 'Junior'
        self.skills = ''
    
    def display(self):
        print('Welcome to turing with {seniority} developer with skill {skills}'.format(seniority = self.__seniority__, skills = self.skills))
        
class NodeJs(Developer):
    def __init__(self):
        super().__init__()
        self.__seniority__ = 'Senior'
        self.skills = 'NodeJs'
c = NodeJs()
c.display()
new_line() #welcome to turing with senior developer with skills NodeJs
        