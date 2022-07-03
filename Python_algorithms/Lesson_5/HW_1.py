ent_num = int(input('Enterprise amount: '))
ent_cash = {}

for el in range(ent_num):
    ent_name = input('Enter enterprise name: ')
    ent_profit = input('Enter enterprise profits through the gap: ').split()
    for ell in range(len(ent_profit)):
        ent_profit[ell] = int(ent_profit[ell])
    avg = sum(ent_profit) / 4
    ent_cash[ent_name] = avg

keys = list(ent_cash.values())

best_avg = keys[0]
for k, v in ent_cash.items():
    if v > best_avg:
        best_avg = v
        best_ent_name = k

print(f'The biggest average {best_avg} profit has enterprise "{best_ent_name}"')

worst_avg = keys[0]
for k, v in ent_cash.items():
    if v < worst_avg:
        worst_avg = v
        worst_ent_name = k

print(f'The smallest average {worst_avg} profit has enterprise "{worst_ent_name}"')
