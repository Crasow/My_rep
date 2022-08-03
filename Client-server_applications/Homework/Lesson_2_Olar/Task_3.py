import yaml

message_data = {'recipients': ['Katya', 'NeKatya', 'TochnoKatya'],
                'qty': 3500,
                'costs': {'Katya': '350€', 'NeKatya': '999€', 'TochnoKatya': '1€'}
                }

with open('file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(message_data, file, allow_unicode=True, default_flow_style=False)

with open('file.yaml', encoding='utf-8') as file:
    print(yaml.safe_load(file))
