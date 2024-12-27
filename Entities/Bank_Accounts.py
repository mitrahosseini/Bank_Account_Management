from random import randint
from Entities.Account import Account


class Bank:
    def __init__(self, AccountList=None):
        if AccountList:
            self.Account_list = AccountList
        else:
            self.Account_list = []
        self.show_Account_list = self.Account_list.copy()

    def search_account(self, term):
        self.show_Account_list.clear()
        for account in self.Account_list:
            if term in account.id or term in account.national_code:
                self.show_Account_list.append(account)

    def creat_random_account_number(self):
        prefix = "01"  # کدبانک
        number = randint(1000, 9999)  # کد شعبه بانک 4 رقم
        check = randint(1000000000, 9999999999)  # شماره حساب مشتری 10 رقم
        AccountNumber = f"{prefix}-{number}-{check}"
        print(AccountNumber)
        return AccountNumber

    def insert_account(self, Nationalcode, firstname, lastname, phonenumber):
        while True:
            AccountNumber = self.creat_random_account_number()  # creat unique account number
            if AccountNumber not in self.Account_list:
                new_account = Account(AccountNumber, Nationalcode, firstname, lastname, phonenumber,
                                      AccountAmount=0)  # creat account
                self.Account_list.append(new_account)
                self.show_Account_list.append(new_account)
                break
        return AccountNumber

    def get_account(self, account_id):
        for account in self.Account_list:
            if account.id == account_id:
             return account
