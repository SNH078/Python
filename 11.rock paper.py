import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Convert user input to corresponding numeric value
you = youDict[youstr]

# Dictionary mapping numbers to choices (Rock, Paper, Scissors)
reverseDict = {-1: "Rock", 0: "Paper", 1: "Scissors"}

# Assuming 'you' and 'computer' are already defined
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw!")

else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You Lose!")
    else:
        print("Something went wrong!")
