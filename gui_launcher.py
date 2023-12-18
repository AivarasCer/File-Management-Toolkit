# Launcher for Graphical User Interface

import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('400x150')
        self.title('File Management Toolkit')

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("button clicked")


app = App()
app.mainloop()
