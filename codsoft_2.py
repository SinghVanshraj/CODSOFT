import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor"]

    def get_user_choice(self):
        while True:
            choice = input("Choose rock/paper/scissor: ").strip().lower()
            if choice in self.choices:
                return choice
            print("Invalid input. Please choose rock, paper, or scissor.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user, computer):
        print("\n------------------------")
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")
        
        if user == computer:
            print("It's a draw!")
        elif (user == "rock" and computer == "scissor") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissor" and computer == "paper"):
            print("You won!")
        else:
            print("You lost!")

    def play_round(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        self.determine_winner(user_choice, computer_choice)

    def play(self):
        while True:
            self.play_round()
            again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("\nThanks for playing!")
                print("------------------------")
                break

# Start the game
game = Game()
game.play()
