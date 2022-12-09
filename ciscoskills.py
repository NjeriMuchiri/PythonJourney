# print("Tell me anything")
# anything = input("Say something:")
# print("Hmm", anything, "...Woow!")
# x = int(input())
# y = int(input())
# print(x + y)

# bestPlant = str(input("Name one of the best and helpful inhouse plant: "))

# if bestPlant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!!")
# elif bestPlant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathyphyllum, not", bestPlant)

# Leap year and common year
# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
# 	if year % 4 != 0:
# 		print(year,"Common year")
# 	elif year % 100 != 0:
# 		print(year, "Leap year")
# 	elif year % 400 != 0:
# 		print(year, "Common year")
# 	else:
# 		print(year, "Leap year")
  
# import time

# for count in range(1,6):
#     print(count, "Mississippi")
#     time.sleep(1)

# print("Ready or not, here I come")

##Sorting right order
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True # It's a little fake, we need it to enter the while loop.
# while swapped:
#    swapped = False # no swaps so far
#    for i in range(len(my_list) - 1):
#        if my_list[i] > my_list[i + 1]:
#            swapped = True # a swap occurred!
#            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)


# BMI
# def bmi(weight,height):
#     weight = float(input("Enter your weight: "))
#     height = float(input("Enter your height: "))
#     if height < 0.5 or weight > 300:
#         return None
#     calculations = weight / height **2
#     return calculations
# print("your bmi is: ",bmi(144,1.7))

# factorial
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
# for n in range(1, 10):
#     print(n, factorial_function(n))
# # use case of dir
# import math

# for name in dir(math):
#     print(name, end=' \t ')

# from random import random,seed
# seed(1)
# for i in range(5):
#      print(random())

# from random import choice, sample
# my_list = [1,2,3,4,5,6,7,8,9,10]

# print(choice(my_list))
# print(sample(my_list, 5))
# print(sample(my_list, 10))

# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr)
# from random import randint

# for i in range(2):
#    print(randint(1, 2), end='')

# Caesar Cipher encryption
# text = input("Enter your message: ")
# cipher = ''
# for char in text:
#    if not char.isalpha():
#       continue
#    char = char.upper()
#    code = ord(char) + 1
#    if code > ord('Z'):
#       code = ord('A')
#    cipher += chr(code)
# print(cipher)

# # decryption
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#    if not char.isalpha():
#       continue
#    char = char.upper()
#    code = ord(char) - 1
#    if code < ord('A'):
#       code = ord('Z')
#    text += chr(code)
# print(text)

# Palindrome - a word when read both forward and backward looks the same
# user = input("Enter some text: ")

# text = user.replace(' ','')
# if len(text) > 1 and text.upper() == text[::-1].upper():
#      print("it's a palindrome")
# else:
#    print("it's not a palindrome")
   
# palindrome solution 2   
# string= input("Please enter a word: ")

# if(string == string[::-1]):
#    print("It's a palindrome!")
# else:
#    print("It's not a palindrome")   
         
# Anagram case - words rearranged once becomes one and the same thing
# word_1 = input("Enter the first word: ")
# word_2 = input("Enter the second word: ")

# word_1 = ''.join(sorted(list(word_1.upper().replace(' ', ''))))
# word_2 = ''.join(sorted(list(word_2.upper().replace(' ', ''))))
# if len(word_1) > 0 and word_1 == word_2:
#    print("Anagram present")
# else:
#    print("Anagram absent")

# Digit of Life
# date = input("Enter your birth date(farmat in YYYYMMDD): ")
# if len(date) != 8 or not date.isdigit():
#    print("Invalid date format.")
# else:
#    while len(date) > 1:
#       the_sum = 0
#       for dig in date:
#          the_sum += int(dig)
#       print(date)
#       date = str(the_sum)
#    print("Your Digit of Life is: " + date)
   








































































