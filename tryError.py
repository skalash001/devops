a = int(input("How many books do you have : "))
try:
    if a >= 5:
        print('You have good collection habit..')

    else:
        print("You shoud think to upskill yourself...")
except ValueError:
    print("That's not a number...")

