# file = open('/home/janarbek/Рабочий стол/python/file/text.txt ', 'w')
# print(file.write('nu nichego strashnogo'))
#
# file = open('/home/janarbek/Рабочий стол/python/file/text.txt ', 'r')
# print(file.read())
# file.close()
# file.close()

# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога.
# Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir.
# В итоге у вас на рабочем столе должен появиться файл directories.txt.
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

# new = '''bin@    dev/   lib@    libx32@      mnt/   root/  snap/     sys/  var/
# boot/   etc/   lib32@  lost+found/  opt/   run/   srv/      tmp/
# cdrom/  home/  lib64@  media/       proc/  sbin@  swapfile  usr/'''.split()

# with open(r'/home/janarbek/Рабочий стол/directories.txt', 'w') as files:
#     for i in new:
#         files.write(i + '\n')

# Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.
# with open(r'/home/janarbek/Рабочий стол/users.txt', 'w') as user:
#     login = input('Enter your login: ')
#     passw = input('Enter your password: ')
#     user.write(login + "\n")
#     user.write(passw)
#     user.close()

# Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”,
# то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.
# with open(r'/home/janarbek/Рабочий стол/w.txt', 'w') as w:
#     word = input('Enter word in English --> ')
#     if 'w' in word:
#         print('Да, в тексте есть w')
#     else:
#         print('Нет, в тексте нет w')

# Создайте текстовый файл python.txt и запишите в него текст #1:
# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
# выведите на экран все полученные слова. Подсказка: используйте for.

# t_words = []
#
# with open(r'/home/janarbek/Рабочий стол/python.txt', 'r') as py:
#     g = py.read().split()
#     for i in g:
#         if 'T' in i or 't' in i:
#             t_words.append(i)
#     print(t_words)

# Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти или зарегистрироваться.
# Спросите его логин и пароль. Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться спросив пароль.
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию.
# Спросите у него Пароль 2 раза и сохраните в файл datebase.txt только если пароли совпадают.

with open(r'/home/janarbek/Рабочий стол/database.txt', 'r') as db:
    dict = {}
    for i in db.readlines():
        log_pass = i.split()
        dict[log_pass[0]] = log_pass[1]

    reg_or_sign = input("Выберите действие: \n1.Войти\n2.Зарегимтрироваться")
    if reg_or_sign == '1':
        log = input('enter login: ')
        if log in dict.keys():
            print('Такой пользователь уже зарегистрирован!')



    print(dict)
    # if reg_or_sign == '1':

    # spi = db.read().split()
    # log = input('Enter login: ')
    # if log in spi:
    #     print('Beatifull')
    # else:
    #     print('Netu ai')
    #     password = input('Enter password: ')

