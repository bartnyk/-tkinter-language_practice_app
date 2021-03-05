from tkinter import *
import random

with open("data/words.csv", "r", encoding='utf-8') as data:
    rows = data.read().split("\n")
    WORDS = {var[0]: var[1] for var in [x.split(",") for x in rows]}

BACKGROUND_COLOR = "#B1DDC6"

FROM = None
TO = None

# ---------- BACK-END ----------#

def main():
    def change_card():
        card_canvas.itemconfig(current_language, text=TO, fill="white")
        card_canvas.itemconfig(to_translate, text=key, fill="white")
        card_canvas.itemconfig(card, image=back_side)

    def change_word(result):
        if result == "right":
            del WORDS[key]
        return main()

    key = random.choice(list(WORDS.keys()))
    word = WORDS[key]
    card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card = card_canvas.create_image(400, 263, image=front_side)
    card_canvas.grid(row=0, columnspan=2)
    current_language = card_canvas.create_text(400, 130, text=FROM, fill="black", font=("Arial", 26, "bold"))
    to_translate = card_canvas.create_text(400, 330, text=word, fill="black", font=("Arial", 28, "italic bold"))

    button_wrong = Button(height=100, width=100, image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=lambda: change_word("wrong"))
    button_right = Button(height=100, width=100, bg=BACKGROUND_COLOR, image=right, highlightthickness=0, command=lambda: change_word("right"))
    button_wrong.grid(row=1, column=0, pady=10)
    button_right.grid(row=1, column=1, pady=10)

    window.after(3000, change_card)


def choice():
    def change_language(fr, to):
        global FROM, TO, WORDS
        FROM = fr
        TO = to
        if FROM == "English":
            WORDS = {value: key for (key, value) in WORDS.items()}
        choice_canvas.delete("all")
        return main()
    choice_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    pl_en_button = Button(image=right, command=lambda: change_language("Polish", "English"), bg=BACKGROUND_COLOR, highlightthickness=0)
    en_pl_button = Button(image=right, command=lambda: change_language("English", "Polish"))
    choice_canvas.create_window(180, 163, window=pl_en_button)
    choice_canvas.create_window(180, 343, window=en_pl_button)
    choice_canvas.create_text(440, 163, text="from Polish to English", font=("Arial", 20, "italic bold"))
    choice_canvas.create_text(440, 343, text="from English to Polish", font=("Arial", 20, "italic bold "))
    choice_canvas.grid(row=0, columnspan=2)

def on_closing():
    global WORDS
    if FROM == "English":
        WORDS = {value: key for (key, value) in WORDS.items()}
    to_file = [f"{key}:{WORDS[key]}" for key in WORDS.keys()]
    print(to_file)
    with open("data/words.csv", "w", encoding='utf-8') as file:
        #file.writelines([f"{line}\n" for line in to_file])
        for line in to_file:
            if line != to_file[-1]:
                file.write(f"{line.replace(':', ',')}\n")
            else:
                file.write(f"{line.replace(':', ',')}")
    exit()

# ---------- UI ----------#

window = Tk()
window.title("Language practice")
window.config(bg=BACKGROUND_COLOR, pady=80, padx=80)
window.resizable(False, False)

front_side = PhotoImage(file="images/card_front.png")
back_side = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

choice()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
