words_lst = ['разработка', 'администрирование', 'protocol', 'standard']
byte_lst = []
result_lst = []

for el in words_lst:
    byte_lst.append(el.encode('utf-8'))
print(byte_lst)

for el in byte_lst:
    result_lst.append(el.decode('utf-8'))
print(result_lst)
