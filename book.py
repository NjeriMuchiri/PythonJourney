#from automateboringstuffwithpython.com book
#this program says hello and asks for my name
#CHAPTER1
# print('Hello, Kashee!')
# print('What\'s your name?')
# myName = input()
# print('It is good to meet you,' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?')
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.' )

#CHAPTER2
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

# for i in range(0, 30, 3):
#     print(i)

# importing modules
# import random 
# for i in range(5):
#     print(random.randint(1,10))
    
# import sys
# while True:
#     response = input('Type exit to exit: ')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# import random 
# secretNumber = random.randint(1, 20)
# print( 'I am thinking of a number between 1 and 20')

# for guessesTaken in range(1, 7):
#     guess = int(input('Take a guess. '))
    
#     if guess < secretNumber:
#         print('Your guess is too low!')
#     elif guess > secretNumber:
#         print('Your guess is too high!!')
#     else:
#         break
    
#     if guess == secretNumber:
#         print('Good job! You guessed my number in' + str(guessesTaken) + 'guesses!')
#     else:
#         print('Nope.The number I was thinking of was ' + str(secretNumber) )
        
# Rock,Paper,Scissor
# import random, sys
# print('ROCK, PAPER, SCISSORS')

# wins = 0
# losses = 0
# ties = 0

# while True: #The main game loop
#     print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties)) 
#     while True: # the player loop
#        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit ')  
#        playerMove = input()
#        if playerMove == 'q':
#            sys.exit()
#        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#            break
#        print('Type one of r, p, s, or q.')
#     #    Display what the player choose
#        if playerMove == 'r':
#            print('ROCK versus...')
#        elif playerMove == 'p':
#            print('PAPER versus...')
#        elif playerMove == 's':
#            print('SCISSORS versus...')
#     # Display what computer choose
#        randomNumber = random.randint(1, 3)
#        if randomNumber == 1:
#            computerMove = 'r'
#            print('ROCK')
#        elif randomNumber == 2:
#            computerMove = 'p'
#            print('PAPER')
#        elif randomNumber == 3:
#            computerMove = 's'
#            print('SCISSORS')
#      #Display and record the win/loss/tie:
#        if playerMove == computerMove:
#          print('It is a tie!')
#          ties = ties + 1
#        elif playerMove == 'r' and computerMove == 's':
#            print('You Win!')
#            wins = wins + 1
#        elif playerMove == 'p' and computerMove == 'r':
#            print('You Win!')
#            wins = wins + 1
#        elif playerMove == 's' and computerMove == 'p':
#            print('You Win!')
#            wins = wins + 1  
#        elif playerMove == 'r' and computerMove == 'p':
#            print('You Lose!')
#            losses = losses + 1   
#        elif playerMove == 'p' and computerMove == 's':
#            print('You Lose!')
#            losses = losses + 1  
#        elif playerMove == 's' and computerMove == 'r':
#            print('You Loose!')
#            losses = losses + 1       
            
# CHAPTER 3
#functions
# def hello():
#       print('Howdy!')
#       print('Howdy!!!')
#       print('Hello there')
      
# hello()
# hello()
# hello()

# functions and parameters 
# def hello(name):
#       print('hello, ' + name)  

# hello('Alice')
# hello('Bob')                  

# return values and statements
# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidely so'
#     elif answerNumber == 3:
#         return 'yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
# print(getAnswer(random.randint(1, 9)))
    
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
# import random
# print(random.randrange(1,10,2))

#Keyword arguments #end
# print('Hello', end=' ')
# print('World')
# #sep
# print('cats', 'dogs', 'mice', sep=',')

#call stack
# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a() returns')
# def b():
#     print('b() starts')
#     c()
#     print('b() returns')
# def c():
#     print('c() starts')
#     print('c() returns')
# def d():
#     print('d() starts')
#     print('d() returns')
    
# a()  
# local and global scope
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
    
# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# global scope
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)
  
# Exception handling, error handling: try and except statements
# def spam(divideBy):
#     return 42 / divideBy
# try:
#         print(spam(2))
#         print(spam(12))
#         print(spam(0))
#         print(spam(1))
# except ZeroDivisionError:
#         print('Error: Invalid argument.')

# collatz sequence
# def collatz(number):
#     if number % 2 == 0:
#      print(number // 2)
#      return number // 2
#     elif number % 2 == 1:
#      print( 3 * number + 1)
#      return 3* number + 1
# n = int(input('Enter a number: '))
# while n != 1:
#     n = collatz(n)
    
# CHAPTER 4
# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +
# ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '' :
#         break 
#     catNames = catNames + [name]
# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)
        
# for i in [0,1,2,3]:
#     print(i)

# supplies = ['pens', 'staples', 'flame-throwers', 'binders']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
##the not in keywords 
# myPets = ['Zophie', 'Pooka', 'FatTail']
# name = input('Enter a pet name: ')
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')
    
# # Multiple Assignment Trick || The number of variables and length of line must be exactly equal else valueerr
# cat = ['fat', 'black', 'loud']
# size,color,disposition = cat

##Augmented Assignment Operator +=
# spam = 22
# spam += 1
# print(spam) #23
##other augmented assignment operators +=, -=, *=1, /=, %=
# spam  = 'Hello'
# spam += ' Kashee the webdesigner!'
# print(spam)

# bacon = ['Zophie']
# bacon *= 3
# print(bacon)

# #METHODS
# A method is the same thing as a function except it is called on a value 
# Ann = ['Kashee', 'Njesh', 'Njerinna', 'Anika', 'Jeje']
# print(Ann.index('Jeje'))
##Note if there are duplicates in the list the index of its first appearance is returned

# Adding values with append and insert methods
# Ann = ['Kashee', 'Njesh', 'Njerinna', 'Anika', 'Jeje']
# Ann.append('NjeriMuchiri') #Adds to the end of list
# print(Ann)   

#insert method can add  a value at nay index in the list
# Ann = ['Kashee', 'Njesh', 'Njerinna', 'Anika', 'Jeje']
# Ann.insert(1, 'NjeriMuchiri')
# print(Ann)

##Removing values form list with remove()
# Ann = ['Kashee', 'Njesh', 'Njerinna', 'Anika', 'Jeje']
# Ann.remove('Kashee')
# print(Ann)
   #The del statement is good to use when you know the index of the value you want to remove from the list and remove method is good when you know the value you want to remove from the list
#Sort Method
# Ann = ['Kashee', 'Njesh', 'Njerinna', 'Anika', 'Jeje']
# Ann.sort()
# print(Ann)
# Ann.sort(reverse = True)
# print(Ann)

# Letters = ['a', 'z', 'A', 'Z']
# Letters.sort()
# print(Letters)
# Letters.sort(key = str.lower)
# print(Letters)

# name = 'Kashee'
# for l in name:
#     print('**** ' + l + ' ****' )

##Mutable and immutable data types
# A list value is a mutable data type * It can have values added, removes or changed
# A string is immutable - It cannot be changed
#The proper way to mutate a string is to use slicing and concatenation to build a new string by copying parts of the old string
# name  = 'She goes by Kashee'
# newName = name[0:12] + 'Njesh'
# print(name)
# print(newName)
# Tuple is an immutable data type

##Passing References
# def eggs(someParameter):
#     someParameter.append('Hello')
# spam = [1,2,3]
# eggs(spam)
# print(spam)

#The copy() and deepcopy() methods
# Copy() - can be used to make a duplicate copy of a mutable value like a list or dictionary 