# 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

# Hint: what numbers do we have to check?
itis = True
prime_check = int(input("enter positive number "))
if prime_check>0:
    for dalitajs in range(2,prime_check):
        remainder=prime_check%int(dalitajs)
        if int(remainder)==0:
            itis =False
    if itis == True:
        print("It is prime number!")
    else:
        print("it is not prime number")
else:
    print("It is not positive number, try again")