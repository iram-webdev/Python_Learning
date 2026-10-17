
# # numbers=[50,10,40,30,20,88]
# # numbers.sort()
# # print("List in ascending order", numbers)

# # num= int(input("enter the numbers :"))
# # if num<=1:
# #     print("it is no prime")
# # else:
# #     for i in range(2,num):
# #         if num %2==0:
# #               print("it is not prime")
# #               break
# #         else:
# #              print("it is prime number")

# # n=int(input("Enter the number of terms"))
# # a=0
# # b=1
# # for i in range(n):
# #     print(a,end="")
# #     c=a+b
# #     a=b
# #     b=c
# # n=int(input("Enter the number of terms"))
# # a=0
# # b=1

# # for i in range(n):
# #     print(a, end="")
# #     c=a+b
# #     a=b
# #     b=c
# # num=int(input("Enter the number :"))
# # if num > 0:
# #     print("it is positive number")
# # elif num < 0:
# #     print("it is negative number")
# # else:
# #     print("Zero")

# num = int(input("Enter the number : "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




# # write a program to check the no. is prime or not 
# num=int(input("enter the number:"))
# if num<=1:
#     print("it is not prime")
# else:
#     for i in range(2,num):
#         if num %2==0:
#             print("it is not prime")
#             break
#         else:
#             print("it is prime")

# # write a program to check the no. is positive ,negative or zero
# num =int(input("enter the no.:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# # write a program to check the no. is even or odd

# num=int(input("enter the no.:"))
# if num%2==0:
#     print("even")
# else:
#     print('odd')

# n=int(input("enter the no. of term :"))
# a=0
# b=1
# for i in  range(n):
#     print(a,end="")
#     c=a+b
#     a=b
#     b=c

# greatings="welcome"
# print(greatings[0:7])
# print(greatings[:])
# print(greatings[:7])
# print(greatings[0:])
# print(greatings[:5])
# print(greatings[1:3])
# print(greatings[2:7])


# s = "PYTHONPROGRAMMING"
# print(s[2:15:3])

# s = "PYTHONPROGRAMMING"
# print(s[10:2:-2])


# s = "COMPUTERSCIENCE"
# print(s[-2:-12:-3])

# s = "abcdefghijklmnopqrstuvwxyz"
# print(s[-15:-5:-4])

# s = "PYTHON"
# print(s[1:-1][::-1])
# s = "0123456789"
# print(s[-1:1:2])

# s = "PROGRAMMING"
# print(s[1:9:2][::-2])


# nm="iram"
# print(nm.upper())

# import time
# hour=int(time.strftime("%H"))

# if hour<12:
#     print("Good morning")
# elif hour<17:
#     print('Good Afternoon!')
# else:
#     print('Good evening')


import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)   
timestamp=time.strftime("%H")
print(timestamp) 
timestamp=time.strftime('%M')
print(timestamp)
timestramp=time.strftime("%S")
print(timestramp)
