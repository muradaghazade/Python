import random

list = ['Rock', 'Scissors', 'Paper']

comp_choice = random.choice(list)

while True:
    a = input("Type your choice:\t")
    b = a.capitalize()

    if comp_choice == "Scissors" and b == "Rock":
        print("Human wins")
    elif comp_choice == "Paper" and b == "Scissors":
        print("Human wins")
    elif comp_choice == "Rock" and b == "Paper":
        print("Human wins")  
    elif comp_choice == b:
        print("Tie")
    else:
        print("Computer wins")  
    break