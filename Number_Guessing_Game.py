import random
import pickle

class NumberGuessingGame:
    def __init__(self):
        self.max_attempts = 0
        self.secret_number = 0
        self.attempts = 0
        self.score = 0

    def set_difficulty(self, difficulty):
        if difficulty == 'easy':
            self.max_attempts = 10
        elif difficulty == 'medium':
            self.max_attempts = 7
        elif difficulty == 'hard':
            self.max_attempts = 5

    def generate_number(self):
        self.secret_number = random.randint(1, 100)

    def save_game(self):
        with open("savegame.pkl", "wb") as file:
            pickle.dump(self, file)

    def load_game(self):
        try:
            with open("savegame.pkl", "rb") as file:
                saved_game = pickle.load(file)
                return saved_game
        except FileNotFoundError:
            print("No saved game found.")
            return None

    def play_game(self):
        print("Welcome to the Advanced Number Guessing Game!")
        print("Choose your difficulty: easy, medium, or hard.")
        difficulty = input("Difficulty: ").lower()

        # Load a saved game or start a new one
        saved_game = self.load_game()
        if saved_game:
            self.__dict__.update(saved_game.__dict__)
        else:
            self.set_difficulty(difficulty)
            self.generate_number()

        print(f"Guess the number between 1 and 100. You have {self.max_attempts} attempts.")

        while self.attempts < self.max_attempts:
            try:
                guess = int(input("Enter your guess: "))

                if guess == self.secret_number:
                    print(f"Congratulations! You guessed the correct number {self.secret_number} "
                          f"in {self.attempts + 1} attempts. Your score is {self.score}.")
                    break
                elif guess < self.secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")

                self.attempts += 1
                self.calculate_score()

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        else:
            print(f"Sorry, you've run out of attempts. The correct number was {self.secret_number}.")

    def calculate_score(self):
        # Score is calculated based on difficulty and number of attempts
        self.score = 1000 // (self.attempts + 1)

        # Optionally, you can add more criteria for scoring based on time or other factors.

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play_game()
    game.save_game()
