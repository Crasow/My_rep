"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
try:
    a = eval("b'функция'")
    b = b'attribute'
    d = b'type'
except SyntaxError:
    print('You got SYNTAX ERROR, lol')

try:
    c = bytes('класс', encoding='ascii')
except UnicodeEncodeError:
    print('You got UNICODE ENCODE ERROR, lol')
"""
В байты нельзя перевести содержимое любой строки, что содержит
один или более не ASCII символ с помощью конструкции b'*'
"""
