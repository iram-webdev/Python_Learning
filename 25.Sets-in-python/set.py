s={2,4,2,6} # set not allows duplicate values
print(s)

info={"carla",19,False,5.9,19} # order is dependents on python
print(info)


# important for interview
iram=set()
print(type(iram))

# If i try this
iram={}
print(type(iram)) # the output will be dict


for value in info:
    print(value)