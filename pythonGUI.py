from tkinter import *

d = {"one": "aardvark", "two": "abaca", "three": "aback"}

def button_click():
    typed_text = entry1.get()

    output_text.delete(0.0, END)
    try:
        meaning = d[typed_text]
    except:
        meaning = "The word you entered could not be found."

    output_text.insert(END, meaning)

def deleteAll():
    output_text.delete(0.0, END)
    output_text.insert(END, "Deleted All Text")



window = Tk() #creating a window (window is just a variable name)
window.title("Testing Tk") #Title for that window

menubar = Menu(window)

first_menu = Menu(menubar, tearoff=0)
first_menu.add_command(label="Delete All", command="deleteAll")
first_menu.add_command(label="Quit", command=window.destroy)
menubar.add_cascade(label="Tools", menu=first_menu)

second_menu = Menu(menubar, tearoff=0)
second_menu.add_command(label="Delete All", command="deleteAll")
second_menu.add_command(label="Quit", command=window.destroy)
menubar.add_cascade(label="Tools", menu=second_menu)

label1 = Label(window, text="Dictionary", width=30, height=2)
label1.grid(row = 0, column = 0, columnspan = 2, sticky = N)

entry1 = Entry(window, width=20,bg = "light green")
entry1.grid(row = 1, column = 0, sticky = E)

button1 = Button(window, text="SUBMIT", width = 5, command=button_click)
button1.grid(row=2, column=0, sticky = N)

output_text = Text(window, width=30, height=10, wrap=WORD, background="cyan")
output_text.grid(row=3, column=0, columnspan=2, sticky=S)

label2 = Label(window, text="Spinbox", width=30, height=2)
label2.grid(row = 4, column = 0, columnspan = 1, sticky = N)

v=IntVar()
spin = Spinbox(window, textvariable=v, from_=1, to=10)
spin.grid(row=4, column=1, sticky = E)

var1 = IntVar()
c1 =  Checkbutton(window, text="Check Once!", variable=var1)
c1.grid(row=5, column=0, sticky= N)

var2 = IntVar()
c2 =  Checkbutton(window, text="Check Twice!", variable=var2)
c2.grid(row=6, column=0, sticky= N)

var3 = IntVar()
c3 =  Checkbutton(window, text="Check Thrice!", variable=var3)
c3.grid(row=7, column=0, sticky= N)

radiovar = StringVar()
rb = Radiobutton(window, text="One", variable=radiovar, value="Option 1")
rb.grid(row=8, column=0, sticky=N)

rb = Radiobutton(window, text="Two", variable=radiovar, value="Option 2")
rb.grid(row=9, column=0, sticky=N)

rb = Radiobutton(window, text="Three", variable=radiovar, value="Option 3")
rb.grid(row=10, column=0, sticky=N)


canvas1 = Canvas(window, bg = "light blue", height=200, width=400)
canvas1.grid(row=11, column=0, sticky=W)

circle = canvas1.create_oval(50, 50, 150, 150, outline="blue", fill="blue")

square = canvas1.create_rectangle(50,50,100,150, outline="red", fill="red")

window.config(menu=menubar)

window.mainloop() #checks for any inputs or triggers (always looping)

window2 = Tk()
window2.title("Current")
window2.geometry("500x200")

#buttonA = Button(window2, text="SUBMIT", width = 10, height = 4, command=button_click)
#buttonA.grid(row=1, column=0)

#buttonB = Button(window2, text="SUBMIT", width = 10, height = 4, command=button_click)
#buttonB.grid(row=2, column=1)

#buttonC = Button(window2, text="SUBMIT", width = 10, height = 4, command=button_click)
#buttonC.grid(row=3, column=2)

label = Label(window2, text = "Welcome to my Registration Site", height = 2)
label.grid(row = 0, column = 0, sticky = N)

nameEntry = Entry(window2, width = 30, bg="light grey")
nameEntry.grid(row = 2, column = 0, sticky = W)

window2.mainloop()