"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

a = b'функция'
b = b'attribute'
c= b'класс'
d = b'type'
"""
В байты нельзя перевести содержимое любой строки, что содержит
один или более не ASCII символ
"""