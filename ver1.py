import tkinter as tk
from functools import partial

class Converter:
    def __init__(self, parent):
        #formatting variables
        background_color = 'light blue'

        self.converter_frame = tk.Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        self.temp_converter_label = tk.Label(self.converter_frame, text='Temperature Converter',
                                            font=('Arial', '16', 'bold'),
                                            padx=10, pady=10, bg=background_color)
        self.temp_converter_label.grid(row=0)

        self.help_button = tk.Button(self.converter_frame, text='help',
                                    padx=10, pady=10)
        self.help_button.grid(row=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    App = Converter(root)
    root.mainloop()