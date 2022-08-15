import chardet


def to_utf_8(path):
    with open(path, 'rb') as file:
        file_bytes = file.read()
        encoding = chardet.detect(file_bytes)['encoding']
        # print(encoding)
        decoded = file_bytes.decode(encoding)
        with open(path, 'w', encoding='utf-8') as ffile:
            ffile.write(decoded)
