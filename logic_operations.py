# var_1 = True
var_1 = False

# первый тип логического ветвления
if var_1:
    print("")
    # print("строка с ПРАВДОЙ!")
    # выполнится код той "ветки" которая является "правдой"

if var_1:
    print("строка с ПРАВДОЙ!")
    # выполнится код той "ветки" которая является "правдой"
else:
    print("строка с ЛОЖЬЮ!")
    # выполнится код той "ветки" которая является "ложью"

if var_1:
    print("строка с ПРАВДОЙ!")
    if var_1:
        print("")
        # print("строка с ПРАВДОЙ!")
        # выполнится код той "ветки" которая является "правдой"
    # выполнится код той "ветки" которая является "правдой"
else:
    print("строка с ЛОЖЬЮ!")
    # выполнится код той "ветки" которая является "ложью"

print('тут происходит разделение')

var_2 = -13  # все числа, кроме нуля = это правда
var_3 = 0.1  # все числа, кроме нуля = это правда
var_4 = ['']  # все, кроме пустого массива - правда
var_5 = '1'  # все, кроме пустого массива - правда

if var_5:
    print("строка с ПРАВДОЙ!")
    # выполнится код той "ветки" которая является "правдой"
else:
    print("строка с ЛОЖЬЮ!")
    # выполнится код той "ветки" которая является "ложью"

print('тут происходит разделение 2')

var_12 = -13
var_13 = -13.01

print(var_12 == var_13)  # оператор сравнения
print(var_12 != var_13)  # оператор сравнения
print(var_12 > var_13)  # оператор сравнения
print(var_12 >= var_13)  # оператор сравнения
print(var_12 < var_13)  # оператор сравнения
print(var_12 <= var_13)  # оператор сравнения