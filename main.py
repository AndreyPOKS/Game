import tkinter as tk
import random
C = 0
i = 3


def add_label1():
    global i
    i = 3
    btk3 = tk.Button(win, text="try your luck",bg="#f0c4ff", command=get_entry)
    btk3.grid(row=4, column=0)
    global C
    C = random.randrange(10)
    print(C)
def get_entry():
    value = number.get()
    global C
    global i
    if value:
        i = i - 1
        label4 = tk.Label(win, text=i, bg="#f0c4ff", ).grid(row=7, column=0)
        if i <= 0:
            blose = tk.Button(win, text="!!You Loser!!",bg="#f0c4ff", state=tk.DISABLED).grid(row=4, column=0)

        if int(value) != C:
            if int(value) > C:
                    label3 = tk.Label(win, text="your number bigger", bg="#f0c4ff",).grid(row=5, column=0)

            elif int(value) < C:
                    label3 = tk.Label(win, text="your number smaller", bg="#f0c4ff",).grid(row=5, column=0)
        else:
            bwin = tk.Button(win, text="You Winner!!!",bg="#f0c4ff", state=tk.DISABLED).grid(row=4, column=0)
    else:
            print("Error")


win = tk.Tk()
photo = tk.PhotoImage(file="icon.png")
win.config(bg="#de7aff")
win.iconphoto(False, photo)
win.title("Угадай число/POKS44b")
win.geometry("655x600+100+200")
win.resizable(False, False)
number = tk.Entry(win,)
label_2 = tk.Label(win, text="Это игра угадай число. "
                                 "Суть игры отгадать число, "
                                 "которое придумал ПК от 0 до 10,"
                                 " за 3 попытки",
                       bg="#de7aff",
                       fg="white",
                       font=("Arial", 10, "bold"),
                       relief=tk.RAISED,
                       bd=10
                       )
label_2.grid(row=0, column=0)
btk1 = tk.Button(win, text="Play", command=add_label1,
                    bg="#de7aff",
                    fg="white",
                    font=("Arial", 20, "bold"),
                    relief=tk.RAISED,
                    bd=10
                  )
label4 = tk.Label(win, text=i, bg="#f0c4ff", ).grid(row=7, column=0)
label4 = tk.Label(win, text="Life", bg="#f0c4ff", ).grid(row=6, column=0)
number.grid(row=3, column=0)
btk1.grid(row=1, column=0)
win.mainloop()