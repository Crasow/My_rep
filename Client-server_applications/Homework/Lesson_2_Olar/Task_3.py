import yaml

message_data = {'recipients': ['Katya', 'NeKatya', 'TochnoKatya'],
                'qty': 3500,
                'costs': {'Katya': '350\u20AC', 'NeKatya': '999\u20AC', 'TochnoKatya': '1\u20AC'}
                # Вставил кодовые точки
                }

with open('file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(message_data, file, allow_unicode=True, default_flow_style=False)

with open('file.yaml', encoding='utf-8') as file:
    # print(yaml.safe_load(file))
    var = yaml.safe_load(file)
    for k, v in var.items():
        print(k, v)
