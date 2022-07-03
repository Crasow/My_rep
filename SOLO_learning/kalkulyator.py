# Калькулятор
import colorama
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.BLACK)
print(Back.RED)

what = input("Что делаем? (+, -): ")
if what != '+' and what != '-':
    print('Дурак? Сочувствую(')
    exit()

print(Back.CYAN)

a = float(input("Первое число: "))
b = float(input("Второе число: "))

print(Back.YELLOW)

if what == "+":
    c = a + b
    print("Ответ: ", str(c))
elif what == "-":
    c = a - b
    print("Ответ: " + str(c))

input()
