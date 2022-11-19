from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Button
def button_clicked():
    form_text = input_text.get()
    my_label.config(text=form_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#New Button
new_button = Button(text="Click Me Too")
new_button.grid(column=2, row=0)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label["text"] = "New Label"
my_label.config(text="even newer label", font=("Arial", 10, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Entry
input_text = Entry()
input_text["width"] = 10
input_text.grid(column=3, row=3)






window.mainloop()
