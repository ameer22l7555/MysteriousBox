import tkinter as tk
from random import shuffle, randint
from tkinter import messagebox

class MysteryBoxGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Mystery Box Game")
        self.master.configure(bg="#f0f0f0")
        self.num_boxes = 20
        self.boxes_buttons = []
        self.players = ['Player 1', 'Player 2']
        self.current_player = self.players[0]

        self.turn_label = tk.Label(self.master, text=f"Turn: {self.current_player}", bg="#f0f0f0", font=("Arial", 12))
        self.turn_label.grid(row=self.num_boxes // 4 + 1, column=0, columnspan=self.num_boxes // 4)

        self.create_buttons()
        self.start_game()

    def create_buttons(self):
        for index in range(self.num_boxes):
            button = tk.Button(self.master, text='?', width=10, height=3, bg="#ffffff", fg="#000000",
                               font=("Arial", 10, "bold"), relief="groove",
                               command=lambda idx=index: self.reveal_box(idx))
            button.grid(row=index // 4, column=index % 4)
            self.boxes_buttons.append(button)

    def start_game(self):
        self.reset_game()
        self.prize_position = randint(0, self.num_boxes - 1)
        self.boxes = [''] * self.num_boxes
        self.boxes[self.prize_position] = 'Suicide'
        shuffle(self.boxes)

    def reveal_box(self, index):
        if self.boxes[index] == 'Suicide':
            self.boxes_buttons[index].config(text='Suicide', state='disabled', bg="#990000", fg="#ffffff")
            messagebox.showinfo("End of Game", f"{self.current_player} shot himself!\n{self.current_player} Lost!")
            self.ask_play_again()
        else:
            self.boxes_buttons[index].config(text='Empty', state='disabled', bg="#0090ff", fg="#ffffff")
            self.switch_player()
            self.update_turn_label()

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def update_turn_label(self):
        self.turn_label.config(text=f"Turn: {self.current_player}")

    def reset_game(self):
        for button in self.boxes_buttons:
            button.config(text='?', state='normal', bg="#ffffff", fg="#000000")
        
        self.current_player = self.players[0]
        self.update_turn_label()

    def ask_play_again(self):
        response = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if response:
            self.start_game()
        else:
            self.master.destroy()

def main():
    root = tk.Tk()
    root.configure(bg="#f0f0f0")
    game = MysteryBoxGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()