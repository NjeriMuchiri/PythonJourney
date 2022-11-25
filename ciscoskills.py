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
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True # It's a little fake, we need it to enter the while loop.
while swapped:
   swapped = False # no swaps so far
   for i in range(len(my_list) - 1):
       if my_list[i] > my_list[i + 1]:
           swapped = True # a swap occurred!
           my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)