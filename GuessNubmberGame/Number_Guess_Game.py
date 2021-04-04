import random

range = (1,199)
n = random.randint(range[0], range[1])
print("This is number guessing game.  User has 6 chances to guess the number. \nAfter each wrong guess, user looses the 20 points")
count = 5
bool_guess = bool(0)
points = 100
pt_val = {5:100, 4:80, 3:60, 2:40, 1:20, 0:0}

try:
    guess = int(input("Enter an integer from 1 to 199: "))
    if guess < range[0] or guess > range[1]:
	    raise ValueError("Invalid number is entered.  Please enter input in the range 1 to 199")

    while count > 0:
        if guess < n:
            print ("guess is low")
            guess = int(input("Enter an integer from 1 to 199: "))
        if guess < range[0] or guess > range[1]:
	        raise ValueError("Invalid number is entered.  Please enter input in the range 1 to 199")
        elif guess > n:
            print ("guess is high")
            guess = int(input("Enter an integer from 1 to 199: "))
        if guess < range[0] or guess > range[1]:
	        raise ValueError("Invalid number is entered.  Please enter input in the range 1 to 199")
        else:
            print ("you guessed it!")
            bool_guess = bool(10)
            break
        count-=1

    if bool_guess:
        print("You earned ", pt_val[count],  " points")
    else:
        print("The number was : ", n)
        print("You earned ", pt_val[count], " points and lost the game")
except ValueError as ve:
    print(ve)
except:
    print("Invalid input")