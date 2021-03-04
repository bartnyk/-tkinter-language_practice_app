from tkinter import *
import random

with open("data/words.csv", "r", encoding='utf-8') as data:
    rows = data.read().split("\n")
    print(rows)
    WORDS = {var[0]: var[1] for var in [x.split(",") for x in rows]}

BACKGROUND_COLOR = "#B1DDC6"

FROM = "Polish"
TO = "English"


# ---------- BACK-END ----------#

def change_word():
    card_canvas.itemconfig(to_translate, text=WORDS[random.choice(list(WORDS.keys()))])

def change_language():
    global FROM, TO
    FROM, TO = TO, FROM

def set_default():
    pass
# ---------- UI ----------#

window = Tk()
window.title("Language practice")
window.config(bg=BACKGROUND_COLOR, pady=80, padx=80)
window.resizable(False, False)

back_side = PhotoImage(file="images/card_front.png")
front_side = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_side = card_canvas.create_image(400, 263, image=front_side)
pl_en_button = Button(image=right, command=set_default, bg=BACKGROUND_COLOR, highlightthickness=0)
en_pl_button = Button(image=right, command=change_language)
pl_en = card_canvas.create_window(200, 163, window=pl_en_button)
en_pl = card_canvas.create_window(200, 343, window=en_pl_button)
temp1 = card_canvas.create_text(410, 163, text="from Polish to English", font=("Arial", 20, "italic bold"))
temp2 = card_canvas.create_text(410, 343, text="from English to Polish", font=("Arial", 20, "italic bold "))
language = card_canvas.create_text(400, 180, text="Polish", font=("Tahoma", 28))
to_translate = card_canvas.create_text(400, 300, text=WORDS[random.choice(list(WORDS.keys()))], font=("Arial", 28, "italic bold"))

card_canvas.grid(row=0, columnspan=2)

button_wrong = Button(height=100, width=100, image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=change_word)
button_right = Button(height=100, width=100, bg=BACKGROUND_COLOR, image=right, highlightthickness=0, command=change_word)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)

window.mainloop()
