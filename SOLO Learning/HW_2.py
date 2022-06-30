print ('Заполните, пожалуйста, медицинскую анкету.')
name = input ('Ваше имя:')
surname = input ('Ваша фамилия:')
age = int(input ('Ваш возраст:'))
weight =int (input ('Ваш вес:'))
print (name, surname, age,'год', 'вес:', weight, end ='.')

if age<=30 and (weight>50 or weight<120):
    print ('Не волнуйся,  у тебя все хорошо')
elif age>=30 and age<40 and (weight<50 or weight>120):
    print('Тебе стоит заняться собой')
elif age>=40 and (weight<50 or weight>120):
    print ('Тебе нужен врачебный осмотр')
