import Tkinter  # Button, Label, Frame
import random

COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

def stimulus(same):
    colors = list(COLORS)

    word = random.choice(colors)

    if same:
        return (word, word)

    colors.remove(word)

    color = random.choice(colors)

    return (word, color)

def next_selected():
    word, color = stimulus(random.choice((True, False)))

    label.config(text=word, fg=color)

    label.update()

def quit_selected():
    root.destroy()

root = Tkinter.Tk()

# create the window

# create label using stimulus
word, color = stimulus(True)
label = Tkinter.Label(root, text=word, fg=color)
label.pack()

closebutton = Tkinter.Button(root, text='close', command=quit_selected)
closebutton.pack(padx=50, pady=50)

nextbutton = Tkinter.Button(root, text='next', command=next_selected)
nextbutton.pack()

root.mainloop()