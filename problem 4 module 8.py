# Byron Garcia
# 3/10/24
# Write a function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.


def leap_year(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input("Input a year"))
print (leap_year(year))
