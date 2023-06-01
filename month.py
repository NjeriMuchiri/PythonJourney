# def main():
#     months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    
#     n = int(input("Enter a month number (1-12): "))
#     #compute the starting position of mnth n in mnths
#     pos = (n - 1) * 3
#     #grab the appropriate slice from months
#     monthAbbrev = months[pos:pos+3]
#     #print the result
#     # print("The month abbreviation is", monthAbbrev + ".")
# main()

#A program to print the month abbreviation, given its number

def main():
    #months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]
    n = int(input("Enter a month number (1 - 12): "))
    print("The month abbreviation is", months[n - 1] + ".")
main()