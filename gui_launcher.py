# Launcher for Graphical User Interface

import threading
import customtkinter as ctk
import tkinter.messagebox
from tkinter import Label, Canvas
from PIL import Image, ImageTk
from pathlib import Path

from bulkArchiver import bulk_archiver


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title('File Management Toolkit')

        # Side frame
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.pack(side='left', fill='y')

        # Main content frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side='right', fill='both', expand=True)

        # Initialize BulkArchiver
        self.bulk_archiver = BulkArchiver(self.main_frame)
        self.show_archiver_button = ctk.CTkButton(self.sidebar_frame, text='Bulk Archiver',
                                                  command=self.show_bulk_archiver)
        self.show_archiver_button.pack(pady=10)

    def show_bulk_archiver(self):
        # Clear the main frame and display BulkArchiver
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.bulk_archiver = BulkArchiver(self.main_frame)
        self.bulk_archiver.pack(fill='both', expand=True)


class BulkArchiver(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Logo
        base_path = Path(__file__).parent
        logo_path = base_path / 'static' / 'logo.png'
        pil_image = Image.open(logo_path)
        pil_image = pil_image.resize((100, 100), Image.Resampling.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(pil_image)
        self.logo_label = Label(self, image=self.logo_image, bg=self['bg'], borderwidth=0, highlightthickness=0)
        self.logo_label.pack(pady=20)

        self.directory_label = ctk.CTkLabel(self, text='Directory:')
        self.directory_label.pack(padx=20, pady=10)
        self.directory_entry = ctk.CTkEntry(self)
        self.directory_entry.pack(padx=20, pady=10)

        # Input for excluded extensions
        self.exclude_label = ctk.CTkLabel(self, text='Exclude Extensions (comma-separated):')
        self.exclude_label.pack(padx=20, pady=10)
        self.exclude_entry = ctk.CTkEntry(self)
        self.exclude_entry.pack(padx=20, pady=10)

        # Button to execute bulk_archiver
        self.archive_button = ctk.CTkButton(self, text='Archive', command=self.archive_files)
        self.archive_button.pack(padx=20, pady=10)

    def archive_files(self):
        directory = self.directory_entry.get()
        exclude_str = self.exclude_entry.get()
        exclude_extensions = set(exclude_str.split(',')) if exclude_str else None

        # Threading for long-running operations
        threading.Thread(target=self.run_archiving, args=(directory, exclude_extensions)).start()

    def run_archiving(self, directory, exclude_extensions):
        contents, efficiency = bulk_archiver(directory, exclude_extensions)
        tkinter.messagebox.showinfo("Archiving Complete", "Archiving is complete")
        print('Files in ZIP:', contents)
        print('Compression Efficiency: {:.2f}'.format(efficiency))


app = App()
app.mainloop()
