import socket
from IP import IP
def zapis(IP):
    with open ('IP.py', 'w', encoding="utf-8") as file:
        word = f'IP = "{IP}"'
        file.write(word)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if IP == '':
    IP = input('Введи IP адрес устройства которому хочешь отправить датаграмму: ')
    zapis(IP)
else:
    question = input(f'Использовать прошлый IP адрес ({IP})? Да или нет? ')
    if question.lower() == 'нет':
        NowIP = input('Введи IP адрес устройства которому хочешь отправить датаграмму: ')
        answer = input('Запомнить этот IP адрес? Да или нет? ')
        if answer.lower() == 'да':
            zapis(NowIP)

mes = input('Введите свое сообщение: ')
s.sendto(mes.encode(), (IP, 8888))