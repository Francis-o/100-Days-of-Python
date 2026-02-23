from tkinter import *


def miles_to_km():
    try:
        miles_value = int(input_box.get())
        km_value = miles_value  * 1.609344
        formated_km_value = f"{km_value:.2f}"
        answer_label.config(text=formated_km_value)
    except:
        print("You entered an invalid input.")


window = Tk()
window.minsize(width=300, height=300)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

text_label = Label(text="is equal to ")
text_label.config(padx=20, pady= 20)
text_label.grid(column=0, row=1)

input_box = Entry(width=7, font=("Arial", 15))
# input_box.config(padx=20, pady= 20)
input_box.grid(column=1, row=0)

answer_label = Label(text="0")
answer_label.config(padx=20, pady= 20)
answer_label.grid(column=1, row=1)

button = Button(text="Calculate",  width=10, height=1, relief="raised", command=miles_to_km)
button.config(padx=10, pady= 10)
button.grid(column=1, row=2)

miles_label = Label(text="miles")
miles_label.config(padx=20, pady= 20)
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.config(padx=20, pady= 20)
km_label.grid(column=2, row=1)


window.mainloop()
