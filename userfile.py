#program to create a file of username in batch mode
from tkinter.filedialog import askopenfilename, asksaveasfilename
def main():
    print("This program creates a file of usernames from a")
    print("file of names")

#get the file names
    infileName = input("What files are the names in?")
    outfileName = input("What file should the usernames go in? ")

#open the file
    infile = askopenfilename()
    outfile = asksaveasfilename()

#process each line of the input file
    for line in infile:
        #get the first and last names from line
        first, last = line.split()
        #create the username
        uname = (first[0]+last[:7]).lower()
        #write it to the output file
        print(uname, file=outfile)
    #close bith files
    infile.close()
    outfile.close()
    print("Usernames have been written to", outfileName)
main()