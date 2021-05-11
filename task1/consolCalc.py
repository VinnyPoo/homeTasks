# Консольный калькулятор

import myIO

# main
whatDo = input('Что делаем + - * / ')
if (whatDo == "+") or (whatDo == "-") or (whatDo == "*") or (whatDo == "/"):
    
    number1 = myIO.inpNum ('Введите первое число ')
    number2 = myIO.inpNum ('Введите второе число ')
    
    if whatDo == "+":
        result = number1 + number2

    elif whatDo == "-":
        result = number1 - number2

    elif whatDo == "*":
        result = number1 * number2

    elif whatDo == "/":
        try:
            result = number1 / number2
        except ZeroDivisionError:
            print('Делить на ноль нельзя')
            result = 1e308

    print('Результат : ' + str(result))

else:
    print('Неверный символ операции : ' + whatDo + ' допустимы только + - * / ')