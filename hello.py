
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

n=int(input("enter the no. of term :"))
a=0
b=1
for i in  range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c