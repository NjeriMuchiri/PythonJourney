# #!/usr/bin/python3
# import os

# with open("ANN_MUCHIRI_CV.pdf", mode = "w", encoding="utf-8") as myFile:
#     myFile.write("Njeri is an awesome programmer\nYou will love her products\nOh yes!!!")

# with open("ANN_MUCHIRI_CV.pdf", encoding="utf-8") as myFile:
#     print(myFile.read())
# os.rename("ANN_MUCHIRI_CV.pdf", "Kashee_resume.pdf")

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)
main()
