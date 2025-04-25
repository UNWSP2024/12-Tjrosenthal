#Tanner Rosenthal
#4/24/25
#Phone Call GUI

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.services = {
            'Daytime': 0.02,
            'Evening': 0.12,
            'Off-Peak': 0.05
        }

        self.rate_var = tkinter.StringVar()
        self.rate_var.set('Daytime')

        self.radio_frame = tkinter.LabelFrame(self.main_window, text="Select Rate Category")
        self.radio_frame.pack(padx=10, pady=10)


        for rate in self.services:
            tkinter.Radiobutton(self.radio_frame,
                           text=rate,
                           variable=self.rate_var,
                           value=rate).pack(anchor='w')

        self.entry_frame = tkinter.Frame(self.main_window)
        self.entry_frame.pack(pady=10)

        self.minutes_label = tkinter.Label(self.entry_frame, text='Enter Minutes')
        self.minutes_label.pack(side='left')

        self.minutes_entry = tkinter.Entry(self.entry_frame, width=10)
        self.minutes_entry.pack(side='left')

        self.calculate_button = tkinter.Button(self.main_window, text='Calculate', command=self.calculate_charge)
        self.calculate_button.pack()

        self.main_window.mainloop()

    def calculate_charge(self):
        minutes = float(self.minutes_entry.get())
        rate_type = self.rate_var.get()
        rate = self.services[rate_type]
        total = minutes * rate
        tkinter.messagebox.showinfo("Charge", f"Total cost: ${total:.2f}")


my_gui = MyGUI()
