from Entities.Account import Account


def load_data():
    account_list = []
    with open("Data\\Accounts_Database.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line_splited = line.split(",")
            account = Account(line_splited[0], line_splited[1], line_splited[2], line_splited[3], line_splited[4],int(line_splited[5]))
            account_list.append(account)
    return account_list


def replace_data(account_list):
    data_text = ""
    last_account_item = account_list[-1]
    for account in account_list:
      data_text += f"{account.id},{account.national_code},{account.first_name},{account.last_name},{account.phone_number},{account.amount}"
      if account != last_account_item:
        data_text += "\n"

    with open("Data\\Accounts_Database.txt", mode="w") as file:
        file.write(data_text)
