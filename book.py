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
name = 'Njeri'
password = 'kashee@#work'
if name == 'Njeri':
    print('hello,Njeri')
    if password == 'kashee@#work':
        print('Access granted.')
    else:
        print('Not Authorized!')

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
    
# name = ""
# while name != 'your name':
#     print("Please type your name.")
#     name = input() 
# print('Thank you!')


print('What is your name?')
name = input()
if name != 'njeri':
    print('Not Authorized!', name)
else:
    print('Hi Njeri!')
      