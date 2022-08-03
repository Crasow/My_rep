"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess

import chardet

args = ['ping', 'yandex.ru']

ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    var = chardet.detect(line)
    line = line.decode(var['encoding'])
    print(f'{line}')

args = ['ping', 'youtube.com']
ytb_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in ytb_ping.stdout:
    var = chardet.detect(line)
    line = line.decode(var['encoding'])
    print(line)
