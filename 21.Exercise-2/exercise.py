# import time
# hour=int(time.strftime("%H"))
# if hour<12:
#     print("Good Morning !")
# elif hour<17:
#     print("Good Afternoon !")
# else:
#     print('Good Evening !')

import time
# t=time.strftime('%H:%M:%S')
# print(t)
hour=int(time.strftime('%H'))
hour=int(input("Enter hour:"))
# print(timestramp)
# timestramp=time.strftime('%M')
# print(timestramp)
# timestramp=time.strftime('%S')
# print(timestramp)

import time

if(hour>=0 and hour<12):
    print("Good Morning Iram !")
elif(hour>=0 and hour<17):
    print('Good Afternoon Iram !')
elif(hour>=17 and hour<0):
    print("Good Night Iram !")