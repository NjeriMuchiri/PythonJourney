#A program that converts a sequence of unicode 
#numbers into a string of text
def main():
    print("This program converts a sequence of unicode numbers into")
    print("the string of text that it represents.\n")
    
    #get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")
    #Loop throught each substring and build unicode message
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr) #converts digits to number
        message = message + chr(codeNum) #concatenates character to message
    print("\nThe decoded message is: ", message)
main()
