#creating a bubble sort function
def bubble_sort(list1):
    #outer loop for traverse the entire list
    for i in range(0,len(list1) - 1):
        for j in range(len(list1) - 1):
            if(list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

list1 = [4,3,9,6,7,1]
print("The unsorted list is: ",list1)
#Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list1))

def new_line():
    print('\n') 
new_line()

#median
import numpy as np
a = np.array([1,2,3,4,5,6,7])
p = np.percentile(a, 50) #returns the soth percentile which is also the median
print(p)

new_line()

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i == 0):
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
else:
        print(num, "is not a prime number")      
                    
new_line()
x = ["Turing","Deep","Talent","Cloud"]
print(" ".join(x))

new_line()

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return(Fibonacci(n -1) + Fibonacci(n-2))
nterms = int(input("Enter the terms? "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(Fibonacci(i))

# def add_nums(num1, num2):
#     while num2 != 0:
#         data = num1 & num2
#         num1 = num1 ^ num2
#         num2 = data << 1
#     return num1
# print(add_nums(23, 26))

from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
print(is_anagram('developer', 'redevelop'))
print(is_anagram("Turing", "Turning"))
new_line()
#3D Array:
# import NumPy as np
# three_dimensional_list = [[[1,2,3], [4,5,6], [7,8,9]]]
# three_dimensional_array = np.array(three_dimensional_list)
# print("3D array is: ",three_dimensional_array)

#shallow copy and deep copy
from copy import copy, deepcopy
list_1 = [1,2, [3,5], 4]
#shallow copy
list_2 = copy(list_1)
list_2[3] = 7
list_2[2].append(6)
list_2
list_1
#deepcopy
list_3 = deepcopy(list_1)
list_3[3]=8
list_3[2].append(7)
list_3
list_1
