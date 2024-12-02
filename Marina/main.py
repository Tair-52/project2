import csv
# Авторизация
print("У вас есть аккаунт?")
authorRegistr = input ("1 - да. 2 - нет.")
if authorRegistr == "1":
    login = input("Логин:")
    password = input("Пароль:")
    allUsers = []
    with open ("main.csv", "r",encoding = "utf-8") as f:
        reader = csv.reader(f)
        allUsers = list(reader)
    for user in allUsers:
           if user [0] == login:
                if user[1] == password :
                     print(user[2],"welcome!")
                     if user[-1] == "admin":
                             print(allUsers)    
                     else:
                             print (user[2],user[3],user[4])   
                else:
                     print("Пользователь не найден")     
# Регистрация
if authorRegistr == "2":
     login = input ("Логин - ")
     password = input ("Пароль - ")
     name = input("Ваше имя - ")
     dateBirth = str(input("Ваш день рождения - "))
     status = "user"
     with open("main.csv","a", encoding = "utf-8", newline = "\n") as f:
        newUser = [login,password,name,dateBirth,status ] 
        writer = csv.writer(f)
        writer.writerow(newUser)

# print ("Вы админ?")        
# userRegistr = input("1- да. 2 - нет.") 
# if userRegistr == "1":
#      print(allUsers)    
# if userRegistr == "2":
#      for user in allUsers:
#            if user [0] == login:
#                 if user[1] == password :
#                     print(user[2],user[3],user[4])       