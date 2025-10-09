from tkinter import * 
import random


def submit():
    guess = entry.get().strip()
    if guess.lower() == random_word:
        result_label.config(text="Lol nice")
    else:
        result_label.config(text="Wrong, die")

window = Tk()
window.title("PLACEHOLDER TITLE")
window.geometry("600x600")
window.config(background="#550000")

with open("words.txt", "r") as f:
    exec(f.read()) # executive mode cmon now (Top Dogs Only)
    
random_word = random.choice(easy_words) # select a random word from the list
sorted_word = sorted(random_word)
sorted_string = "".join(sorted_word)


# GUI ELEMENTS
title_label = Label(window, text="Word Guessr", font=("Segoe Script Bold", 24, "bold"), bg="#550000")
title_label.pack(pady=20)

guess_word_label = Label(window, text="Guess the word:", font=("Palatino Linotype Bold Italic", 16), bg="#550000")
guess_word_label.pack(pady=21)

rand_word = Label(window, text=sorted_string, font=("Palatino Linotype Bold Italic", 12), bg="#550000")
rand_word.pack()

entry = Entry(window, font=("Palatino Linotype Bold Italic", 14))
entry.place(relx=0.5, rely=0.7, anchor="center") 
entry.focus_set() # clutch lets you start typing immediately without needing to click the box first

result_label = Label(window, text="", bg="#550000", fg="white", font=("Palatino Linotype Bold Italic", 14))
result_label.pack(pady=8)

submit_button = Button(window, text="Enter", command=submit)
submit_button.place(relx=0.5, rely=0.9, anchor="center")

window.bind("<Return>", lambda e: submit()) # connects keyboard enter button to submit button, clutch

window.mainloop()