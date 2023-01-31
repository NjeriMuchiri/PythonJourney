#geneating own dataset
from faker import Faker
fake = Faker()
for _ in range(10):
    print(fake.name())
    
def new_line():
    print('\n')
new_line()

    
#how to check the largest string between two
str1 = 'Kasheeinthebuilding'
str2 = 'kasheeinthebuidingcoding'

if str1 > str2:
    print(str1, 'is the largest string')
else:
    print(str2, 'is the largest string')

# print(max(str1,str2))

new_line()

#print month of a year

import calendar
print(calendar.month(2023,2))

#how to make colorful texts
print("\033[92mKashee is a firm believer")
print("\033[96mKashee loves ken")
print("\033[93mKashee is yet to be a great software engineer")
print("\033[95mKashee wants to be overly consistent when it comes to working out!")
print("\033[1mKashee loves helping her mum and others out when necessary")
print("\033[4mKashee wants to be consistent in her coding learning graph")
print("\033[94mKashee feels like her life is about to change for the better")

new_line()
#password cracker
# import subprocess

# data = (
#     subprocess.check_output(["netsh","wlan","show","profiles"]).decode("utf-8").split("\n")
# )
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = (
#         subprocess
#         .check_output(["netsh","wlan","show","profile",i,"key=clear"]).decode("utf-8").split("\n")
#     ) 
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print("{:<30}| {:<}".format(i, results[0]))
#     except IndexError:
#         print("{:<30}| {:<}".format(i, ""))

#Digital Clock
# import every_tkinter as tk
# from time import strftime

# def light_theme():
#     frame = tk.Frame(root, bg="white")
#     frame.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)
#     lbl_1 = tk.Label(frame, font=('calibri', 40, 'bold'), background='white', foreground='black')
#     lbl_1.pack(anchor="s")
    
#     def time():
#         string = strftime('%I:%M:%S %p')
#         lbl_1.config(text=string)
#         lbl_1.after(1000, time)
#     time()
    
# def dark_theme():
#     frame = tk.Frame(root, bg="#22478a")
#     frame.place(relx=0.1, rely=0.1,relwidth=0.8,relheight=0.8)
#     lbl_2 = tk.Label(frame, font=('calibri',40, 'bold'), background='#22478a', foreground='black')
#     lbl_2.pack(anchor='s')
    
#     def time():
#         string = strftime('%I:%M:%S %p')
#         lbl_2.config(text=string)
#         lbl_2.after(1000, time)
#     time()

# root = tk.Tk()
# root.title('Digital-Clock')
# canvas = tk.Canvas(root, height=140,width=400)
# canvas.pack

# frame = tk.Frame(root, bg='22478a')
# frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
# lbl = tk.Label(frame,font=('calibri',40,'bold'), background='#22478a', foreground='black')
# lbl.pack(anchor="s")
    
# def time():
#         string = strftime('%I:%M:%S %p')
#         lbl.config(text=string)
#         lbl.after(1000, time)
# time()

# menubar = tk.Menu(root)
# theme_menu = tk.Menu(menubar,tearoff=0)
# theme_menu.add_command(label="Light",command=light_theme)
# theme_menu.add_command(label="Dark",command=dark_theme)
# menubar.add_cascade(label="Theme", menu=theme_menu)
# root.config(menu=menubar)
# root.mainloop()







