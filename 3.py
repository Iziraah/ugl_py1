# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
#  from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)

count = 0
while count<11:
    your_num = int(input('Какое число я загадал?.'))
    if your_num > num:
        print('меньше')
    if your_num < num:
        print('больше')
    if your_num == num:
        print('Угадал!..=)')
        quit()
else: 
    print('У тебя закончились попытки..')
    quit()
