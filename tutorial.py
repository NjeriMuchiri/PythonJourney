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

# def hide_cards(card_numbers):
#     cards_list = []
#     for card_number in card_numbers:
#         last_four_digits = card_number[-4:]
#         formattedCreditCard =  f'**** **** **** {last_four_digits}'
#         cards_list.append(formattedCreditCard)
        
#     return cards_list
    
# my_card = hide_cards(['1234567890123456','3456654378967654','2345543267898765'])
# print(my_card)


#Class #constructor
# class CreditCard:
#     def __init__(self, number,company,limit):
#         self.number= number
#         self.company = company
#         self.limit = limit
    
#     def hide(self):
#         self.number = f'**** **** **** {self.number[-4:]}'
# c1 = CreditCard(number = "7654546734562345", company = "Njerina",limit = "5000")

# c1.hide()
# print(c1.number)

#Tutorial final project
import random
#Game Variables
deck = 10
p_won_score = (deck / 2 + 1)
class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.cards = list(range(1, deck + 1, 1))
        
        random.shuffle(self.cards) 
        
    def pickCard(self):
        picked_card = self.cards[0]
        self.cards.remove(picked_card)
        print(f"{self.name} card is {picked_card}")
        return picked_card
      
    def add_point(self):
        self.points += 1
        print(f"A point has been added to {self.name}")
        
    def game_is_over(self):
        return len(self.cards) == 0 or self.points == p_won_score
    
p1 = Player(name = "Kashee")
p2 = Player(name = "Kaggy")
print("Game Starts...")
while True:
    input("Press Enter to pick a card!")
    p1_card = p1.pickCard()
    p2_card = p2.pickCard()      
    if p1_card > p2_card:
        p1.add_point()
    elif p2_card > p1_card:
        p2.add_point()
    else:
        print("TIE!!!")
        
    if p1.game_is_over() or p2.game_is_over():
        print("The game is over!")
    if p1.points > p2.points:
        print(f"{p1.name} wins!")
    elif p2.points > p1.points:
        print(f"{p2.name} wins!")
    else:
        print("Score is TIE!")
        
        print(f"Final Score: {p1.points} - {p2.points}")
        break
    print(f"Score: {p1.points} - {p2.points}")