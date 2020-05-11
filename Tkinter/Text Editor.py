# Python's version used: 3.8.2 64 bit
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

# These  lines are only to create a correct executable file with Pyinstaller
# by importing correctly the icon file.
# To do this go in the terminal in the folder of this file and type
# For Windows:
# pyinstaller --onefile --noconsole --add-data="Text Editor.ico;." --icon="Text Editor.ico" "Text Editor.py"
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "Text Editor.ico")
else:
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        pass
    finally:
        icon_path = "Text Editor.ico"


# Defining the menu bar to use later in the window
class Menubar:
    def __init__(self, parent):
        # Choosing the font and size for the menu bar
        font_specs = ("Calibri", 14)
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        # Defining the file section in the menu bar
        # Tearoff is to deny the section file to move from its position
        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        # Add option New File in the section file
        file_dropdown.add_command(label="New File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        # Add a separator line
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Open File...",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save",
                                  accelerator="Ctrl+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Save As...",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=parent.master.destroy)
        
        # Defining the about section in the Menu Bar
        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About",
                                   command=self.show_about_message)
        
        # Setting the names of the sections
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="About", menu=about_dropdown)

    def show_about_message(self):
        box_title = "About Text_Editor"
        box_message = "A simple Text Editor created with Python and Tkinter."
        messagebox.showinfo(box_title, box_message)

    def show_release_notes(self):
        box_title = "Release notes"
        box_message = "Version 0.1"
        messagebox.showinfo(box_title, box_message)


# Defining the Status Bar
class Statusbar:
    def __init__(self, parent):
        font_specs = ("Helvetica", 12)
        self.status = tk.StringVar()
        self.status.set("Text_Editor 0.1 - Status Bar")

        label = tk.Label(parent.textarea,
                         textvariable=self.status,
                         fg="black",
                         bg="lightgrey",
                         anchor='sw',
                         font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, x):
        if x == 1:
            self.status.set("Your file was saved")
        elif x == 2:
            self.status.set("File opened correctly")
        elif x == 3:
            self.status.set("Unsupported File Extension")
        elif x == 4:
            self.status.set("New blank file")
        else:
            self.status.set("Text_Editor 0.1 - Status Bar")


class Text_editor:
    def __init__(self, master):
        # Title of the window
        master.title("Untitled - Text_Editor")
        # Make the default window fit the screen's size
        master.state('zoomed')
        master.geometry("1200x700")
        # Icon of the window
        try:
            # Windows
            master.iconbitmap(icon_path)
        except:
            # Linux
            pass

        # Choosing the font and its size
        font_specs = ("Helvetica", 18)

        self.master = master

        # Creating the area for the text in the window
        # cursor is mandatory with the gray background
        self.textarea = tk.Text(master,
                                font=font_specs,
                                cursor="arrow",
                                background="gray")
        # Creating the scrollbar in the window
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        # The area for writing will fill all the window
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # The scrollbar will be put at the right of the window
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Menubar
        self.menubar = Menubar(self)

        # Status Bar
        self.statusbar = Statusbar(self)

        # Keyboard Shortcuts
        self.bind_shortcuts()

    # set window title when a new file is opened
    # to use it later as function
    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - Text_Editor")
        else:
            self.master.title("Untitled - Text_Editor")

    # new file option
    # *args is needed for shortcuts
    def new_file(self, *args):
        # make the window blank
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()
        self.statusbar.update_status(4)

    # open file option
    def open_file(self, *args):
        # open a file
        try:
            self.filename = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"),
                           ("Python Script", "*.py*"),
                           ("Markdown Text", "*.md*"), ("JavaScript", "*.js"),
                           ("Document HTML", "*.html*"),
                           ("Document CSS", "*.css*")])
            if self.filename:
                # make the window blank
                self.textarea.delete(1.0, tk.END)
                with open(self.filename, "r") as f:
                    self.textarea.insert(1.0, f.read())
                # set new window title equals to the filename
                self.set_window_title(self.filename)
                self.statusbar.update_status(2)

        except:
            self.statusbar.update_status(3)

    # save option
    def save(self, *args):
        # if file have already a name do this
        try:
            if self.filename:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(1)
            else:
                self.save_as()
        # if file doesn't have a name yet do this
        except:
            self.save_as()

    # save as option
    def save_as(self, *args):
        try:
            # save new file
            new_file = filedialog.asksaveasfilename(
                # default name of the new file to save
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"),
                           ("Python Script", "*.py*"),
                           ("Markdown Text", "*.md*"), ("JavaScript", "*.js"),
                           ("Document HTML", "*.html*"),
                           ("Document CSS", "*.css*")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(1)
        except Exception as e:
            print(e)

    # Defining keyboard shortcuts
    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-N>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-O>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save)
        self.textarea.bind('<Control-Shift-s>', self.save_as)
        self.textarea.bind('<Control-Shift-S>', self.save_as)
        self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == "__main__":
    # Creating window
    master = tk.Tk()
    pt = Text_editor(master)
    master.mainloop()
