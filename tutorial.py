# import random

# people = ["Allen", "Michael", "John", "Ben"]
# chosen_person = random.choice(people)
# people.remove(chosen_person)
# print(f'The chosen person is: {chosen_person}')
# print(f'The length of people list is {len(people)}')

# friends = ["Ann","Ken","Ben", "John", "Michael","Jim"]
# bestFriend = "Ken"
# # if bestFriend in friends:
# #     print(f"{bestFriend} my best of friends is here!")
# for friend in friends:
#     if friend == bestFriend:
#       print(f"{bestFriend}'s here")
#       break
#     else:
#         print(f"This is {friend}")
#     print("Defaulting")

while True:
    number = input("Please type something: ")
    if number == 'out':
        break
    elif int(number):
        print(f"You are on a {number} floor")
    else:
        print("Type out to break out of the loop")