#############################################################################################
# TASK 6
while True:
    try:
        first_day_distance = int(input('Введите расстояние в км, которое пробежал спотсмен в первый день'))
        required_distance = int(input("Введите интересующую, общую дистанцию, которую пробежит спортсмен за всё время? "
                                      "А я, определю номер дня когда это расстояние будет достигнуто"))
        break
    except ValueError:
        print('Запрашиваемые данные, необходимо ввести числом! Попробуйте снова.')

days = 1
while first_day_distance < required_distance:
    first_day_distance *= 1.1
    days += 1
print(days)
#############################################################################################