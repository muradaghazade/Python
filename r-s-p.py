import random

list = ["Rock", "Scissors", "Paper"]

games = 0
human = 0
comp = 0
tie = 0



while True:
    comp_choice = random.choice(list)
    a = input("Type your choice:\t")
    if a != "q":
        b = a.capitalize()
        games+=1

        if comp_choice == "Scissors" and b == "Rock":
            human+=1
            print(f' Your choice: {b}\n Computer choice: {comp_choice}\n Human wins!\n Games played: {games} Human: {human} Computer: {comp} Tie: {tie}')
        elif comp_choice == "Paper" and b == "Scissors":
            human+=1
            print(f' Your choice: {b}\n Computer choice: {comp_choice}\n Human wins!\n Games played: {games} Human: {human} Computer: {comp} Tie: {tie}')
        elif comp_choice == "Rock" and b == "Paper":
            human+=1
            print(f' Your choice: {b}\n Computer choice: {comp_choice}\n Human wins!\n Games played: {games} Human: {human} Computer: {comp} Tie: {tie}') 
        elif comp_choice == b:
            tie+=1
            print(f' Your choice: {b}\n Computer choice: {comp_choice}\n Tie!\n Games played: {games} Human: {human} Computer: {comp} Tie: {tie}')
        elif b != "Rock" and b != "Scissors" and b != "Paper":
            print("Do not cheat!\a")
        else:
            comp+=1
            print(f' Your choice: {b}\n Computer choice: {comp_choice}\n Computer wins!\n Games played: {games} Human: {human} Computer: {comp} Tie: {tie}')
            
    else:
        print("Your choice: Exit.\nBye!")
        break