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


skills = ['Node', 'pyth', 'React', 'vue js']
skills.insert(3, 'Java') #answer
print(skills)

print([i.lower() for i in "TURING"])
# ['t','u','r','i','n','g'] #answer
a = [1,2,3,4]
b = [sum(a[0:x + 1]) for x in range(0, len(a))]
print(b)
# [1,3,6,10] #answer

z = set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)
#{'p','b','q','san','c','a'} #answer


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

# x = 'abcdef'
# i = 'a'
# while i in x[:-1]: 
#    print(i, end="")  #prints infinitely a

data = [1,2,3]
def incr(x):
    return x + 1
print(list(map(incr, data)))
# [2,3,4] #answer
 
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


print(2**(3**2), (2**3)**2,(2**3)**3)
# answer is 512 64 512