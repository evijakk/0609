username = input("Choose your username ")
age = input(f"{username}, how old are you? ")
hundred_in = 100-int(age)
print(f"After {hundred_in} years you will be hundred years old 🤯")
import datetime
print("Today is", datetime.datetime.now())
current_year = int(datetime.datetime.now (). year)
year_when_hundred = current_year + hundred_in
print("Then it will be", year_when_hundred)