# import csv
# import random

# print("У вас уже есть аккаунт?")
# authOrRegistr = input("1 - да. 2 - нет.")

# if authOrRegistr == "1":
#     login = input("Логин: ")
#     password = input("Пароль: ")
#     allUsers = []
#     with open("main.csv", "r", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         allUsers = list(reader)
#     for user in allUsers:
#         if user[0] == login:
#             if user[1] == password:
#                 print(user[2], user[3])
#             print("Хотите получить данные карты?")
#             authOrRegistr = input("1 - да. 2 - нет.")
#             if authOrRegistr == "1":
#                 allUsers
#             with open("main.csv", "r", encoding="utf-8") as f:
#                 reader = csv.reader(f)
#                 allUsers = list(reader)
#             for user in allUsers:
#                 if user[0] == login:
#                     if user[1] == password:
#                         print(user[8:-3])

# if authOrRegistr == "2":
#     login = input("Логин: ")
#     password = input("Пароль: ")
#     name = input("Ваше имя: ")
#     surname = input("Ваша фамилия: ")
#     patronymic = input("Ваше отчество: ")
#     seriaPassport = str(input("Ваша серия паспорта: "))
#     nomerPassport = str(input("Ваш номер паспорт: "))

#     dateBirth = str(input("Ваш день рождения: "))
#     BankAccount = "S-" + str(random.randint(100000000, 999999999))
#     nomerBankAccount = str(random.randint(800000000000, 999999999999))
#     dateBankAccount = "07/27"
#     CVCBankAccount = str(random.randint(100, 999))
#     CreditCard = str(random.randint(800000000000, 999999999999))
#     SumCredit = input("Сумма кредита: ")
#     SrokCredita = input("Срок кредита(в месяцах): ")
#     with open("main.csv", "a", encoding="utf-8", newline="\n") as f:
#         newUser = [login,password,name,surname,patronymic,seriaPassport,nomerPassport,dateBirth,BankAccount,nomerBankAccount,dateBankAccount,CVCBankAccount,CreditCard,SumCredit,SrokCredita]
#         writer = csv.writer(f)
#         writer.writerow(newUser)
#         import csv
import random

print("У вас уже есть аккаунт?")
authOrRegistr = input("1 - да. 2 - нет.")

if authOrRegistr == "1":
    login = input("Логин: ")
    password = input("Пароль: ")
    allUsers = []
    with open("main.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        allUsers = list(reader)
    for user in allUsers:
        print(user[1])
        if user[0] == login:
            if user[1] == password:
                yesOrNo = input("Вы хотите получить данные карты? 1 - да. 2 - нет")
                if yesOrNo == "1":
                    chetUser = input("Введите номер счёта")
                    chetBD = user[8]
                    chetBD = chetBD[2:11]
                    if chetUser == chetBD:
                        print(user[9], user[10], user[11], user[12], user[13], user[14])
                    else:
                        print("Такого счёта нету")
                YesOrNo = input("Хотите взять кредит? 1- да. 2 - нет")
                if YesOrNo == "1":
                    mounthCredit = int(input("Введите количество месяцев кредита"))
                    sumCredit = int(input("Введите сумму кредита"))
                    plateMounth = sumCredit*(0.00875+(0.00875/(((1+0.00875)**mounthCredit)-1)))
                    arrPlateMounth = []
                    for i in range(mounthCredit):
                        arrPlateMounth.append(plateMounth)
                    print("Ваш список платежей:")
                    print(arrPlateMounth)

if authOrRegistr == "2":
    login = input("Логин: ")
    password = input("Пароль: ")
    name = input("Ваше имя: ")
    surname = input("Ваша фамилия: ")
    patronymic = input("Ваше отчество: ")
    seriaPassport = str(input("Ваша серия паспорта: "))
    nomerPassport = str(input("Ваш номер паспорт: "))
    dateBirth = str(input("Ваш день рождения: "))
    BankAccount = "S-" + str(random.randint(100000000, 999999999))
    nomerBankAccount = str(random.randint(800000000000, 999999999999))
    dateBankAccount = "07/27"
    CVCBankAccount = str(random.randint(100, 999))
    CreditCard = str(random.randint(800000000000, 999999999999))
    SumCredit = input("Сумма кредита: ")
    SrokCredita = input("Срок кредита(в месяцах): ")
    with open("main.csv", "a", encoding="utf-8", newline="\n") as f:
        newUser = [login,password,name,surname,patronymic,seriaPassport,nomerPassport,dateBirth,BankAccount,nomerBankAccount,dateBankAccount,CVCBankAccount,CreditCard,SumCredit,SrokCredita]
        writer = csv.writer(f)
        writer.writerow(newUser)