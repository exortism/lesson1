#############################################################################################
# TASK 2
user_input = int(input("Введите кол-во секунд, для преобразования"))
hours = str(user_input // 3600)
minutes = (user_input // 60)%60
seconds = user_input % 60
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0'+str(seconds)
else:
    seconds = str(seconds)
print(hours+':'+minutes+':'+seconds)
#############################################################################################
