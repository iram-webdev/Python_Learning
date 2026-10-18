# dic={
#     1903:"Azmat",
#     1904:"Nashrin",
#     1905:"Iram"
# }
# print(dic[1903])


info ={"name":"iram","age":20, "eligible":True}
# print(info)
# # print(info["name2"])
# print(info.get('name2')) # if i want to show my output with error free that time we can use this method get
# print(info.keys()) # if i want to print all keys present we can access 
# print(info.values())

# for key in info.keys(): # if i want to print like iteration that vtime we can use this way
#     print(f"The values corresponding to the key {key} is {info[key]}")


print(info.items())  

for key,value in info.items(): 
     print(f"The values corresponding to the key {key} is {value}")