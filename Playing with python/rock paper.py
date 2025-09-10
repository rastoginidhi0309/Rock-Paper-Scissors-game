from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry('300x300')
root.config(bg='Orange')

l1 = Label(root,
           text="Rock Paper Scissor",
           font=("Arial", 14, "bold"),
           bg="white",
           borderwidth=2,
           relief="solid"
           )
l1.pack(side=TOP, pady=10, padx=5)

l2 = Label(root,
           text="You Choose.....",
           font=("Arial", 10, "bold"),
           bg="white",
           width=30,
           borderwidth=1,
           relief="solid"
           )
l2.pack(side=TOP, pady=10, padx=5)

l3 = Label(root,
           text="Computer Choose.....",
           font=("Arial", 10, "bold"),
           bg="white",
           width=30,
           borderwidth=1,
           relief="solid"
           )
l3.pack(pady=5)

l4 = Label(root,
           text="Match Results",
           font=("Arial", 10, "bold"),
           bg="white",
           width=30,
           borderwidth=1,
           relief="solid"
           )
l4.pack(pady=5)

def check(op):
    options = ["Rock", "Paper", "Scissor"]
    cop = random.randint(0, 2)
    l2.config(text=f"You Choose: {options[op]}")
    l3.config(text=f"Computer Choose: {options[cop]}")
    if op == cop:
        l4.config(text="Match Draw")
    elif (op == 0 and cop == 2) or (op == 1 and cop == 0) or (op == 2 and cop == 1):
        l4.config(text="You Win")
    else:
        l4.config(text="Computer Wins")

b1 = Button(root,
            text="Rock",
            font=("Arial", 10),
            bg="red",
            width=7,
            command=lambda: check(0)
            )
b1.place(x=20, y=150)

b2 = Button(root,
            text="Paper",
            font=("Arial", 10),
            bg="white",
            width=7,
            command=lambda: check(1)
            )
b2.place(x=110, y=150)

b3 = Button(root,
            text="Scissor",
            font=("Arial", 10),
            bg="blue",
            fg="white",
            width=7,
            command=lambda: check(2)
            )
b3.place(x=200, y=150)

root.mainloop()
