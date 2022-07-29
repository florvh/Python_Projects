from random import randint

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    roll1:int = randint(1,6)
    roll2:int = randint(1,6)
    print("Dices rolling...")
    print("The values are :")
    print(roll1)
    print(roll2)
    roll_again = input("Roll the Dices Again?\n")

