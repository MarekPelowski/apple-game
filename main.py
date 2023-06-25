from tkinter import *
from random import randrange
import os
import sys

root = Tk()
root.geometry("1000x500")
root.configure(bg="black")
root.resizable(False, False)
root.title("Apple Game")

score_number = 0
countdown_number = 60

score = IntVar()
score.set(score_number)

countdown_var = IntVar()
countdown_var.set(countdown_number)


x_apple = randrange(0, 920, 5)
y_apple = randrange(0, 420, 5)

x_player = 100
y_player = 210

player_speed = 5

apple_img = PhotoImage(file=r"apple.png")
player_right_img = PhotoImage(file=r"player_right.png")
player_left_img = PhotoImage(file=r"player_left.png")
player_up_img = PhotoImage(file=r"player_up.png")
player_down_img = PhotoImage(file=r"player_down.png")

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def try_again():


    your_score1 = Label(root, text="Your score is: ", font=("Arial", 40, "bold"), bg="white", fg="black")
    your_score1.place(x=30, y=30)

    your_score2 = Label(root, text=score_number, font=("Arial", 40, "bold"), bg="white", fg="black")
    your_score2.place(x=420, y=30)

    try_again_button = Button(root, text="Try Again?", fg="black", font=("Arial", 25, "bold"), borderwidth=0, command=restart_program)
    try_again_button.place(x=30, y=150)

def destroy_all_widgets():
    player.destroy()
    apple.destroy()
    countdown1_label.destroy()
    countdown2_label.destroy()
    score1_label.destroy()
    score2_label.destroy()


def tksleep(t):
    ms = int(t+1000)
    var = IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    '''
    from the internet
    '''

def countdown():
    global countdown_number

    for x in range(60):
        tksleep(1)
        countdown_number = countdown_number - 1
        countdown_var.set(countdown_number)
    destroy_all_widgets()
    try_again()




def hitting_border():
    global y_player, x_player

    if y_player == 0:
        y_player = y_player + 50
    elif y_player == 420:
        y_player = y_player - 50
    elif x_player == 0:
        x_player = x_player + 50
    elif x_player == 920:
        x_player = x_player - 50


def make_apple():
    global x_apple
    global y_apple
    global apple

    x_apple = randrange(0, 920, 5)
    y_apple = randrange(0, 420, 5)

    apple = Label(root, image=apple_img, borderwidth=0, bg="black")
    apple.place(x=x_apple, y=y_apple)

def moving(event):
    global x_player
    global y_player

    hitting_apple()
    hitting_border()

    if event.keysym == 'w':
        y_player = y_player - player_speed
        player.place(y=y_player)
        player.configure(image=player_up_img)


    elif event.keysym == 'a':
        x_player = x_player - player_speed
        player.place(x=x_player)
        player.configure(image=player_left_img)


    elif event.keysym == 's':
        y_player = y_player + player_speed
        player.place(y=y_player)
        player.configure(image=player_down_img)


    elif event.keysym == 'd':
        x_player = x_player + player_speed
        player.place(x=x_player)
        player.configure(image=player_right_img)


def hitting_apple():
    global score_number



# from the left

    if x_player == (x_apple - 40) and y_player >= y_apple and y_player < (y_apple + 40):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number)
    elif x_player == (x_apple - 40) and y_player <= y_apple and y_player > (y_apple - 85):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number)


# from the bottom

    elif x_player >= x_apple and x_player <= (x_apple + 40) and y_player == (y_apple + 40):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number)
    elif x_player <= x_apple and x_player >= (x_apple - 40) and y_player == (y_apple + 40):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number)


# from the top

    elif x_player >= x_apple and x_player <= (x_apple + 40) and y_player == (y_apple - 80):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number)

    elif x_player <= x_apple and x_player >= (x_apple - 40) and y_player == (y_apple - 80):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number)



# from the right

    if x_player == (x_apple + 40) and y_player >= y_apple and y_player < (y_apple + 40):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number + 1)

    elif x_player == (x_apple + 40) and y_player <= y_apple and y_player > (y_apple - 85):
        apple.destroy()
        make_apple()
        score_number = score_number + 1
        score.set(score_number + 1)





apple = Label(root, image=apple_img, borderwidth=0, bg="black")
apple.place(x=x_apple, y=y_apple)

player = Label(root, image=player_right_img, borderwidth=0, bg="black")
player.place(x=x_player, y=y_player)


score1_label = Label(root, text="score: ", font=("Arial", 20, "bold"), bg="white", fg="black")
score1_label.place(x=20, y=20)

score2_label = Label(root, textvariable=score, font=("Arial", 20, "bold"), bg="white", fg="black")
score2_label.place(x=110, y=20)


countdown1_label = Label(root, text="Timer: ", font=("Arial", 20, "bold"), bg="white", fg="black")
countdown1_label.place(x=20, y=80)

countdown2_label = Label(root, textvariable=countdown_var, font=("Arial", 20, "bold"), bg="white", fg="black")
countdown2_label.place(x=120, y=80)


root.bind("<Key>", moving)


countdown()

hitting_apple()

root.mainloop()