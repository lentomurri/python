# the program will organise a working directory, moving all files with a certain extension to another directory.
# if the new directory doesn't exist, it will be created.
# there's an option to copy or transfer the files
# at operation done, the number of files copied or transferred will be displayed.

#usr/bin/python3

import tkinter as tk
import shutil, os
from send2trash import send2trash
from tkinter import messagebox
from pathlib import Path

# function to create structure
class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__()
        self.master = master
        self.create_frame()

    def create_frame(self):
        main_frame = tk.Frame(self.master, bg = "#C785AE")
        main_frame.grid(row = 0, column = 0)

        explanation_label = tk.Label(main_frame, text="""Enter the directory
        you want to move files from, the destination directory 
        and a single file extension (zip, pdf, etc)""", bg= "white")
        explanation_label.grid(row = 0, column = 0, columnspan = 2)

        # starting directory
        starting_label = tk.Label(main_frame, text="""Enter the starting directory 
        absolute path""", bg = "white", width = 30)
        starting_label.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        self.starting_directory = tk.Entry(main_frame, width=60)
        self.starting_directory.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.starting_directory.focus()

        # destination directory
        destination_label = tk.Label(main_frame, text="""Enter the destination directory 
        absolute path""", bg = "white", width = 30)
        destination_label.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        self.destination_directory = tk.Entry(main_frame, width=60)
        self.destination_directory.grid(row = 2, column = 1, padx = 5, pady = 5)

        # file extension
        file_label = tk.Label(main_frame, text="""Enter the file extension""", bg = "white", width = 30)
        file_label.grid(row = 3, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        self.file_extension = tk.Entry(main_frame, width=60)
        self.file_extension.grid(row = 3, column = 1, padx = 5, pady = 5, ipadx = 5, ipady = 5)

        # button_frame
        button_frame = tk.Frame(self.master, bg = "#C785AE")
        button_frame.grid(row = 1)

        # cancel or copy button
        self.copy_or_cancel = tk.IntVar()
        copy = tk.Radiobutton(button_frame, text = "Copy Files", variable = self.copy_or_cancel, value = 1)
        copy.select()
        copy.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5)
 
        transfer = tk.Radiobutton(button_frame, text = "Transfer Files", variable = self.copy_or_cancel, value = 2)
        transfer.grid(row = 0, column = 1,padx = 5, pady = 5, ipadx = 5, ipady = 5)
        

        # submit and quit button
        submit_button = tk.Button(button_frame, text = "Submit", bg = "#C785AE", command = self.set_directories)
        submit_button.grid(row = 1, column = 0, sticky = "nesw")
        quit_button = tk.Button(button_frame, text = "Quit", bg= "#FFDAAA", command = self.master.destroy)
        quit_button.grid(row = 1, column = 1, sticky = "nesw")

        # organise files to return for organise_files function

    def set_directories(self):
        starting = self.starting_directory.get()
        destination = self.destination_directory.get()
          
        # open starting directory if it exists
        self.starting = starting.replace('"', '') # removes quotes if user pass in string path
        if not os.path.exists(self.starting):
            tk.messagebox.showinfo("Error", "Please enter a valid, absolute path for the starting directory")
        os.chdir(self.starting)
        
        self.destination = destination.replace('"', '')
        if not os.path.exists(self.destination):
            try:
                os.mkdir(self.destination)
                tk.messagebox.showinfo("Success", "Destination directory created!")
            except:
                tk.messagebox.showinfo("Error", "Please enter a valid, absolute path for destination")
        
        self.organise_files()
    
    def organise_files(self):
        file_extension = self.file_extension.get()
        copy_or_cancel = self.copy_or_cancel.get()

        listfile = os.listdir(self.starting)

        count = 0
        for current_file in listfile:
            if current_file.endswith(file_extension):
                count +=1
                shutil.copy(Path(current_file).absolute(), self.destination)
                if copy_or_cancel == 2:
                    send2trash(current_file)
        if copy_or_cancel == 1:
            tk.messagebox.showinfo("Success!", f"{count} files have been copied!")
        else:
            tk.messagebox.showinfo("Success!", f"{count} files have been transferred!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()