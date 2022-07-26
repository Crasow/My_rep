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
    c = bytes('класс', encoding='ascii')
    d = b'type'
except SyntaxError or UnicodeEncodeError:
    print('You have Error, dude')
"""
В байты нельзя перевести содержимое любой строки, что содержит
один или более не ASCII символ
И отловить ошибку нельзя, ибо она возникает при компиляции, еще до запуска кода
"""
