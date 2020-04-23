import tkinter as tk
from functools import partial

class Converter:
    def __init__(self, parent):
        background_color = 'light blue'

        self.converter_frame = tk.Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        self.temp_converter_label = tk.Label(self.converter_frame, text='Temperature Converter',
                                            font=('Arial', '16', 'bold'),
                                            padx=10, pady=10, bg=background_color)
        self.temp_converter_label.grid(row=0)

        self.help_button = tk.Button(self.converter_frame, text='help',
                                    padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text='Help Text Goes Here')


class Help:
    def __init__(self, partner):
        background = 'orange'
        partner.help_button.config(state='disabled')

        self.help_box = tk.Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = tk.Frame(self.help_box, width=600, height=600, bg=background, pady=10)
        self.help_frame.grid()
        # Set up Help Heading (row 0)
        self.how_heading = tk.Label(self.help_frame, text="Help / Instructions",
                                    font='arial 30 bold', bg=background)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = tk.Label(self.help_frame, text='',
                                justify='left', width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)
        # Dismiss button (row 2)
        self.dismiss_btn = tk.Button(self.help_frame, text='Dismiss',
                                    width=10, bg='orange', font='arial 10 bold',
                                    command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state='normal')
        self.help_box.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    App = Converter(root)
    root.mainloop()