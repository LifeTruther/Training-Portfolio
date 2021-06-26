#Question 4 of the pre-work: I went with nested if statements
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            print("That is a leap year!")
    elif a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 ==0:
                print("That is a leap year!")            
    else: 
        print("I'm sorry, that is not a leap year")
is_leap_year(1996)
#terminal was a bit buggy with this one: it returned the strings for the right years, but it would magically stop printing the message for the leap year after a few iterations.
