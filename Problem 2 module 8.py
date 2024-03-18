# Byron Garcia
# 3/10/24
# Program checks to see if values add to less, more, or equal to 10

x = float(input("What is your first number?"))
y = float(input("What is your second number?"))

if x + y < 10:
    print("Your numbers add up to less than 10")
else:
    if x + y > 10:
        print("Your numbers add up to more than 10 ")
    else:
        print("Your numbers add up to 10 exactly")