from tkinter import * 

def submit():
    return

window = Tk()
window.title("PLACEHOLDER TITLE")
window.geometry("400x300")
window.config(background="#550000")

# title label
title_label = Label(window, text="Word Guessr", font=("Segoe Script Bold", 24, "bold"), bg="#550000")
title_label.pack(pady=20)

word_label = Label(window, text="Guess the word:", font=("Palatino Linotype Bold Italic", 16), bg="#550000")
word_label.pack(pady=21)

entry = Entry(window, font=("Palatino Linotype Bold Italic", 14))
entry.place(relx=0.5, rely=0.7, anchor="center") # where the entry widget is on screen


submit_button = Button(window, text="Enter", command=submit)
submit_button.place(relx=0.5, rely=0.9, anchor="center")

window.mainloop()