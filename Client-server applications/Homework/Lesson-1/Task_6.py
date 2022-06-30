import chardet

with open('test_file.txt', 'w',
          encoding='cp1251') as file_bytes:  # Специально создаю программно с другой кодировкой для чистоты эксперемента
    file_bytes.write('сетевое программирование сокет декоратор')

with open('test_file.txt', 'rb') as file:
    file_bytes = file.read()
    encoding = chardet.detect(file_bytes)['encoding']
    print(encoding)
    decoded = file_bytes.decode(encoding)
    with open('test_file.txt', 'w', encoding='utf-8') as ffile:
        ffile.write(decoded)

with open('test_file.txt', encoding='utf-8') as file:
    for el in file:
        print(el, end='')
