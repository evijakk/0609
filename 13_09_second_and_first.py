#  2. Christmas tree 

# Ask user to enter the height of the tree 

# Then Print the tree: Ex. height == 3 

# The printout would be: 

#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

numbber = int(input("enter the height of the tree"))
bottom_row = numbber*2+1
stars=1
blank_space = numbber
while stars<bottom_row:
    print(" "*blank_space+"*"*stars)
    stars+=2
    blank_space-=1
    
# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile

for num in range (1,101):
    if num%35==0:
        print("FizzBuzz, ", end="")
    elif num%5==0:
        print("Fizz, ", end="")
    elif num%7==0:
        print("Buzz, ", end="")
    else:
        print(num,", ", end="")
print("")

# 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

# Hint: what numbers do we have to check?
itis = True
prime_check = int(input("enter positive number"))
if prime_check>0:
    for dalitajs in range(2,prime_check):
        remainder=prime_check%int(dalitajs)
        if int(remainder)==0:
            itis =False
    if itis == True:
        print("It is prime number!")
    else:
        print("it is not")
else:
    print("It is not positive number, try again")