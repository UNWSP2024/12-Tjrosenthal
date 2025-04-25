#Tanner Rosenthal
#4/24/25
#Check Box GUI

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.services = {
            'Oil Change': 30.00,
            'Lube Job': 20.00,
            'Radiator Flush': 40.00,
            'Transmission Fluid': 100.00,
            'Inspection': 35.00,
            'Muffler Replacement': 200.00,
            'Tire Rotation': 20.00
        }

        self.vars = {}

        for service in self.services:
            var = tkinter.IntVar()
            cb = tkinter.Checkbutton(self.main_window, text=f"{service} - ${self.services[service]:.2f}", variable=var)
            cb.pack(anchor='w')  # Align to the left
            self.vars[service] = var

        self.calc_button = tkinter.Button(self.main_window, text='Calculate Total', command=self.calculate_total)
        self.calc_button.pack()

        self.total_label = tkinter.Label(self.main_window, text="")
        self.total_label.pack()

        tkinter.mainloop()

    def calculate_total(self):
        total = 0.0
        for service, var in self.vars.items():
            if var.get() == 1:
                total += self.services[service]
        self.total_label.config(text=f"Total: ${total:.2f}")


my_gui = MyGUI()
