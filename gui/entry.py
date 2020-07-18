import tkinter as tk
from tkinter import messagebox
import json, os, pyperclip
from crypto import KeyGenerator

class App(tk.Frame):
    jsonFile = os.path.join(os.path.dirname(__file__), "dict.json")
    
    #styling variables
    green_bg = "#62AAA8"
    pink_bg = "#FEB6B8"

    # creates jsonfile in same directory if it doesn't exist
    if not os.path.exists(jsonFile):
        with open(jsonFile, "w+") as fl:
            fl.write("{}")
            fl.close()

    #stores json contents in data variable
    with open(jsonFile, "r") as fl:
        data = json.load(fl)
        fl.close()
    
    # inherits the init from the Frame Class
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master # selects root to unpack into 
        self.grid() # unpack item in root

        # main frame 
        self.main_frame = tk.LabelFrame(self.master, text = "Enter existing user or create new one", bg = self.green_bg) 
        self.main_frame.grid(row = 0, column = 0, sticky = "nesw")

        # ask for user credentials 
        self.username_label = tk.Label(self.main_frame, text="Enter username: ", bg = self.green_bg)
        self.username_label.grid(row = 0, column = 0)

        self.password_label = tk.Label(self.main_frame, text="Enter Password: ", bg = self.green_bg)
        self.password_label.grid(row = 1, column = 0)

        self.username_field = tk.Entry(self.main_frame, width = 30, takefocus = 1)
        self.username_field.grid(row=0, column = 1, padx = 5)
        self.username_field.focus()

        self.password_field = tk.Entry(self.main_frame, width = 30)
        self.password_field.grid(row = 1, column = 1, padx = 5)

        self.button_frame = tk.Frame(self.main_frame, bg = self.green_bg) 
        self.button_frame.grid(row = 3, column = 0, sticky = "nesw")
        self.button_frame.rowconfigure(3, weight=1)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        check_button = tk.Button(self.button_frame,text = "Create/Log In", command = self.user_check, bg= self.pink_bg)
        check_button.grid(row = 0, column = 0, sticky="nesw")

        quit_button = tk.Button(self.button_frame, text="QUIT", command=self.master.destroy, bg= self.pink_bg)
        quit_button.grid(row = 0, column = 1, sticky="nesw")
    
    # checks if the username and password match the ones set for the program 
    def user_check(self):
        username = self.username_field.get()
        password = self.password_field.get()
        if username != None and password != None:
            if "username" not in self.data:
                self.data["username"] = username
                self.data["password"] = KeyGenerator(password = password).encrypt_key()
                with open(self.jsonFile, "w") as write_file:
                    json.dump(self.data, write_file)
                    write_file.close()
                self.choice_widget()
            elif self.data["username"] != username or KeyGenerator(password = self.data["password"]).decrypt_key() != password:
                tk.messagebox.showinfo("Error", "Wrong username and/or password")
                self.master.destroy()
            else:
                self.choice_widget()

    # main widget to give user access to CREATE NEW ACCOUNT PASSWORD or RETRIEVE options
    def choice_widget(self):
        self.main_frame.destroy()
        # button frame
        self.choice_frame = tk.LabelFrame(self.master, text="Welcome back," + self.data["username"]) 
        self.choice_frame.grid(row = 0, padx = 10, pady = 10)

        #center button
        self.new_button = tk.Button(self.choice_frame, text="""Enter new account/password combination
        OR
        Update existing password""", bg = self.green_bg, command = self.create_new_account)
        self.new_button.grid(row = 0, column=0, sticky="nesw", padx = 20, pady = 20)

        self.retrieve_button = tk.Button(self.choice_frame, text="Retrieve password", bg = self.green_bg, command = self.retrieve_account )
        self.retrieve_button.grid(row = 0, column=0, sticky="nesw", padx = 20, pady = 20)

        # exit button 
        quit_button = tk.Button(self.choice_frame, text="QUIT", command=self.master.destroy, bg= self.pink_bg)
        quit_button.grid(row = 1, column = 0, sticky="nesw", padx = 20, pady = 20)
    
    def create_new_account(self):
        self.choice_frame.destroy()
        self.form_frame = tk.Frame(self.master, bg = self.green_bg) # creates a frame to handle labels and entries related to the form
        self.form_frame.grid(row = 0)

        # form field: labels and associated entry widgets
        new_account_label = tk.Label(self.form_frame, text="Account Name: ", bg = self.green_bg)
        new_account_label.grid(row = 0, column = 0)
        self.new_account_field = tk.Entry(self.form_frame, width = 30)
        self.new_account_field.grid(row=0, column = 1, padx = 5)

        new_password_label = tk.Label(self.form_frame, text="Password: ", bg = self.green_bg)
        new_password_label.grid(row = 1, column = 0)
        self.new_password_field = tk.Entry(self.form_frame, width = 30)
        self.new_password_field.grid(row = 1, column = 1, padx = 5)

        # button frame
        button_frame = tk.Frame(self.form_frame, bg = self.green_bg) # creates a frame to handle labels and entries related to the form
        button_frame.grid(row = 2)

        #enter button
        enter_new = tk.Button(button_frame, text="Enter/Update", command = self.set_account, bg = self.pink_bg)
        enter_new.grid(row = 0, column=1, sticky = "nesw")

        # exit button 
        quit_button = tk.Button(button_frame, text="QUIT", command=self.master.destroy, bg = self.pink_bg)
        quit_button.grid(row = 0, column = 2, sticky = "nesw")

        # get the account and store it in json file
    def set_account(self):
        if self.new_account_field.get() != "" and self.new_password_field.get() != "":
            encrypt_password = KeyGenerator(password = self.new_password_field.get()).encrypt_key() # creates a crypted password to store into the json file
            self.data[self.new_account_field.get()] = encrypt_password
            with open(self.jsonFile, "w") as write_file:
                json.dump(self.data, write_file)
                print(encrypt_password)
                write_file.close()
        else:
            tk.messagebox.showinfo("Error", "Please enter a valid account and password")

    def retrieve_account(self):
        #get_account frame
        self.choice_frame.destroy()
        self.form_frame = tk.Frame(self.master, bg = self.green_bg) # creates a frame to handle labels and entries related to the form
        self.form_frame.grid(row=0)

        #get_account labels and entries
        account_label = tk.Label(self.form_frame, text="""Enter the account name 
       to retrieve the password.""", bg = self.green_bg)
        account_label.grid(row = 1, column = 0)
        account_field = tk.Entry(self.form_frame, width = 30)
        account_field.grid(row=1, column = 1, padx = 5)

        # account_to_search = name_of_account_field.get()
        def search_account():
            account_name = account_field.get()
        # IF data[key] exists:
            if account_name in self.data:
                retrieved_password = KeyGenerator(password=self.data[account_name]).decrypt_key()
                pyperclip.copy(retrieved_password)
                tk.messagebox.showinfo("Success!", "Password copied to clipboard")
            else:
                tk.messagebox.showinfo("Error", "No account in database")
        
        button_frame = tk.Frame(self.form_frame, bg = self.green_bg) # creates a frame to handle labels and entries related to the form
        button_frame.grid(row = 2)

        search_button = tk.Button(button_frame, text= "Search", command = search_account, bg = self.pink_bg)
        search_button.grid(row = 2, column = 0, sticky = "nesw")

        quit_button = tk.Button(button_frame,text="QUIT", command=self.master.destroy, bg = self.pink_bg)
        quit_button.grid(row = 2, column = 2, sticky = "nesw")



if __name__ == "__main__":
    root = tk.Tk()  
    app = App(master=root)
    app.mainloop()