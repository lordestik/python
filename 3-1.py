#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div():
    try:
        var1 = float(input('Введите число которое хотите разделить: '))
        var2 = float(input('Введите число на которое хотите поделить: '))
    except (TypeError, ValueError):
        return 'You must use only numbers'
    try:
        div = var1 / var2
    except ZeroDivisionError:
        return 'Division by zero'
    return f'{div:.4f}'

print(div())