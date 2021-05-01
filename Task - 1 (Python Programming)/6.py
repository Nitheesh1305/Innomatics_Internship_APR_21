#Question 6 - Write a Function

#Task
#Given a year, determine whether it is a leap year. 
#If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(n):
    if n % 400 == 0 or n % 4 == 0 :
        return True
    if n % 100 == 0:
        return False

    return False
    
year = int(input('Enter a year : '))

print(is_leap(year))
