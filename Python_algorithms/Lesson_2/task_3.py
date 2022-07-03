user_num = input('Ваше число: ')
new_num = ''
for el in range(len(user_num)+1):
    new_num += user_num[-el]
print(new_num[1:])
