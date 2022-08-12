import json

import rewriter

rewriter.to_utf_8('orders.json')  # Вообще без понятия как мне пришла идея с абсолютным путем


def write_order_to_json():
    with open('orders.json', 'r', encoding='utf-8') as file_to_read:
        data_from_json = json.load(file_to_read)
        for el in data_from_json['orders']:
            print(el)

        data_from_json['orders'].append(
            {'item': input('Item name: '), 'quantity': input('Item q-ty: '),
             'price': input('Item price: '), 'buyer': input('Item buyer: '), 'date': input('Date: ')
             })

        data_to_json = data_from_json
        print(data_to_json)
        with open('orders.json', 'w', encoding='utf-8') as file_to_write:
            json.dump(data_to_json, file_to_write, indent=4, ensure_ascii=False)


write_order_to_json()
