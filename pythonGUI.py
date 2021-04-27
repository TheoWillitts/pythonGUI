from tkinter import *

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
label.grid(row = 0, column = 2, sticky = N)

nameLabel = Label(window2, text = "Please enter your name: ", height = 1)
nameLabel.grid(row = 2, column = 1, sticky = W)

nameEntry = Entry(window2, width = 30, bg="light grey")
nameEntry.grid(row = 3, column = 1, sticky = W)

numberLabel = Label(window2, text = "Please enter your phone number: ", height = 1)
numberLabel.grid(row = 4, column = 1, sticky = W)

numberEntry = Entry(window2, width = 30, bg="light grey")
numberEntry.grid(row = 5, column = 1, sticky = W)

emailLabel = Label(window2, text = "Please enter your email: ", height = 1)
emailLabel.grid(row = 6, column = 1, sticky = W)

emailEntry = Entry(window2, width = 30, bg="light grey")
emailEntry.grid(row = 7, column = 1, sticky = W)

genderLabel = Label(window2, text = "Please enter your gender:", height = 1)
genderLabel.grid(row = 8, column = 1)

radiovar = StringVar()
rb = Radiobutton(window2, text="Male", variable=radiovar, value="Male")
rb.grid(row=9, column=0, sticky=N)

rb = Radiobutton(window2, text="Female", variable=radiovar, value="Female")
rb.grid(row=9, column=1, sticky=N)

window2.mainloop()