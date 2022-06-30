import chardet


def encoding_convert(file_path):  # Путь к файлу в str
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
        encoding = chardet.detect(file_bytes)['encoding']
        # print(encoding)
        decoded = file_bytes.decode(encoding)
        with open(file_path, 'w', encoding='utf-8') as ffile:
            ffile.write(decoded)
