def listSkills(val, list=[]):
    list.append(val)
    return list
list1 = listSkills('nodeJs')
list2 = listSkills('Java', [])
list3 = listSkills('React')
print("%s" % list1)
print("%s" % list2)
print("%s" % list3)


skills = ['Node', 'pyth', 'React', 'vue js']
skills.insert(3, 'Java')
print(skills)

print([i.lower() for i in "TURING"])

a = [1,2,3,4]
b = [sum(a[0:x + 1]) for x in range(0, len(a))]
print(b)

z = set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)

from re import A


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
        print(l)
f(2)
f(3, [3,2,1])
f(3)

x = 'abcdef'
i = 'a'
while i in x[:-1]:
   print(i, end="")

data = [1,2,3]
def incr(x):
    return x + 1
print(list(map(incr, data)))


def func1():
    x = 50
    return x
func1()
print(x)



f = None
for i in range(5):
    with open("app.log", "w") as f:
        if i > 2:
            break
print(f.closed)


print(2**(3**2), (2**3)**2,(2**3)**3)
