from tkinter import * 
import random


def submit():
    return

window = Tk()
window.title("PLACEHOLDER TITLE")
window.geometry("400x300")
window.config(background="#550000")

with open("words.txt", "r") as f:
    exec(f.read()) # executive mode cmon now (Top Dogs Only)
    

random_word_text = random.choice(easy_words) # wtf is choice, (select a random element from a sequence, aka easy_words in words)

# title label
title_label = Label(window, text="Word Guessr", font=("Segoe Script Bold", 24, "bold"), bg="#550000")
title_label.pack(pady=20)

Guess_word_label = Label(window, text="Guess the word:", font=("Palatino Linotype Bold Italic", 16), bg="#550000")
Guess_word_label.pack(pady=21)

rand_word = Label(window, text=random_word_text, font=("Palatino Linotype Bold Italic", 12), bg="#550000")
rand_word.pack()



entry = Entry(window, font=("Palatino Linotype Bold Italic", 14))
entry.place(relx=0.5, rely=0.7, anchor="center") 


submit_button = Button(window, text="Enter", command=submit)
submit_button.place(relx=0.5, rely=0.9, anchor="center")

window.mainloop()