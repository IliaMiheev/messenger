import socket
from IP import IP

# поднимаем регист после точки
def capitalize_after_dot(string):
    words = string.split('. ')
    new_string = []
    
    for word in words:
        if word:
            new_word = word[0].upper() + word[1:]
            new_string.append(new_word)
    return '. '.join(new_string)

# поднимаем регист после пробела
def capitalize_after_space(word):
    word = word.replace(".", ". ")
    word = " ".join(word.replace(" ", " ").split())
    word = word.replace(' .', '.')
    word = capitalize_after_dot(word)

    if word[-1] == ".":
        word = word[0].upper() + word[1:]
    else:
        word = word[0].upper() + word[1:] + "."
    return word

# функция которая записывает значение IP в файл IP.py
def zapis(IP):
    with open ('IP.py', 'w', encoding="utf-8") as file:
        word = f'IP = "{IP}"'
        file.write(word)

# функция для очистки консоли
def clear_console():
    import os
    operating_system = os.name
    if operating_system == 'posix':
        _ = os.system('clear')
    elif operating_system == 'nt' or operating_system == 'dos':
        _ = os.system('cls')
    else:
        print("Очистка консоли не поддерживается на данной операционной системе.")
clear_console()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # определяем IP адрес устройства
    if IP == '':
        IP = input('Введи IP адрес устройства с которы хочешь начать переписку: ')
        zapis(IP)
    else:
        answer = input(f'Использовать прошлый IP адрес ({IP})? Да или нет? ')
        if answer.lower() == 'нет':
            clear_console()
            NowIP = input('Введи новый IP адрес: ')
            zapis(NowIP)

    # начинаем выполнять код
    s.connect((IP, 8888))
    clear_console()
    print('Первая буква все слов будет в верхнем регистре.')
    print()

    while True:
        # вводим сообщение
        mess = input('Введите свое сообщение: ')
        print('--------------------------------------')
        if mess == 'выход' or mess == 'exit':
            s.send('выход'.encode())
            break
        elif mess == '':
            print('Пустые сообщения отправлять нельзя.')
        else:
            # отправляем сообщение
            mess = mess[0].upper() + mess[1:]
            s.send(mess.encode())
except socket.error as e:
    print('\033[31mСобеседник не включил сервер.\033[0m')
finally:
    s.close()
    print('\033[31mВы вышли из чата.\033[0m')