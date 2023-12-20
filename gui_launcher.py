# Launcher for GUI

import threading
import customtkinter as ctk
import tkinter.messagebox
from tkinter import Label, filedialog, Toplevel
from PIL import Image, ImageTk
from pathlib import Path

from bulkArchiver import bulk_archiver
from selectiveArchiver import selective_archiver


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
        self.show_archiver_button.pack(padx=10, pady=3)

        # Initialize SelectiveArchiver
        self.selective_archiver = SelectiveArchiver(self.main_frame)
        self.show_archiver_button = ctk.CTkButton(self.sidebar_frame, text='Selective Archiver',
                                                  command=self.show_selective_archiver)
        self.show_archiver_button.pack(padx=10, pady=3)

        # Initialize DirOrganizer
        self.dir_organizer = DirOrganiser(self.main_frame)
        self.show_organizer_button = ctk.CTkButton(self.sidebar_frame,
                                                   text='Directory Organizer', command=self.show_dir_organizer)
        self.show_organizer_button.pack(padx=10, pady=3)

    # Clear the main frame and display BulkArchiver
    def show_bulk_archiver(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.bulk_archiver = BulkArchiver(self.main_frame)
        self.bulk_archiver.pack(fill='both', expand=True)

    # Clear the main frame and display SelectiveArchiver
    def show_selective_archiver(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.selective_archiver = SelectiveArchiver(self.main_frame)
        self.selective_archiver.pack(fill='both', expand=True)

    # Clear the main frame and display SelectiveArchiver
    def show_dir_organizer(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.dir_organizer = DirOrganiser(self.main_frame)
        self.dir_organizer.pack(fill='both', expand=True)


class BulkArchiver(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Logo
        base_path = Path(__file__).parent
        logo_path = base_path / 'static' / 'ba_logo.png'
        pil_image = Image.open(logo_path)
        self.logo_image = ImageTk.PhotoImage(pil_image)
        self.logo_label = Label(self, image=self.logo_image, bg=self['bg'], borderwidth=0, highlightthickness=0)
        self.logo_label.pack(pady=20)

        # Title text
        self.title_label = ctk.CTkLabel(self, text="Bulk Archiver", font=("Arial", 25))
        self.title_label.pack()

        # Browse for Directory
        self.directory_label = ctk.CTkLabel(self, text='Directory:')
        self.directory_label.pack(padx=20, pady=10)
        self.directory_entry = ctk.CTkEntry(self)
        self.directory_entry.pack(padx=20, pady=10)
        self.browse_button = ctk.CTkButton(self, text='Browse', command=self.browse_directory)
        self.browse_button.pack(padx=20, pady=10)

        # Input for excluded extensions
        self.exclude_label = ctk.CTkLabel(self, text='Exclude Extensions (comma-separated):')
        self.exclude_label.pack(padx=20, pady=10)
        self.exclude_entry = ctk.CTkEntry(self)
        self.exclude_entry.pack(padx=20, pady=10)

        # Button to execute bulk_archiver
        self.archive_button = ctk.CTkButton(self, text='Archive', command=self.archive_files)
        self.archive_button.pack(padx=20, pady=10)

        # Help button
        self.help_button = ctk.CTkButton(self, text='?', width=20, height=20, command=self.show_help_popup)
        self.help_button.place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")

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

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, 'end')
            self.directory_entry.insert(0, directory)

    def show_help_popup(self):
        popup = Toplevel(self)
        popup.title("Help")
        popup.geometry("350x250")
        Label(popup, text='''
        Bulk Archiver - File Management Toolkit
        ---------------------------------------
        This program helps you to archive files in a selected directory.

        Features:
        - Browse and select a directory to archive.
        - Exclude specific file extensions from archiving.
        - View archiving status and results.

        How to Use:
        1. Click 'Browse' to select a directory.
        2. Enter file extensions to exclude (optional).
        3. Click 'Archive' to start the archiving process.''',
              justify="left").pack(padx=10, pady=10)


class SelectiveArchiver(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Logo
        base_path = Path(__file__).parent
        logo_path = base_path / 'static' / 'sa_logo.png'
        pil_image = Image.open(logo_path)
        self.logo_image = ImageTk.PhotoImage(pil_image)
        self.logo_label = Label(self, image=self.logo_image, bg=self['bg'], borderwidth=0, highlightthickness=0)
        self.logo_label.pack(pady=20)

        # Title text
        self.title_label = ctk.CTkLabel(self, text="Selective Archiver", font=("Arial", 25))
        self.title_label.pack()

        # Browse for Directory
        self.directory_label = ctk.CTkLabel(self, text='Directory:')
        self.directory_label.pack(padx=20, pady=10)
        self.directory_entry = ctk.CTkEntry(self)
        self.directory_entry.pack(padx=20, pady=10)
        self.browse_button = ctk.CTkButton(self, text='Browse', command=self.browse_directory)
        self.browse_button.pack(padx=20, pady=10)

        # Input for extensions to archieve
        self.exclude_label = ctk.CTkLabel(self, text='Enter Extensions (comma-separated):')
        self.exclude_label.pack(padx=20, pady=10)
        self.exclude_entry = ctk.CTkEntry(self)
        self.exclude_entry.pack(padx=20, pady=10)

        # Button to execute selective_archiver
        self.archive_button = ctk.CTkButton(self, text='Archive', command=self.archive_files)
        self.archive_button.pack(padx=20, pady=10)

        # Help button
        self.help_button = ctk.CTkButton(self, text='?', width=20, height=20, command=self.show_help_popup)
        self.help_button.place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, 'end')
            self.directory_entry.insert(0, directory)

    def archive_files(self):
        directory = self.directory_entry.get()
        exclude_str = self.exclude_entry.get()
        extensions = set(exclude_str.split(','))

        # Threading for long-running operations
        threading.Thread(target=self.run_archiving, args=(directory, extensions)).start()

    def run_archiving(self, directory, extensions):
        contents, efficiency = selective_archiver(directory, extensions)
        tkinter.messagebox.showinfo("Archiving Complete", "Archiving is complete")
        print('Files in ZIP:', contents)
        print('Compression Efficiency: {:.2f}'.format(efficiency))

    def show_help_popup(self):
        popup = Toplevel(self)
        popup.title("Help")
        popup.geometry("420x300")
        Label(popup, text='''
        Selective Archiver - File Management Toolkit
        ---------------------------------------
        This program helps you to archive the file types in a selected directory.

        Features:
        - Browse and select a directory to archive.
        - Indicate the specific file extensions for archiving.
        - View archiving status and results.

        How to Use:
        1. Click 'Browse' to select a directory.
        2. Enter file extensions to archive.
        3. Click 'Archive' to start the archiving process.''',
              justify="left").pack(padx=10, pady=10)


class DirOrganiser(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Logo
        base_path = Path(__file__).parent
        logo_path = base_path / 'static' / 'do_logo.png'
        pil_image = Image.open(logo_path)
        self.logo_image = ImageTk.PhotoImage(pil_image)
        self.logo_label = Label(self, image=self.logo_image, bg=self['bg'], borderwidth=0, highlightthickness=0)
        self.logo_label.pack(pady=20)

        # Title text
        self.title_label = ctk.CTkLabel(self, text="Directory Organizer", font=("Arial", 25))
        self.title_label.pack()

        # Browse for Directory
        self.directory_label = ctk.CTkLabel(self, text='Directory:')
        self.directory_label.pack(padx=20, pady=10)
        self.directory_entry = ctk.CTkEntry(self)
        self.directory_entry.pack(padx=20, pady=10)
        self.browse_button = ctk.CTkButton(self, text='Browse', command=self.browse_directory)
        self.browse_button.pack(padx=20, pady=10)

        # Help button
        self.help_button = ctk.CTkButton(self, text='?', width=20, height=20, command=self.show_help_popup)
        self.help_button.place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, 'end')
            self.directory_entry.insert(0, directory)

    def show_help_popup(self):
        popup = Toplevel(self)
        popup.title("Help")
        popup.geometry("800x450")
        Label(popup, text='''Directory Organizer - File Management Tool
        ------------------------------------------
        This tool helps you organize files in a specified directory based on certain criteria.
        
        Features:
        1. Organize by Type:
           Automatically sorts files into folders based on their file type.
           For example, all .jpg files go into a 'Jpg' folder, all .docx files into a 'Docx' folder, etc.
        
        2. Organize by Name:
           Sorts files into a specified folder based on a regex pattern in their names.
           You can define a custom regex pattern and the name of the destination folder.
        
        3. Organize by Date:
           Organizes files into folders based on their modification date.
           Each folder is named with the date of modification, and files are moved accordingly.
        
        How to Use:
        - Choose the directory you want to organize.
        - Select the method of organization:
          1) By Type: Files will be organized into folders named after their file types.
          2) By Name: Provide a regex pattern and a folder name. Files matching the pattern will be moved to the specified folder.
          3) By Date: Files will be organized into folders named by their modification dates.
        - Confirm your choice, and the program will organize the files accordingly.
        
        Note: Ensure you have the necessary permissions to modify the contents of the directory. ''',
              justify="left").pack(padx=10, pady=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()
