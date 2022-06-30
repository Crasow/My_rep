# Калькулятор
import colorama
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.BLACK)
print(Back.RED)

what = input("Что делаем? (+, -): ")

print(Back.CYAN)

a = float(input("Первое число: "))
b = float(input("Второе число: "))

print(Back.YELLOW)

if what == "+":
    с = a + b
    print("Ответ: ", str(c))
elif what == "-":
    с = a - b
    print("Ответ: " + str(c))
else:
    print("Че? Дурак что-ли?")
input()
