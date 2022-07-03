import csv
import os
import re

path_to_folder = 'Source'  # Легко сделать кастомным с использованием input


def get_data(folder):
    files_list = list(os.walk(folder))
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for el in files_list[0][-1]:
        with open(folder + '/' + el) as file:
            var = file.read()
            var = re.split(':|,|\n', var)
            print (var)
            counter = 0
            for ell in var:
                if ell == 'Изготовитель системы':
                    varr = re.search(r'\b.+\b', var[counter + 1])  # Выбирает из строки предложене без лишних пробелов
                    os_prod_list.append(varr[0])
                    counter += 1
                elif ell == 'Название ОС':
                    varr = re.search(r'\b.+\b', var[counter + 1])
                    os_name_list.append(varr[0])
                    counter += 1
                elif ell == 'Код продукта':
                    varr = re.search(r'\b.+\b', var[counter + 1])
                    os_code_list.append(varr[0])
                    counter += 1
                elif ell == 'Тип системы':
                    varr = re.search(r'\b.+\b', var[counter + 1])
                    os_type_list.append(varr[0])
                    counter += 1
                else:
                    counter += 1
    for el in range(len(os_prod_list)):
        main_data.append([os_prod_list[el], os_name_list[el], os_code_list[el], os_type_list[el]])

    return main_data


def write_to_csv(folder):
    data_to_wrt = get_data(path_to_folder)
    with open('report.csv', 'w', encoding='utf-8') as file:
        file = csv.writer(file)
        for el in data_to_wrt:
            file.writerow(el)


write_to_csv(path_to_folder)
