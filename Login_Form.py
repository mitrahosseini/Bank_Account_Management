from tkinter import Tk, Entry, messagebox, Label, Button


def creat_login_form():
    login_form = Tk()
    login_form.title("Login Form ")
    login_form.grid_columnconfigure(1, weight=1)

    username_login_lable = Label(login_form, text="UserName: ")
    username_login_lable.grid(row=0, column=0, padx=10, pady=10)
    username_login_entry = Entry(login_form)
    username_login_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="we")

    password_login_lable = Label(login_form, text="Password: ")
    password_login_lable.grid(row=1, column=0, padx=10, pady=10)
    password_login_entry = Entry(login_form,show="*")
    password_login_entry.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="we")
    login_failed_counter = {"count":1}

    def search_user_pass_database(username=None, password= None):
      try:
        with open("Data\\User_Pass_Database.txt") as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace("\n", "")
                line_splited = line.split(",")
                if username == line_splited[0] and password == line_splited[1]:
                    return True
      except FileNotFoundError:
          messagebox.showerror("Error","Database File Not Found.")
          return False

    def login_button_clicked():
            username = username_login_entry.get()
            password = password_login_entry.get()
            if search_user_pass_database(username, password):
                messagebox.showinfo(title="Login", message="Login successfull")
                login_form.destroy()

            else:
                login_failed_counter["count"] += 1
                if login_failed_counter["count"] <= 3:
                  messagebox.showerror(title="Login Failed", message="Invalid Username or Password")
                  username_login_entry.delete(0, "end")
                  password_login_entry.delete(0, "end")
                else:
                    messagebox.showerror(title="Login locked!",
                                         message="Input Invalid Username or Password More Than 3 Times.")
                    login_form.destroy()

    login_button = Button(login_form, text="Login", command=login_button_clicked)
    login_button.grid(row=2, column=1, pady=(0, 10), sticky="w")
    login_form.mainloop()
