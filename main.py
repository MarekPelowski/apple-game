from tkinter import *
from random import randrange

root = Tk()
root.geometry("1000x500")
root.configure(bg="black")
root.resizable(False, False)
root.title("Apple Game")

score_number = 0

score = IntVar()
score.set(score_number)

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

def tksleep(t):
    ms = int(t+1000)
    var = IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    '''
    from the internet
    '''



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
        score.set(score_number + 1)

    elif x_player == (x_apple + 40) and y_player <= y_apple and y_player > (y_apple - 85):
        apple.destroy()
        make_apple()
        score.set(score_number + 1)





apple = Label(root, image=apple_img, borderwidth=0, bg="black")
apple.place(x=x_apple, y=y_apple)

player = Label(root, image=player_right_img, borderwidth=0, bg="black")
player.place(x=x_player, y=y_player)

score1_label = Label(root, text="score: ", font=("Arial", 20, "bold"), bg="white", fg="black")
score1_label.place(x=20, y=20)

score2_label = Label(root, textvariable=score, font=("Arial", 20, "bold"), bg="white", fg="black")
score2_label.place(x=110, y=20)

root.bind("<Key>", moving)

hitting_apple()

root.mainloop()