import random
import time

choices = ["r", "p", "s"]

print("Welcome  To My Rock Paper Scissors Game\n\nR - Rock\nP - Paper\nS - Scissors\n")


def play_game():
    choose = input("Select your choice: ").lower()
    while choose not in choices:
        choose = input("Select a valid input \n\nR - Rock\nP - Paper\nS - Scissors\n\nSelect your choice: ").lower()
    cpu = random.choice(choices).lower()
    print(f"CPU: {cpu}")
    print(f"Player: {choose}")
        
    if cpu == choose:
        print("DECISION: Tie!")
        while True:
            time.sleep(2)
            print("Play Again")
            time.sleep(0.5)
            play_game()
            break


    elif choose == 'r':
        if cpu == 's':
            print("DECISION: You Win!")
        if cpu == 'p':
            print("DECISION: CPU Win!")

    elif choose == 'p':
        if cpu == 'r':
            print("DECISION: You Win!")
        if cpu == 's':
            print("DECISION: CPU Wins!")

    elif choose == 's':
        if cpu == 'r':
            print("DECISION: CPU Wins!")
        if cpu == 'p':
            print("DECISION: You win!")

    else:
        print("Thanks for playing.....bye!")


play_game()