# Модуль myIO.py

# Функция запроса ввода пользователем числа
# Входной параметр - строка с текстом запроса числа у пользователя
# Возвращает введённое пользователем число
def inpNum (inpString):
    trueFlag = False # False пока от пользователя не будет получено корректное число
    while (trueFlag == False):
        sNumber = input(inpString)
        try:
            inpNumber = float(sNumber)
        except ValueError:
            print('Вы ввели не число')
        else: 
            trueFlag = True
            return inpNumber
