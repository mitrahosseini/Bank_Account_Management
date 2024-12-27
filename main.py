from tkinter import Tk, Entry, messagebox, Label, Button
from tkinter.ttk import Treeview
from Entities.Bank_Accounts import Bank
from Entities.Account import Account
from Login_Form import creat_login_form
from working_database import load_data
from working_database import replace_data
from Entities.Account import validate_iranian_national_code
from Entities.Account import is_iranian_mobile_number

creat_login_form()
AccountList = load_data()
bank = Bank(AccountList)

print(bank.Account_list)
window = Tk()
window.title("Bank Account Aplication")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_columnconfigure(5, weight=1)
window.grid_rowconfigure(2, weight=1)


def show_account_form(account=None):
    account_form = Tk()
    if account:
        account_form.title("Update Account")
    else:
        account_form.title("New Account")
    first_name_lable = Label(account_form, text="First Name")
    first_name_lable.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    first_name_entry = Entry(account_form, width=50)
    first_name_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="w")

    last_name_lable = Label(account_form, text="Last Name")
    last_name_lable.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="e")

    last_name_entry = Entry(account_form, width=50)
    last_name_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    national_code_lable = Label(account_form, text="National Code")
    national_code_lable.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="e")

    national_code_entry = Entry(account_form, width=50)
    national_code_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    phone_number_lable = Label(account_form, text="Phone Number")
    phone_number_lable.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="e")

    phone_number_entry = Entry(account_form, width=50)
    phone_number_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    account_number_lable = Label(account_form, text="Account Number")
    account_number_lable.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="e")

    account_number_entry = Entry(account_form, width=50)
    account_number_entry.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    if account:
        first_name_entry.insert(0,account.first_name)
        last_name_entry.insert(0,account.last_name)
        national_code_entry.insert(0,account.national_code)
        phone_number_entry.insert(0,account.phone_number)
        account_number_entry.insert(0,account.id)
        account_number_entry.config(state="readonly")
        national_code_entry.config(state="readonly")
    def submit_clicked():

        def validation_data_entry():
            firstname = first_name_entry.get()
            if not firstname.isalpha():
                messagebox.showerror(title="Invalid Data", message=" !!! Invalid Data For First Name !!! ")
                first_name_entry.delete(0, "end")
            lastname = last_name_entry.get()
            if not lastname.isalpha():
                messagebox.showerror(title="Invalid Data", message=" !!! Invalid Data For Last Name !!! ")
                last_name_entry.delete(0, "end")
            Nationalcode = national_code_entry.get()
            if not (validate_iranian_national_code(Nationalcode)):
                messagebox.showerror(title="Invalid Data", message=" !!! Invalid Data For National Code !!! ")
                national_code_entry.delete(0, "end")
            phonenumber = phone_number_entry.get()
            if not is_iranian_mobile_number(phonenumber):
                messagebox.showerror(title="Invalid Data", message=" !!! Invalid Data For Phone Number !!! ")
                phone_number_entry.delete(0, "end")
            if firstname.isalpha() and lastname.isalpha() and validate_iranian_national_code(
                    Nationalcode) and is_iranian_mobile_number(phonenumber):
                return True
            else:
                return False

        validate_data = validation_data_entry()
        if validate_data == True:
            # submit_button.config(state="normal")
            firstname = first_name_entry.get()
            lastname = last_name_entry.get()
            Nationalcode = national_code_entry.get()
            phonenumber = phone_number_entry.get()
            AccountNumber=account_number_entry.get()

            if account:
                account.Update(AccountNumber,Nationalcode,firstname,lastname,phonenumber,AccountAmount=0)
                bank.show_Account_list=bank.Account_list.copy()
            else:
                AccountNumber = bank.insert_account(Nationalcode, firstname, lastname, phonenumber)
                account_number_entry.config(state="normal")
                account_number_entry.delete(0, "end")
                account_number_entry.insert(0, AccountNumber)
                account_number_entry.config(state="readonly")
                submit_button.config(state="disabled")

            load_data_treeview()
            replace_data(bank.Account_list)
            # account_form.destroy()


    submit_button = Button(account_form, text="Submit", command=submit_clicked)
    submit_button.grid(row=5, column=1, padx=10, pady=(0, 10), sticky="w")


    account_form.mainloop()


new_account_button = Button(window, text="New Account", command=show_account_form)
new_account_button.grid(row=0, column=1, padx=10, pady=10)

def update_button_clicked():
    update_id=accounts_treeview.selection()[0]
    updete_contact=bank.get_account(update_id)
    show_account_form(updete_contact)

update_account_button = Button(window, text="Update Account",command=update_button_clicked)
update_account_button.grid(row=0, column=2, padx=(0, 10), pady=10)

def increase_reduction_amount_form(increase=None,reduction=None):
    account_form = Tk()
    if increase:
        account_form.title("Account Increase Amount")
        account=increase
    elif reduction:
        account_form.title("Account Reduction Amount")
        account=reduction

    account_number_lable = Label(account_form, text="Account Number")
    account_number_lable.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    account_number_entry = Entry(account_form, width=50)
    account_number_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="w")

    account_amount_lable = Label(account_form, text="Account Amount")
    account_amount_lable.grid(row=1, column=0, padx=10, pady=(0,10), sticky="e")

    account_amount_entry = Entry(account_form, width=50)
    account_amount_entry.grid(row=1, column=1, padx=(0, 10), pady=(0,10), sticky="w")

    if increase:
        account_increase_amount_lable = Label(account_form, text="Increase Amount")
        account_increase_amount_lable.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="e")

        account_increase_amount_entry = Entry(account_form, width=50)
        account_increase_amount_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="w")


    elif reduction:
        account_reduction_amount_lable = Label(account_form, text="Reduction Amount")
        account_reduction_amount_lable.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="e")

        account_reduction_amount_entry = Entry(account_form, width=50)
        account_reduction_amount_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="w")

    account_number_entry.delete(0,"end")
    account_number_entry.insert(0,account.id)
    account_number_entry.config(state="readonly")

    account_amount_entry.delete(0,"end")
    account_amount_entry.insert(0,account.amount)
    account_amount_entry.config(state="readonly")

    def submit_button_clicked():
        if increase:
            IncreaseAmount=account_increase_amount_entry.get()
            vlidate_operation=account.Increase(IncreaseAmount)

        elif reduction:
            ReductionAmount=account_reduction_amount_entry.get()
            vlidate_operation=account.Reduction(ReductionAmount)

        if vlidate_operation:

            bank.show_Account_list=bank.Account_list.copy()
            load_data_treeview()
            replace_data( bank.show_Account_list)
            submit_button.config(state="disabled")
            account_form.destroy()

        else:
            account_form.destroy()


    submit_button = Button(account_form, text="Submit",command=submit_button_clicked)
    submit_button.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="w")

    account_form.mainloop()


def account_increase_amount_button_clicked():
    account_increase_amount_id=accounts_treeview.selection()[0]
    account_increase_amount=bank.get_account(account_increase_amount_id)
    increase_reduction_amount_form(increase=account_increase_amount)


account_increase_amount_button = Button(window, text="Account Increase Amount",command=account_increase_amount_button_clicked)
account_increase_amount_button.grid(row=0, column=3, padx=(0, 10), pady=10)

def account_reduction_amount_button_clicked():
    account_reduction_amount_id=accounts_treeview.selection()[0]
    account_reduction_amount=bank.get_account(account_reduction_amount_id)
    increase_reduction_amount_form(reduction=account_reduction_amount)


account_reduction_amount_button = Button(window, text="Account Reduction Amount",command=account_reduction_amount_button_clicked)
account_reduction_amount_button.grid(row=0, column=4, padx=(0, 10), pady=10)

search_entry = Entry(window, width=50)
search_entry.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky="ew")

def search_button_clicked():
    term=search_entry.get()
    bank.search_account(term)
    load_data_treeview()

search_button = Button(window, text="Search",command=search_button_clicked)
search_button.grid(row=1, column=5, padx=10, pady=10, sticky="w")

accounts_treeview = Treeview(window, columns=(
    "Account Number", "Account Amount", "National Code", "First Name", "Last Name", "Phone Number"))
accounts_treeview.grid(row=2, column=0, columnspan=6, padx=10, pady=10, sticky="ewns")
accounts_treeview.heading("#0", text="No")
accounts_treeview.heading("#1", text="Account Number")
accounts_treeview.heading("#2", text="Account Amount")
accounts_treeview.heading("#3", text="National Code")
accounts_treeview.heading("#4", text="First Name")
accounts_treeview.heading("#5", text="Last Name")
accounts_treeview.heading("#6", text="Phone Number")
accounts_treeview.column("#0", width=50)
row_list = []


def load_data_treeview():
    for row in row_list:
        accounts_treeview.delete(row)
    row_list.clear()
    row_number = 1
    account_data = bank.show_Account_list
    for account in account_data:
        row = accounts_treeview.insert("", "end", iid=account.id, text=str(row_number), values=(
            account.id, account.amount, account.national_code, account.first_name, account.last_name,
            account.phone_number))
        row_list.append(row)  # list of treeview data
        row_number += 1

new_account_button.config(state="normal")
update_account_button.config(state="disabled")
account_increase_amount_button.config(state="disabled")
account_reduction_amount_button.config(state="disabled")

def manage_button(event):

   select_count=len(accounts_treeview.selection())

   if select_count==1:
       new_account_button.config(state="normal")
       update_account_button.config(state="normal")
       account_increase_amount_button.config(state="normal")
       account_reduction_amount_button.config(state="normal")
   elif select_count>1:
       new_account_button.config(state="normal")
       update_account_button.config(state="disabled")
       account_increase_amount_button.config(state="disabled")
       account_reduction_amount_button.config(state="disabled")
   else:
       new_account_button.config(state="normal")
       update_account_button.config(state="disabled")
       account_increase_amount_button.config(state="disabled")
       account_reduction_amount_button.config(state="disabled")



accounts_treeview.bind("<<TreeviewSelect>>",manage_button)

load_data_treeview()
window.mainloop()
