for i in range(12):
    if(i==5):
         print("skip the iteration")
         continue
    print("5 *",i+1,"=",5*(i+1))


for i in range(12):
    if(i==5):
           print("5 *",i+1,"=",5*(i+1))
           break
    print("skip the iteration")



# Emulate do while loop
while True:
     print(i)
     i=i+1
     if(i%100 == 0):
          break
     


   