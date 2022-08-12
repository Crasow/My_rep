"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""

import chardet


# Функция создает файл программно с другой кодировкой для чистоты эксперемента
def cp_writing():
    with open('test_file.txt', 'w',
              encoding='cp1251') as file_bytes:
        file_bytes.write('сетевое программирование \nсокет \nдекоратор')


def main():
    with open('test_file.txt', 'rb') as file:
        file_bytes = file.read()
        encoding = chardet.detect(file_bytes)['encoding']
        print(f'File encoding is {encoding}')
        decoded = file_bytes.decode(encoding)
        if '\r' in decoded:
            decoded = decoded.replace('\r', '')
        with open('test_file.txt', 'w', encoding='utf-8') as ffile:
            ffile.write(decoded)

    with open('test_file.txt', encoding='utf-8') as file:
        for el in file:
            print(el, end='')


if __name__ == '__main__':
    # cp_writing()
    main()
