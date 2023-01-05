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

# while True:
#     number = input("Please type something: ")
#     if number == 'out':
#         print("Outing of here!")
#         break
#     elif int(number):
#         print(f"You are on a {number} floor")
#     else:
#         print("Type out to break out of the loop")

# def doPyth(a,b,c):
#        num_ab = a ** 2 + b ** 2
#        num_c = c ** 2
#        if num_ab == num_c:
#            print(f"The combination of: {a}, {b}, {c} supports pyth law")
#        else:
#             print(f"The combination of: {a}, {b},  {c} does not support pyth law!")
# doPyth(3,4,5) 
# doPyth(5,6,7)      

def hide_cards(card_numbers):
    cards_list = []
    for card_number in card_numbers:
        last_four_digits = card_number[-4:]
        formattedCreditCard =  f'**** **** **** {last_four_digits}'
        cards_list.append(formattedCreditCard)
        
    return cards_list
    
my_card = hide_cards(['1234567890123456','3456654378967654','2345543267898765'])
print(my_card)