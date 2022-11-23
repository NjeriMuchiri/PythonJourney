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
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print(year,"Common year")
	elif year % 100 != 0:
		print(year, "Leap year")
	elif year % 400 != 0:
		print(year, "Common year")
	else:
		print(year, "Leap year")