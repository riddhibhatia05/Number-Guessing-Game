import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.max_attempts = 0
        self.secret_number = 0
        self.attempts = 0

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Choose Difficulty:").pack()

        difficulty_options = ["easy", "medium", "hard"]
        for difficulty in difficulty_options:
            tk.Radiobutton(
                self.master,
                text=difficulty,
                variable=self.difficulty_var,
                value=difficulty
            ).pack()

        tk.Button(self.master, text="Start Game", command=self.start_game).pack()

    def start_game(self):
        self.max_attempts = 10 if self.difficulty_var.get() == "easy" else 7 if self.difficulty_var.get() == "medium" else 5
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.game_window()

    def game_window(self):
        game_window = tk.Toplevel(self.master)
        tk.Label(game_window, text=f"Guess the number between 1 and 100. You have {self.max_attempts} attempts.").pack()

        tk.Entry(game_window, textvariable=tk.StringVar()).pack()
        tk.Button(game_window, text="Submit Guess", command=lambda: self.check_guess(game_window)).pack()

    def check_guess(self, game_window):
        # Implement the logic to check the guess, update attempts, and provide feedback
        # Display appropriate messages using messagebox.showinfo or messagebox.showerror

        # Example:
        guess = 42  # Replace with the actual guessed value
        if guess == self.secret_number:
            messagebox.showinfo("Congratulations!", f"You guessed the correct number in {self.attempts + 1} attempts.")
            game_window.destroy()
        elif guess < self.secret_number:
            messagebox.showinfo("Too Low", "Try again.")
        else:
            messagebox.showinfo("Too High", "Try again.")

        self.attempts += 1

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The correct number was {self.secret_number}.")
            game_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGameGUI(root)
    root.mainloop()

