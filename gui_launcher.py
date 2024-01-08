# Launcher for GUI

import threading
import customtkinter as ctk
import tkinter.messagebox
from tkinter import Label, filedialog, Toplevel
from PIL import Image, ImageTk
from pathlib import Path

from bulkArchiver import bulk_archiver
from selectiveArchiver import selective_archiver
from directoryOrganiser import DirectoryOrganiser
from fileEncryptor import FileEncryptor


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

        # Initialize Encryptor
        self.encryptor = Encryptor(self.main_frame)
        self.show_encryptor_button = ctk.CTkButton(self.sidebar_frame,
                                                   text='File Encryptor', command=self.show_encryptor)
        self.show_encryptor_button.pack(padx=10, pady=3)

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

    # Clear the main frame and display Encryptor
    def show_encryptor(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.encryptor = Encryptor(self.main_frame)
        self.encryptor.pack(fill='both', expand=True)


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

        # Input for extensions to archive
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

        self.organiser = DirectoryOrganiser('')

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

        # Organize method choice dropdown
        self.method_label = ctk.CTkLabel(self, text='Choose method:')
        self.method_label.pack(padx=20, pady=10)

        self.method_options = ["Type", "Date"]
        self.method_dropdown = ctk.CTkComboBox(self, values=self.method_options)
        self.method_dropdown.set("Select Method")
        self.method_dropdown.pack(padx=20, pady=10)

        # Organize button
        self.organize_button = ctk.CTkButton(self, text='Organize', command=self.organise_files)
        self.organize_button.pack(padx=20, pady=10)

        # Help button
        self.help_button = ctk.CTkButton(self, text='?', width=20, height=20, command=self.show_help_popup)
        self.help_button.place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, 'end')
            self.directory_entry.insert(0, directory)

    def organise_files(self):
        directory = self.directory_entry.get()
        method = self.method_dropdown.get()

        self.organiser = DirectoryOrganiser(directory)

        if method == 'Type':
            self.organiser.organise_by_type()
        elif method == 'Date':
            self.organiser.organise_by_date()
        else:
            print('Invalid or no method selected.')

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
        
        2. Organize by Date:
           Organizes files into folders based on their modification date.
           Each folder is named with the date of modification, and files are moved accordingly.
        
        How to Use:
        - Choose the directory you want to organize.
        - Select the method of organization:
          1) By Type: Files will be organized into folders named after their file types.
          2) By Date: Files will be organized into folders named by their modification dates.
        - Confirm your choice, and the program will organize the files accordingly.
        
        Note: Ensure you have the necessary permissions to modify the contents of the directory. ''',
              justify="left").pack(padx=10, pady=10)


class Encryptor(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.encryptor = FileEncryptor()

        # Logo
        base_path = Path(__file__).parent
        logo_path = base_path / 'static' / 'en_logo.png'
        pil_image = Image.open(logo_path)
        self.logo_image = ImageTk.PhotoImage(pil_image)
        self.logo_label = Label(self, image=self.logo_image, bg=self['bg'], borderwidth=0, highlightthickness=0)
        self.logo_label.pack(pady=20)

        # Title text
        self.title_label = ctk.CTkLabel(self, text='File Encryptor', font=("Arial", 25))
        self.title_label.pack()

        # File selection
        self.file_label = ctk.CTkLabel(self, text='File:')
        self.file_label.pack(padx=20, pady=10)
        self.file_entry = ctk.CTkEntry(self)
        self.file_entry.pack(padx=20, pady=10)
        self.browse_button = ctk.CTkButton(self, text='Browse', command=self.browse_file)
        self.browse_button.pack(padx=20, pady=10)

        # Key input
        self.key_label = ctk.CTkLabel(self, text='Encryption Key:')
        self.key_label.pack(padx=20, pady=10)
        self.key_entry = ctk.CTkEntry(self)
        self.key_entry.pack(padx=20, pady=10)
        self.generate_key_button = ctk.CTkButton(self, text='Generate Key', command=self.generate_key)
        self.generate_key_button.pack(padx=20, pady=10)

        # Encrypt/Decrypt buttons
        self.encrypt_button = ctk.CTkButton(self, text='Encrypt', command=self.encrypt_file)
        self.encrypt_button.pack(padx=20, pady=10)
        self.decrypt_button = ctk.CTkButton(self, text='Decrypt', command=self.decrypt_file)
        self.decrypt_button.pack(padx=20, pady=10)

        # Help button
        self.help_button = ctk.CTkButton(self, text='?', width=20, height=20, command=self.show_help_popup)
        self.help_button.place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_entry.delete(0, 'end')
            self.file_entry.insert(0, file_path)

    def generate_key(self):
        key = FileEncryptor.generate_key()
        self.key_entry.delete(0, 'end')
        self.key_entry.insert(0, key.decode())
        tkinter.messagebox.showinfo("Key Generated", "A new encryption key has been generated. Keep it safe!")

    def encrypt_file(self):
        file_path = self.file_entry.get()
        key = self.key_entry.get().encode()
        self.encryptor = FileEncryptor(key)
        self.encryptor.encrypt_file(file_path)
        tkinter.messagebox.showinfo("Encryption", f"File {file_path} encrypted successfully.")

    def decrypt_file(self):
        file_path = self.file_entry.get()
        key = self.key_entry.get().encode()
        self.encryptor = FileEncryptor(key)
        self.encryptor.decrypt_file(file_path)
        tkinter.messagebox.showinfo("Decryption", f"File {file_path} decrypted successfully.")

    def show_help_popup(self):
        popup = Toplevel(self)
        popup.title("Help")
        popup.geometry("550x300")
        Label(popup, text='''File Encryptor - Secure Your Files
        ----------------------------------
        This tool provides encryption and decryption functionalities to secure your sensitive files.
        
        Features:
        1. Encrypt: Secure a file with robust encryption.
        2. Decrypt: Restore the original content of an encrypted file.
        
        Usage:
        - Choose to encrypt or decrypt a file.
        - Provide the full path of the file.
        - Enter an encryption key or generate a new one.
        - Execute the chosen action to secure or access your file.
        
        Note: Keep your encryption key safe. Losing it means you cannot decrypt your files.''',
              justify="left").pack(padx=10, pady=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()
