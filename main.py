#Sample implementation of the time2lib protocols
import time2lib

time = input("Enter the duration of each session: ")

time = time.split(":")
try:
    hr = int(time[0])
    mn = int(time[1])
except ValueError:
    print("Invalid values have been entered, quitting..")
    quit()

#This is the basic way to use the time2lib package
while True:
    x = time2lib.wait(hr,mn)

    if x == "timeup":
        print('break')

        #more functionality can be added here
