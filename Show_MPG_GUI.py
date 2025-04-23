#Tanner Rosenthal
#4/23/25
#Show MPG GUI

import tkinter

class MyGUI:
     def __init__(self):
         self.main_window = tkinter.Tk()

         self.gallons_label = tkinter.Label(self.main_window, text="How many gallons of gas does your car hold?")
         self.gallons_label.pack()
         self.gallons_entry = tkinter.Entry(self.main_window)
         self.gallons_entry.pack()

         self.miles_label = tkinter.Label(self.main_window, text="How many miles can your car drive on a full tank?")
         self.miles_label.pack()
         self.miles_entry = tkinter.Entry(self.main_window)
         self.miles_entry.pack()

         self.result_label = tkinter.Label(self.main_window, text="")
         self.result_label.pack()

         self.calc_button = tkinter.Button(self.main_window, text="Calculate MPG", command=self.show_info)
         self.calc_button.pack()



     def show_info(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles / gallons
        self.result_label.config(text=f"Miles Per Gallon: {mpg:.2f}")


my_gui = MyGUI()
tkinter.mainloop()
