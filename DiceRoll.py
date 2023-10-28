import tkinter as tk
import random

# main window, resize, and title.
root = tk.Tk()
root.geometry('400x400')
root.title('Roll Dice')

# label to display dice.
label =tk.Label(root, text='', font=('Helvetica', 260))

# function activated by button.
def roll_dice():
    # unicode character strings for dice.
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    print(f'{random.choice(dice)} {random.choice(dice)}')
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()

# button.
button = tk.Button(root, text='roll dice', foreground='green', command=roll_dice)

# pack a widget in the parent widget.
button.pack()

# call the main loop of Tk.
# keeps window open.
root.mainloop()