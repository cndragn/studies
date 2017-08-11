import time
import webbrowser

breaks = 3
count = 0

print("This program started on" + time.ctime())
while (count < breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=XftabV9S2z0")
    count += 1
