import webbrowser
import time

breaks = 3

a = 0
print("This program started on " + time.ctime())
while (count < breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=ZhaT7F7lMEY")
    count = count + 1
    print ("Iteration " + count + ": " + time.ctime())
