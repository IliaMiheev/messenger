import socket
from IP import IP

# функция которая записывает значение IP в файл IP.py
def zapis(IP):
    with open ('IP.py', 'w', encoding="utf-8") as file:
        word = f'IP = "{IP}"'
        file.write(word)

# функция которая очищает консоль
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

# задаём IP адрес устройства
if IP == '':
    IP = input('Введи IP адрес устройства с которы хочешь начать переписку: ')
    zapis(IP)
else:
    answer = input(f'Использовать прошлый IP адрес ({IP})? Да или нет? ')
    clear_console()
    if answer.lower() == 'нет':
        NowIP = input('Введи новый IP адрес: ')
        zapis(NowIP)

# начинаем выполнять код
clear_console()
print('Здесь тебе будут видны сообщения')
print()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, 8888))
s.listen(5)

while True:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    else:
        while True:
            try:
                result = client.recv(1024)
                if not result:
                    client.close()
                    break
                message = result.decode('utf-8')
                # выключаем отправку сообщения
                if message.lower() == 'выход':
                    client.close()
                    print('--------------------------------------')
                    print('\033[31mСобеседник вышел из чата.\033[0m')
                    s.close()
                    exit()
                # выводим сообщения
                else:
                    print('--------------------------------------')
                    print(message)
            except ConnectionResetError:
                client.close()
                break