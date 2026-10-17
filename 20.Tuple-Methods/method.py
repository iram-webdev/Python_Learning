# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries) # we convert here tuple into list
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp) # here again convert into list to tuple
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)



# tuple=(1,2,2,3,2,4,5,6,0,0)
# # tuple1=tuple.count(2)
# tuple1=tuple.index()
# print("count of 2 in tuple is :",tuple1)
import time
hour=int(time.strftime("%H"))

if hour<12:
    print('Good morning!')
elif hour>12:
    print('Good Afternoon')
else:
    print('Good Evening')