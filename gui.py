from tkinter import * 

def submit():
    return

window = Tk()
window.title("PLACEHOLDER TITLE")
window.geometry("400x300")
window.config(background="#550000")

submit = Button(window, text="Enter", command=submit)

entry = Entry()
entry.pack(pady=130) # where the entry widget is on screen


window.mainloop()