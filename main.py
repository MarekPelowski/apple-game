from tkinter import *

root = Tk()
root.geometry("1000x500")
root.configure(bg="black")
root.resizable(False, False)

apple_img = PhotoImage(file=r"apple.png")
player_img = PhotoImage(file=r"player.png")

apple_image = Label(image=apple_img, borderwidth=0).pack()

player_image = Label(image=player_img, borderwidth=0).pack()

root.mainloop()