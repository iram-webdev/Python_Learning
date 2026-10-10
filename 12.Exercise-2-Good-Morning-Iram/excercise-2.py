#Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.
import time
hour=int(time.strftime("%H"))

if hour < 12:
    print('Good morning Iram !')
elif hour > 12:
    print('Good Afternoon Iram!')
else:
    print('Good Evening Iram !')