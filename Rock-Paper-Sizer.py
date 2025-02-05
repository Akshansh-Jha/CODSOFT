import random

def get_computer_choice():
    return random.choice(["R", "P", "S"]) 
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "R" and computer == "S") or \
         (user == "S" and computer == "P") or \
         (user == "P" and computer == "R"):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    while True:
        print("\n*======== Rock-Paper-Scissors Game ========*")
        print("Enter: \n R :- for Rock, \n P :- for Paper,\n S :- for Scissors \n(or 'X' to exit)")
        user_choice = input("Your choice: ").upper()

        if user_choice == "X":
            print("\nFinal Scores:")
            print(f"Your Score: {user_score}, Computer Score: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in ["R", "P", "S"]:
            print("Invalid choice. Please enter R, P, or S.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
if __name__ == "__main__":
    main()
