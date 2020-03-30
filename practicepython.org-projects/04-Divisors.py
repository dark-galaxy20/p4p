# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
user_num = int(input("Please enter the number which you want its divisors : "))
all_nums = range(1,user_num//2)
for i in all_nums:
    if (user_num % i) == 0:
        print(i)
print(user_num)