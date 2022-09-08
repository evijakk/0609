print("hi")
print("bye")
print("nice")
name=25
#mēģinu vēlreiz
print(name)
print("hi")
c=200
print(c)
c=c+1000
print(c)
c+=1000
print(c)
print(type(c))
c+=55
print(c)
print(type(c))
c-=100000.555555555555555555555555578
print(c)
print(type(c))
c=int(c)
print(c)
print(type(c))
a=10.5
print(a)
a=round(a,0)
print(a)
zz=round(0.2,1)
cc=round(0.1,1)
aa=zz+cc
print(aa)

# import datetime
# print("Today is", datetime.datetime.now())
# print("The year is", datetime.datetime.now().year)

# my_name = input("What is your name friend? ")
# print(f"Wow that is a nice name {my_name}")

# a = input("what number you want to double? ")
# a=int(a)
# double_str_a = a * 2 # a is a string so we need to convert it to an int
# print(f"Cool {a} doubled is {double_str_a}, or is it ?")

# a=0.3
# print(a)
# a=a-1
# a=0.7
# print(a)

# Write a program that asks for and saves a username !!!!!!!!!!!!
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically

username = input("Choose your username ")
age = input(f"{username}, how old are you? ")
hundred_in = 100-int(age)
print(f"After {hundred_in} years you will be hundred years old 🤯")
import datetime
print("Today is", datetime.datetime.now())
current_year = int(datetime.datetime.now (). year)
year_when_hundred = current_year + hundred_in
print("Then it will be", year_when_hundred)


