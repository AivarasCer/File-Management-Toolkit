# Launcher for Graphical User Interface

import customtkinter as ctk


def button_callback():
    print("button clicked")

app = ctk.CTk()
app.geometry('400x150')
app.title('File Management Toolkit')

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()
