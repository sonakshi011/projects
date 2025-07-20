import tkinter as tk
from tkinter import messagebox
import random
import pygame

pygame.mixer.init()

click_sound = "click.mp3"
win_sound = "win.mp3"

def play_sound(sound_file):
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except:
        print(f"Missing sound file: {sound_file}")

root = tk.Tk()
root.title("Tic-Tac-Toe 🎮")

window_size = 600
root.geometry(f"{window_size}x{window_size + 100}")
root.configure(bg="#282C34")

current_player = "X"
board = [""] * 9
single_player = True 

def ai_move():
    empty_cells = [i for i in range(9) if board[i] == ""]
    if empty_cells:
        index = random.choice(empty_cells)
        on_click(index)

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)  
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Tie"
    return None

def on_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, fg="blue" if current_player == "X" else "red")
        play_sound(click_sound)

        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie! 🤝")
            else:
                play_sound(win_sound)
                messagebox.showinfo("Game Over", f"🎉 Player {winner} Wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            if single_player and current_player == "O":
                root.after(500, ai_move)

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

frame = tk.Frame(root, bg="#282C34")
frame.place(relx=0.5, rely=0.4, anchor="center")  

buttons = []
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 36, "bold"), width=6, height=3, 
                    bg="#61AFEF", activebackground="#98C379", relief="raised",
                    command=lambda i=i: on_click(i))
    btn.grid(row=i // 3, column=i % 3, padx=10, pady=10) 
    buttons.append(btn)

reset_btn = tk.Button(root, text="Restart Game 🔄", font=("Arial", 16, "bold"),
                      bg="#E06C75", fg="white", command=reset_board)
reset_btn.place(relx=0.5, rely=0.9, anchor="center")  


root.mainloop()
