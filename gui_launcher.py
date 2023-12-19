# Launcher for Graphical User Interface

import threading
import customtkinter as ctk
import tkinter.messagebox

from bulkArchiver import bulk_archiver


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title('File Management Toolkit')

        # Input for directory
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
