from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    french_words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_data = pandas.read_csv("data/french_words.csv")
data_list = french_words_data.to_dict(orient="records")
current_word = None

def meaning():
    canvas.itemconfig(canvas_settings, image=card_back_image)
    canvas.itemconfig(language_text, text = "English", fill="white")
    canvas.itemconfig(canvas_settings, image=card_back_image)
    canvas.itemconfig(word_text, text=current_word["English"], fill = "white")

def word_setup():
    canvas.itemconfig(canvas_settings, image=card_front_image)
    canvas.itemconfig(language_text, text = "French", fill="black")
    canvas.itemconfig(canvas_settings, image=card_front_image)
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")

def card_setup():
    global flip_timer, current_word
    window.after_cancel(flip_timer)
    current_word = random.choice(data_list)
    word_setup()
    flip_timer = window.after(3000, func=meaning)
    
def right_button():
    global data_list
    data = pandas.DataFrame(data_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    card_setup()
    data_list.remove(current_word)

#create window
window = Tk()
window.title("Flahy")
window.config(padx=50, pady=50,  bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=meaning)

#create canvas
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

#create image in canvvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_settings = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#create two buttons with images untop
right_button = Button(image=right_button_image, highlightthickness=0, command=right_button)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=card_setup)
wrong_button.grid(column=0, row=1)

card_setup()

window.mainloop()