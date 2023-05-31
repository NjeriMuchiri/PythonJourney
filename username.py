#simple string processing program to geneate usernames
def main():
    print("This program generates computer usernames.\n")
#get user's first and last names
    first = input("Please enter your first name (all lowecase): ")
    last = input("Please enter your last name (all lowercase): ")
#concatenate first initial with 7 chars of the last name
    uname = first[0] + last[:7]
#output the username
    print("Your Username is:", uname)
main()
