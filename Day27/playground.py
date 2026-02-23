from tkinter import *
# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum

# print(add(2, 4,5,6, 7,3,4))

def handle_click():
    my_label["text"] = "Label"
    user_input = my_entry.get()
    print(user_input)

window = Tk()
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)
window.title("Practicee")
my_label = Label(text="My Label")
my_label.grid(column=0, row=0)
my_button = Button(text="Click Me!", command=handle_click)
my_button.grid(column=1, row=1)
new_button = Button(text="New Button", command=handle_click)
new_button.grid(column=2, row=0)
my_entry = Entry(width=10)
my_entry.grid(column=3, row=2)


window.mainloop()