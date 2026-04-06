"""
gui.py
------
This program creates a GUI that allows the user to enter the values for two
piles to calculate the optimal move.
Also, two players can play Wythoff's game

Usage:
    python gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from wythoff.core import optimal_move


class WythoffApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wythoff's Game Analyzer")
        self.root.geometry("400x300")

        # Create tabbed interface
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10, fill="both", expand=True)

        self.calc_frame = ttk.Frame(self.notebook)
        self.play_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.calc_frame, text="Calculator")
        self.notebook.add(self.play_frame, text="Play Game")

        self.setup_calculator()
        self.setup_player()

    def setup_calculator(self):
        # Center the elements
        self.calc_frame.grid_columnconfigure(0, weight=1)
        self.calc_frame.grid_columnconfigure(1, weight=1)

        tk.Label(self.calc_frame, text="Pile 1:").grid(
            row=0, column=0, pady=10, sticky="e"
        )
        self.calc_entry1 = tk.Entry(self.calc_frame, width=10)
        self.calc_entry1.grid(row=0, column=1, pady=10, sticky="w")

        tk.Label(self.calc_frame, text="Pile 2:").grid(
            row=1, column=0, pady=5, sticky="e"
        )
        self.calc_entry2 = tk.Entry(self.calc_frame, width=10)
        self.calc_entry2.grid(row=1, column=1, pady=5, sticky="w")

        tk.Button(
            self.calc_frame, text="Compute Optimal Move", command=self.compute_move
        ).grid(row=2, columnspan=2, pady=15)

        self.calc_result = tk.StringVar()
        tk.Label(
            self.calc_frame, textvariable=self.calc_result, wraplength=350, fg="blue"
        ).grid(row=3, columnspan=2, pady=5)

    def compute_move(self):
        try:
            x = int(self.calc_entry1.get())
            y = int(self.calc_entry2.get())
            if x < 0 or y < 0:
                self.calc_result.set("Pile sizes must be non-negative.")
                return
            self.calc_result.set(optimal_move(x, y))
        except ValueError:
            self.calc_result.set("Please enter valid integers.")

    def setup_player(self):
        self.game_x = 0
        self.game_y = 0
        self.current_player = 1

        # Initialization Controls
        self.setup_frame = tk.Frame(self.play_frame)
        self.setup_frame.pack(pady=10)

        tk.Label(self.setup_frame, text="Init Pile 1:").grid(row=0, column=0)
        self.init_x = tk.Entry(self.setup_frame, width=5)
        self.init_x.grid(row=0, column=1, padx=5)

        tk.Label(self.setup_frame, text="Init Pile 2:").grid(row=0, column=2)
        self.init_y = tk.Entry(self.setup_frame, width=5)
        self.init_y.grid(row=0, column=3, padx=5)

        tk.Button(self.setup_frame, text="Start", command=self.start_game).grid(
            row=0, column=4, padx=5
        )

        # Game State Display
        self.game_info = tk.StringVar(value="Enter starting piles to begin.")
        tk.Label(
            self.play_frame, textvariable=self.game_info, font=("Arial", 12, "bold")
        ).pack(pady=10)

        # Interactive Controls (Hidden initially)
        self.move_frame = tk.Frame(self.play_frame)

        tk.Label(self.move_frame, text="Take from:").grid(row=0, column=0)
        self.move_action = tk.StringVar(value="1")
        tk.OptionMenu(self.move_frame, self.move_action, "1", "2", "both").grid(
            row=0, column=1, padx=5
        )

        tk.Label(self.move_frame, text="Amount:").grid(row=0, column=2)
        self.move_amt = tk.Entry(self.move_frame, width=5)
        self.move_amt.grid(row=0, column=3, padx=5)

        tk.Button(self.move_frame, text="Make Move", command=self.make_move).grid(
            row=0, column=4, padx=5
        )

        # Optimal Move Hint
        self.hint_var = tk.StringVar()
        tk.Label(self.play_frame, textvariable=self.hint_var, fg="gray").pack(pady=15)

    def start_game(self):
        try:
            self.game_x = int(self.init_x.get())
            self.game_y = int(self.init_y.get())
            if self.game_x < 0 or self.game_y < 0:
                messagebox.showerror("Error", "Piles must be non-negative.")
                return

            self.current_player = 1
            self.update_game_ui()
            self.move_frame.pack(pady=5)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")

    def update_game_ui(self):
        self.game_info.set(
            f"Player {self.current_player}'s Turn  |  State: ({self.game_x}, {self.game_y})"
        )
        self.hint_var.set(f"Hint: {optimal_move(self.game_x, self.game_y)}")

    def make_move(self):
        try:
            action = self.move_action.get()
            amt = int(self.move_amt.get())

            if amt <= 0:
                messagebox.showwarning("Invalid Move", "Amount must be greater than 0.")
                return

            if action == "both":
                if amt <= self.game_x and amt <= self.game_y:
                    self.game_x -= amt
                    self.game_y -= amt
                else:
                    messagebox.showwarning(
                        "Invalid Move", "Not enough items in both piles."
                    )
                    return
            elif action == "1":
                if amt <= self.game_x:
                    self.game_x -= amt
                else:
                    messagebox.showwarning(
                        "Invalid Move", "Not enough items in Pile 1."
                    )
                    return
            elif action == "2":
                if amt <= self.game_y:
                    self.game_y -= amt
                else:
                    messagebox.showwarning(
                        "Invalid Move", "Not enough items in Pile 2."
                    )
                    return

            # Win check
            if self.game_x == 0 and self.game_y == 0:
                self.game_info.set(f"Player {self.current_player} Wins!")
                self.move_frame.pack_forget()
                self.hint_var.set("")
            else:
                self.current_player = 2 if self.current_player == 1 else 1
                self.move_amt.delete(0, tk.END)
                self.update_game_ui()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer amount.")


def run_gui():
    root = tk.Tk()
    WythoffApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
