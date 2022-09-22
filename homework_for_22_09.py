import math
my_list=[]
i=2
places = int(input("How many prime numbers do you need to output?"))

while len(my_list)<places:
    itis = True
    for dalitajs in range(2, round(math.sqrt(i)+1)):
        remainder=i%int(dalitajs)
        if int(remainder)==0:
            itis =False
    if itis == True:
        my_list.append(i)
        
    i+=1
    
print(my_list)



# itis = True
# prime_check = int(input("enter positive number "))
# if prime_check>0:
#     for dalitajs in range(2,prime_check):
#         remainder=prime_check%int(dalitajs)
#         if int(remainder)==0:
#             itis =False
#     if itis == True:
#         print("It is prime number!")
#     else:
#         print("it is not prime number")
# else:
#     print("It is not positive number, try again")