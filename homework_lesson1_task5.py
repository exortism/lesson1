#############################################################################################
# TASK 5
while True:
    try:
        revenue = int(input('Введите сумму выручки компании'))
        expenses = int(input('Введите сумму издержки'))
        break
    except ValueError:
        print('Запрашиваемые данные, необходимо ввести числом! Попробуйте снова.')
if revenue > expenses:
    print('Компания работает в прибыль')
    profitability = revenue / expenses
    print('Рентабельность компании : ', ("%.2f" % profitability))

else:
    print('Компания работает в убыток')

employees_number = int(input('Введиет количество сотрудников в компании'))
profit_per_employee = revenue / employees_number
print('Прибыль фирмы в расчете на одного сотрудника составляет : ', ("%.2f" % profit_per_employee))

#############################################################################################