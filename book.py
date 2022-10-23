#from automateboringstuffwithpython.com book
#this program says hello and asks for my name
#Chapter1
# print('Hello, Kashee!')
# print('What\'s your name?')
# myName = input()
# print('It is good to meet you,' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?')
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.' )

#Chapter2
# name = 'Njeri'
# password = 'kashee@#work'
# if name == 'Njeri':
#     print('hello,Njeri')
#     if password == 'kashee@#work':
#         print('Access granted.')
#     else:
#         print('Not Authorized!')

# name = 'Carol'
# age = 3000
# if name == 'Alice':
#     print('Hi, Alice')
# elif age < 12:
#     print('You are not Alice, granie')
# elif age > 2000:
#     print('Unlike you, Alice is not indead, immortal vampire')
    
# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1
    
# spam = 0
# if spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

    # prints your name endlessly
# name = ""
# while name != 'your name':
#     print("Please type your name.")
#     name = input() 
# print('Thank you!')

# checks the name validity
# name = input('what is your name?')
# if name != 'njeri':
#     print('Not Authorized!', name)
# else:
#     print('Hi Njeri!')
    
# using break statement on the loop
# while True:
#     name = input('Please type your name.')
#     if name == 'njesh':
#        break
# print('Thank you!')

# # continue and break statements in a while loop
# while True:
#     name = input('Who are you?')
#     if name != 'Muchiri':
#         continue
#     print('Hello, Muchiri. \n  What is the password? (web designer in making)')
#     password = input()
#     if password == 'kasheedesignerweb':
#         break
#     print('Access Granted')

# True and falsey values
# name = ''
# while not name:
#       name = input('Enter your name:') 
# numOfGuests = int(input('How many guests will you have?'))
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done')

# for loop and the range function
# myNameIs = input('what is your name programmer?')
# print('My name is', myNameIs)
# for i in range(5):
#     print(myNameIs + ' Five Times(' + str(i) + ')')

# print('My name is')
# for i in range(5):
#     print('Kashee Five Times (' + str(i) + ')')
# total = 0
# for num in range(101):
#     total = total + num
# print(total)

for i in range(8, 10):
    print(i)
