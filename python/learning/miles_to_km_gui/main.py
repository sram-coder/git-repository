from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx = 20, pady = 20)

miles_input = Entry()
miles_input.grid(column = 1, row = 0)
#Labels
mile_label = Label(text="Miles", font = ("Arial", 15))
mile_label.grid(column = 2, row = 0)

eq_label = Label(text = "is equal to", font = ("Arial", 15))
eq_label.grid(column = 0, row = 1)

km_result_label = Label(text = "0", font = ("Arial", 15))
km_result_label.grid(column = 1, row = 1)

km_label = Label(text = "Km", font = ("Arial", 15))
km_label.grid(column = 2, row = 1)


def miles_to_km():
    miles = int(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

calculate_button = Button(text = "Calculate", command = miles_to_km)
calculate_button.grid(column = 1, row = 2)


window.mainloop()