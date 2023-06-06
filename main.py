from tkinter import *
from random import randint

root = Tk()
root.geometry("1000x500")
root.configure(bg="black")
root.resizable(False, False)

x_apple = randint(0, 920)
y_apple = randint(0, 420)

x_player = 30
y_player = 180

player_speed = 7

def moving(event):
    global x_player
    global y_player
    if event.keysym == 'd':
        x_player = x_player + player_speed
        player.place(x=x_player)


apple_img = PhotoImage(file=r"apple.png")
player_img = PhotoImage(file=r"player.png")

apple = Label(root, image=apple_img, borderwidth=0, bg="black")
apple.place(x=x_apple, y=y_apple)

player = Label(root, image=player_img, borderwidth=0, bg="black")
player.place(x=x_player, y=y_player)

root.bind("<Key>", moving)


root.mainloop()