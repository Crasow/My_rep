import csv
import os
import re

my_path_to_folder = 'Source'  # Легко сделать кастомным с использованием input


def get_data(folder):
    files_list = list(os.walk(folder))
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for el in files_list[0][-1]:
        with open(folder + '/' + el) as file:
            file_data = file.read()
            splited_file_data = re.split(':|\n', file_data)
            for ell in range(len(splited_file_data)):
                if splited_file_data[ell] == 'Изготовитель системы':
                    # Выбирает из следующей строки набор символов без лишних пробелов
                    ready_data = re.search(r'\b.+\b', splited_file_data[ell + 1])
                    os_prod_list.append(ready_data.group())
                elif splited_file_data[ell] == 'Название ОС':
                    ready_data = re.search(r'\b.+\b', splited_file_data[ell + 1])
                    os_name_list.append(ready_data.group())
                elif splited_file_data[ell] == 'Код продукта':
                    ready_data = re.search(r'\b.+\b', splited_file_data[ell + 1])
                    os_code_list.append(ready_data.group())
                elif splited_file_data[ell] == 'Тип системы':
                    ready_data = re.search(r'\b.+\b', splited_file_data[ell + 1])
                    os_type_list.append(ready_data.group())

    for el in range(len(os_prod_list)):
        main_data.append([os_prod_list[el], os_name_list[el], os_code_list[el], os_type_list[el]])
    print(main_data)
    return main_data


def write_to_csv(folder):
    data_to_wrt = get_data(folder)
    with open('report.csv', 'w', encoding='utf-8') as file:
        file = csv.writer(file, lineterminator='\n')  # Исправление
        # По умолчанию lineterminator = '\r\n', что и создавало лишние строки
        for el in data_to_wrt:
            file.writerow(el)


write_to_csv(my_path_to_folder)
