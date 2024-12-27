import re
from tkinter import Tk, Entry, messagebox, Label, Button


class Account:
    def __init__(self, AccountNumber, Nationalcode, firstname, lastname, PhoneNumber, AccountAmount=0):
        self.id = AccountNumber
        self.national_code = Nationalcode
        self.first_name = firstname
        self.last_name = lastname
        self.phone_number = PhoneNumber
        # self.balance=AccountBalance
        self.amount = AccountAmount

    def Update(self, AccountNumber, new_Nationalcode, new_firstname, new_lastname, new_PhoneNumber, AccountAmount):
        self.id = AccountNumber
        self.national_code = new_Nationalcode
        self.first_name = new_firstname
        self.last_name = new_lastname
        self.phone_number = new_PhoneNumber
        self.amount = AccountAmount

    def Increase(self, IncreaseAmount):
        try:
            increase_amount = int(IncreaseAmount)
        except ValueError:
            messagebox.showerror(title="Invalid Data", message="Invalid Data For Increase Amount")

        self.amount += increase_amount
        return True


    def Reduction(self, ReductionAmount):  # برداشت وجه

        try:
            reduction_amount = int(ReductionAmount)
            if reduction_amount>self.amount:
                 messagebox.showerror(title="Insufficient Balance",message="The Account Balance Is Insufficient")
                 return False
            else:
                  self.amount -= reduction_amount
                  return  True

        except ValueError:
            messagebox.showerror(title="Invalid Data", message="Invalid Data For Reduction Amount")
            return False
        except UnboundLocalError:
            messagebox.showerror(title="Invalid Data", message="Invalid Data For Reduction Amount")
            return False
        except :
            messagebox.showerror(title="Invalid Data", message="Invalid Data For Reduction Amount")
            return False


def validate_iranian_national_code(code):
    code_len = len(code)
    if code_len > 10 or code_len < 8:
        return False

    if len(set(code)) == 1:
        return False

    if len(code) < 10:
        code = code.zfill(10)

    factors = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    checksum = sum(int(code[i]) * factors[i] for i in range(len(code) - 1))
    remainder = checksum % 11
    last_digit = int(code[-1])

    if remainder < 2:
        return remainder == last_digit
    else:
        return 11 - remainder == last_digit


def is_iranian_mobile_number(number):
    pattern = "^09\d{9}$"
    if re.match(pattern, number):
        return True
    return False
