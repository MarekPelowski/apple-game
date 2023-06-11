from tkinter import *
from random import randint, randrange

root = Tk()
root.geometry("1000x500")
root.configure(bg="black")
root.resizable(False, False)



x_apple = randrange(0, 920, 5)
y_apple = randrange(0, 420, 5)

x_player = 0
y_player = 0

player_speed = 5

apple_img = PhotoImage(file=r"apple.png")
player_right_img = PhotoImage(file=r"player_right.png")
player_left_img = PhotoImage(file=r"player_left.png")
player_up_img = PhotoImage(file=r"player_up.png")
player_down_img = PhotoImage(file=r"player_down.png")

def moving(event):
    global x_player
    global y_player

    hitting_apple()

    if event.keysym == 'w':
        y_player = y_player - player_speed
        player.place(y=y_player)
        player.configure(image=player_up_img)
        hitting_apple()

    elif event.keysym == 'a':
        x_player = x_player - player_speed
        player.place(x=x_player)
        player.configure(image=player_left_img)
        hitting_apple()

    elif event.keysym == 's':
        y_player = y_player + player_speed
        player.place(y=y_player)
        player.configure(image=player_down_img)
        hitting_apple()

    elif event.keysym == 'd':
        x_player = x_player + player_speed
        player.place(x=x_player)
        player.configure(image=player_right_img)
        hitting_apple()

def hitting_apple():


# from the left

    if x_player == (x_apple - 40) and y_player >= y_apple and y_player < (y_apple + 40):
        apple.destroy()
    elif x_player == (x_apple - 40) and y_player <= y_apple and y_player > (y_apple - 85):
        apple.destroy()

# from the bottom










apple = Label(root, image=apple_img, borderwidth=0, bg="black")
apple.place(x=x_apple, y=y_apple)

player = Label(root, image=player_right_img, borderwidth=0, bg="black")
player.place(x=x_player, y=y_player)

root.bind("<Key>", moving)

hitting_apple()

root.mainloop()