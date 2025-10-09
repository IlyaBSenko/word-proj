# import gui
import random

with open("words.txt", "r") as f:
    exec(f.read())
    
random_word_easy = random.choice(easy_words)
random_word_easy_sorted = sorted(random_word_easy)
sorted_string_easy = "".join(random_word_easy_sorted)
user_input = input(f"Guess the word: {sorted_string_easy} ")

if user_input == random_word_easy:
    print("Nice")
else:
    print("WRONG")