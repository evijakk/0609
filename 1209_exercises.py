#exercise 1 
temperature = int(input("What is your temperature?"))
if temperature <35:
    print("it's too cold")
elif temperature > 37:
    print("possible fever")
else:
    print("all right")
#exercise 2
years = 2
bonus_perc = 0.15
salary = int(input("What is your monthly salary?"))
work_years = int(input("How long you work here?"))
if work_years > 2:
    print("Your bonus will be",round(((work_years-years)*bonus_perc*salary),2) , "euro")
else:
    print("Sorry, not this year")
