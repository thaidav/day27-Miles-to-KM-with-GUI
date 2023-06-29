from tkinter import *


window = Tk()
window.title("Miles to Kilometers")
window.geometry("300x200")
window.config(pady=20)

result = 0

input = Entry(width=15)
input.grid(column=2, row=2)

label1_Miles = Label(text="Miles", font=("Arial", 20,))
label1_Miles.grid(column=3, row=2)

label2_Equal = Label(text="is equal to", font=("Arial", 20,))
label2_Equal.grid(column=1, row=3)

label3_Km = Label(text="Km", font=("Arial", 20,))
label3_Km.grid(column=3, row=3)

label4_result = Label(text=result, font=("Arial", 20,))
label4_result.grid(column=2, row=3)


def button_clicked():
    print("Hello")
    new_input = float(input.get())
    calculated_result = new_input*1.60934
    result = round(calculated_result, 2)
    label4_result.config(text=result)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=4)














window.mainloop()