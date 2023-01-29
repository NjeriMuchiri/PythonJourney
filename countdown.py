import time

def countdown(time_sec):
    while time_sec:
        mins, sec = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, sec)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        
        print('stop ')
        
num = int(input("Set Your Time in Sec: "))
countdown(num)