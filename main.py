"""
📄 Project 13: Snake Water Gun Game 
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: May 14, 2025

🧠 Description:
A simple GUI-based Snake Water Gun game built with Python and Tkinter.  
Play against the computer and keep track of wins, losses, and draws.

📦 Features:
- Interactive buttons for Snake, Water, and Gun
- Randomized computer choice
- Real-time result display
- Scoreboard tracking wins, losses, and draws

🧰 Tools & Modules Used:
- tkinter: for GUI elements
- random: for computer choice randomization

💡 How to Use:
1. Run the script: `python main.py`  
2. Click one of the buttons: Snake, Water, or Gun  
3. See the computer's choice and the game result  
4. Score updates automatically after each round  

✅ Example:
You chose Snake  
Computer chose Water  
You win!  
Score - Wins: 1 | Losses: 0 | Draws: 0
"""

import random
import tkinter as tk

# Dictionary for choices and their reverse
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Water Gun Game")
        self.user_choice = None
        self.computer_choice = None
        self.score = {"wins": 0, "losses": 0, "draws": 0}

        self.create_widgets()

    def create_widgets(self):
        # Game title
        title = tk.Label(self.window, text="Snake, Water, Gun Game", font=("Helvetica", 18))
        title.pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(self.window, text=self.get_score(), font=("Helvetica", 14))
        self.score_label.pack(pady=5)

        # Buttons for choices
        self.snake_btn = tk.Button(self.window, text="Snake", width=20, command=lambda: self.play_game("s"))
        self.snake_btn.pack(pady=5)
        
        self.water_btn = tk.Button(self.window, text="Water", width=20, command=lambda: self.play_game("w"))
        self.water_btn.pack(pady=5)

        self.gun_btn = tk.Button(self.window, text="Gun", width=20, command=lambda: self.play_game("g"))
        self.gun_btn.pack(pady=5)

        # Output display
        self.result_label = tk.Label(self.window, text="Choose an option to start!", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def play_game(self, user_choice):
        self.user_choice = youDict[user_choice]
        self.computer_choice = random.choice([-1, 0, 1])
        self.display_choices()
        self.calculate_result()
        self.update_score()

    def display_choices(self):
        self.result_label.config(text=f"You chose {reverseDict[self.user_choice]}\nComputer chose {reverseDict[self.computer_choice]}")

    def calculate_result(self):
        if self.computer_choice == self.user_choice:
            self.result_label.config(text=self.result_label.cget("text") + "\nIt's a draw!")
            self.score["draws"] += 1
        elif (self.computer_choice == -1 and self.user_choice == 1) or \
             (self.computer_choice == 0 and self.user_choice == -1) or \
             (self.computer_choice == 1 and self.user_choice == 0):
            self.result_label.config(text=self.result_label.cget("text") + "\nYou win!")
            self.score["wins"] += 1
        else:
            self.result_label.config(text=self.result_label.cget("text") + "\nYou lose!")
            self.score["losses"] += 1

    def update_score(self):
        self.score_label.config(text=self.get_score())

    def get_score(self):
        return f"Wins: {self.score['wins']} | Losses: {self.score['losses']} | Draws: {self.score['draws']}"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()
