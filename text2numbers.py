#A program to convert a textual message into
#a sequence of numbers, utilizing the underlying unicode encode
def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")
    
    #Ge the message to encode
    message = input("Please enter the message to encode: ")
    #loop through the message and print out the unicode values
    for ch in message:
        print(ord(ch), end=" ")
    print()
    
main()
