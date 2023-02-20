#program to print my name
# name = input("Please enter you name gal: ")
# if name == 'Kashee':
#     print("Hi Kashee")
# else:
#     print("hi", name)

#program to check whether the number is odd or even
# number = int(input("Please enter a number: "))
# if number % 2 == 1:
#     print(number," is odd ")
# elif number % 2 == 0:
#     print(number, "is even")
# else:
#     print("just a number")

# #Program to print maximum of two numbers
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# if num1 > num2:
#     print(num1, "is greater")
# elif num2 > num1:
#     print(num2, "is greater")
# else:
#     print("they are equal")

## Program to print the maximum of three numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if (num1 >= num2) and (num1 >= num3):
    print(num1,"is the greatest")
elif (num2 >= num1) and (num2 >= num3):
    print(num2,"is the greatest")
elif (num3 >= num2) and (num3 >= num1):
    print(num3,"is the greatest")
else:
    print(num1,num2,num3,"are equal")