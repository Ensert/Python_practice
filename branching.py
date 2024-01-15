# 102 Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача,
# то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..
#import calendar
#import cmath
#pas = str(input("Enter password: "))
#con = 'starlink'
#if pas == con:
#    print('Password accepted')
#else:
#    print('Sorry, that is the wrong password')

# 103 Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.

#word_1 = input('enter first name: ')
#word_2 = input('enter second name: ')
#if word_1 <= word_2:  # порівнюються лексикографічно (за алфавітом)
#    print(f'{word_1}\n{word_2}')
#else:
#    print(f'{word_2}\n{word_1}')

# Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число.
# Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.

#a = int(input('enter a: '))
#if a == 1:
#    print('one')
#elif a == 2:
#    print('two')
#elif a == 3:
#    print('three')
#else:
#    print('unknown')

# Користувач вводить дві різних англійські літери в окремих рядках.
# Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

#str1 = str(input('enter first letter: '))
#str2 = str(input('enter second letter: '))
#if str1 < str2:
#    print(f'{str1} less than {str2}')
#else:
#    print(f'{str1} is not less than {str2}')

# Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?.
# Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..

#c = int(input('inter the temperature value: '))
#if c <= 0:
#    print('A cold, isn’t it?')
#elif 0 < c < 10:
#    print('Cool.')
#else:
#    print('Nice weather we’re having.')

# У чемпіонаті з футболу команді за виграш дається 3 очка, за програш - 0, за нічию - 1.
# Відомо кількість очок, отриманих командою за гру. Вивести результат гри у вигляді відповідних слів: «виграш», «програш» або «нічия».

#p = int(input('enter points: '))
#if p == 3:
#    print('win')
#elif p == 1:
#    print('draw')
#elif p == 0:
#    print('lose')
#else:
#    print('wrong value. You should enter 3 or 1 or 0!')

# Відомі дві швидкості: одна в кілометрах за годину, інша - в метрах за секунду. Яка з швидкостей більше?
#k = int(input('enter km/h value: '))
#m = int(input('enter m/s value: '))
#k_to_m = (k * 1000) / 60 / 60
#if k_to_m > m:
#    print(k)
#else:
#    print(m)

# Дано радіус кола і сторона квадрата (дійсні числа). У якої фігури площа більше?

#import math
#pi = round(math.pi, 2)
#r = float(input('enter circle radius: '))
#p = float(input('enter square side size: '))
#sr = (pi * r) * 2
#sp = p ** 2
#if sr > sp:
#    print('Circle')
#elif sr < sp:
#    print('Square')
#else:
#    print('enter numeric positive value!')

# Дано маси і об’єми двох тіл, виготовлених з різних матеріалів (дійсні числа). Матеріал якого з тіл має більшу густину?
# Введення величин відбувається у такому порядку: m1, v1, m2, v2.

#m1 = float(input('Enter 1st mass value: '))
#v1 = float(input('Enter 1st volume value: '))
#m2 = float(input('Enter 2nd mass value: '))
#v2 = float(input('Enter 2nd volume value: '))
#p1 = m1 / v1
#p2 = m2 / v2
#if p1 > p2:
#    print(f'{p1} is bigger than {p2}')
#elif p1 < p2:
#    print(f' p2 {p2} is bigger than {p1}')
#else:
#    print('error')

# Серед учнів школи проводилося тестування з трьох предметів, по кожному з яких учні отримали певну кількість балів (цілі числа).
# Напишіть програму, яку можуть використати учні для обчислення їхнього середнього балу трьох тестів і виведення середнього значення.
# Окрім того, необхідно передбачити виведення повідомлення Congratulations! That is a great average!, якщо середній бал більший ніж 95.

import sys
#try:
#    a = int(input('enter 1 exam points: '))
#    b = int(input('enter 2 exam points: '))
#    c = int(input('enter 3 exam points: '))
#    zalupa = (a + b + c) / 3
#    if zalupa > 95:
#        print(f'{zalupa:.2f}')
#        print('Congratulations! That is a great average!')
#    else:
#        print(f'{zalupa:.2f}')
#except ValueError:
#    print('tu ragul')

# Напишіть програму, на вхід якої подається два цілих числа - вік Сашка і вік Тетянки. Програма має вивести повідомлення про те, хто є старшим серед них.

#a = int(input('вік сашка: '))
#b = int(input('вік тетянки: '))
#if a > b:
#      print('саша стиарший')
#elif b > a:
#     print('таня старша')
#else:
#     print('lox')

#  Напишіть програму, яка запитує два цілих числа.
#  Якщо добуток чисел перевищує їх суму, надрукувати добуток чисел, у протилежному випадку - вивести їх суму.
#  Якщо добуток дорівнює сумі, вивести різницю чисел.

#a = int(input('enter a: '))
#b = int(input('enter b: '))
#if (a * b) > (a + b):
#    print('добуток= ', a * b)
#elif (a * b) < (a + b):
#    print('сума= ', a + b)
#elif (a * b) == (a + b):
#    print('різниця= ', a - b)
#else:
#    print('error')

# Напишіть програму, щоб перевірити, чи є введене число додатним, від’ємним або це нуль.

# a = float(input('eter value: '))
# if a == 0:
#     print('It is Zero')
# elif a < 0:
#     print('It is a negative number')
# elif 0 <= a:
#     print('It is positive number')

# Напишіть програму, яка зчитує два цілих числа a і b (від 1 до 1000) та виводить найбільше значення з них.

#a = int(input('enter a: '))
#b = int(input('enter b: '))
#if a in range(1, 1001) and b in range(1, 1001):
#    print(max(a, b))
#else:
#    print('value must be in range between 1 and 1000')

# Напишіть програму, яка зчитує два цілих числа a і b (від 1 до 1000) та виводить найбільше значення з них.
#text = input('enter text: ')
#
#if text[0].isupper():
#    print('YES')
#else:
#    print('Yes')

# Дано три цілих числа. Визначте, скільки серед них збігаються.
# Програма повинна вивести одне з чисел: 3 (якщо усі однакові), 2 (якщо два однакові) або 0 (якщо усі числа різні).

# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
# if a == b == c:
#     print('3')
# elif a == b or a == c or b == c or b == a or c == a or c == b:
#     print('2')
# else:
#     print('0')

# Автомобіль подолав відстань s км через населений пункт за t хв. Визначити, чи не порушив водій правил дорожнього руху, якщо швидкість автомобіля при цьому не повинна перевищувати 60 км/год.

# s = int(input('km'))
# t = int(input('m'))
# speed = (s / t) * 60
# if speed > 60:
#     print('Traffic rules are not met.')
# else:
#     print('Traffic rules are executed.')

# a = int(input("Введіть значення для a: "))
# b = int(input("Введіть значення для b: "))
# c = int(input("Введіть значення для c: "))
# d = int(input("Введіть значення для d: "))
# e = int(input("Введіть значення для e: "))
#
# кількість_додатніх = 0
#
# if a > 0:
#     кількість_додатніх += 1
#
# if b > 0:
#     кількість_додатніх += 1
#
# if c > 0:
#     кількість_додатніх += 1
#
# if d > 0:
#     кількість_додатніх += 1
#
# if e > 0:
#     кількість_додатніх += 1
#
# print("Кількість додатніх чисел:", кількість_додатніх)

# Дано ціле число a. Знайти значення виразу: a/(|a|-10). Врахувати у програмі випадок, коли відбувається ділення на нуль.

#try:
#    a = int(input('enter a: '))
#    res = a / (abs(a) - 10)
#    print(res)
#except ZeroDivisionError:
#    print('Division by zero!')

#  Напишіть програму, яка запитує користувача номер в діапазоні від 1 до 7. Програма повинна відображати відповідний день тижня, де 1 - це понеділок, а 7 - неділя.
#  Програма має враховувати варіант, коли користувач вводить номер, що знаходиться за межами діапазону від 1 до 7.

#d = int(input('enter day of the week number: '))
#if d in range(1, 8):
#    if d == 5:
#        print('Friday')
#    elif d == 2:
#        print('Tuesday')
#else:
#    print('There is no such day of the week.')

#  128 Червоний, зелений та синій кольори відомі як основні кольори колірної моделі RGB.
#  При змішуванні червоного та зеленого кольорів, отримується жовтий, при змішуванні синього і зеленого - блакитний, а при змішуванні синього і червоного – пурпуровий колір.
#  Напишіть програму, яка запропонує користувачеві ввести назви двох основних кольорів для змішування. Якщо користувач вводить щось інше, ніж «червоний», «синій» або «зелений»,
#  програма повинна виводити повідомлення про відсутність такої палітри. В іншому випадку програма повинна відображати назву кольору, що утворився.

#a = str(input('Enter first color (Blue, Red, or Green): '))
#b = str(input('Enter second color (Blue, Red, or Green): '))
#a = a.capitalize()
#b = b.capitalize()
#if a == 'Green' or a == 'Blue' or a == 'Red' and b == 'Green' or b == 'Blue' or b == 'Red':
#    try:
#        if a == b:
#            print(a)
#        elif a == 'Blue' and b == 'Red' or b == 'Blue' and a == 'Red':
#            print('Purple')
#        elif a == 'Blue' and b == 'Green' or b == 'Blue' and a == 'Green':
#            print('sky-blue')
#        elif a == 'Red' and b == 'Green' or b == 'Red' and a == 'Green':
#            print('Magenta')
#        else:
#            print('The entered colour should be Red, Green or Blue')
#    except ValueError:
#        print('Error!')
#else:
#    print('no such colour!')

# Книжковий інтернет-магазин має книжковий клуб, який нараховує бали своїм клієнтам на основі кількості книг, що купуються щомісяця (бали можна використати як знижку при черговому придбанні книги).
# Бали нараховуються таким чином: якщо клієнт купує менше 2 книг, він отримує 0 балів; якщо клієнт купує від 2 книг до 4 книг, він отримує 5 балів; якщо клієнт купує від 4 книг і до 6 книг, він заробляє 15 балів;
# якщо клієнт купує від 6 книг до 8 книг, він заробляє 30 балів; якщо клієнт купує 8 і більше книг, він заробляє 60 балів.
# Напишіть програму, яка просить користувача ввести кількість книг, які він придбав у цьому місяці, і відображає кількість отриманих балів.

#import sys
#a = int(input('введіть к-сть придбаних книг: '))
#if 0 <= a < 2:
#    a = 0
#elif 2 <= a < 4:
#    a = 5
#elif 4 <= a < 6:
#    a = 15
#elif 6 <= a < 8:
#    a = 30
#elif a >= 8:
#    a = 60
#else:
#    print('error')
#    sys.exit()
#print(f'You erned {a} points.')

#  Компанія-виробник програмного забезпечення у сфері інформаційної безпеки реалізує один комплект програм за 2700 гривень.
#  Якщо відбувається купівля декількох одиниць товару, працює система знижок: 10-19 одиниць товару - 10%, 20-49 - 20%, 50-99 - 30%, 100 або більше - 40%.
#  Напишіть програму, яка отримує від користувача ціле число - кількість придбаних комплектів програмного забезпечення і виводить повідомлення про суму знижки (якщо така є) та загальну суму при купівлі зі знижкою.

#import sys
#d = 0
#total_price = 0
#try:
#    a = int(input('Enter the amount of purchased goods: '))
#    if a > 0 and a % a == 0:
#        try:
#            if a < 9:
#                d = 0
#            elif 10 <= a <= 19:
#                d = 10
#            elif 20 <= a <= 49:
#                d = 20
#            elif 50 <= a <= 99:
#                d = 30
#            elif a >= 100:
#                d = 40
#            if d > 0:
#                total_price = (a * 2700) * ((100 - d) / 100)
#            if d == 0:
#                total_price = (a * 2700)
#        except ZeroDivisionError:
#            print('error')
#    else:
#        print('Value should be positive!')
#        sys.exit()
#except ValueError:
#    print('Should be positive numeric natural value')
#    sys.exit()
#print(f'The amount of discount is {d}%, total amount of the purchase after the discount is UAH {total_price:.1f}')

# Напишіть програму, на вхід якої подається назва місяця, а програма виводить кількість днів у ньому. Врахуйте те, що місяць «Лютий» може мати 28 або 29 днів.
#def кількість_днів_у_місяці(назва_місяця):
#    # Створення словника, який відображає назви місяців на їхні порядкові номери
#    місяці = {'січень': 1, 'лютий': 2, 'березень': 3, 'квітень': 4, 'травень': 5, 'червень': 6,
#              'липень': 7, 'серпень': 8, 'вересень': 9, 'жовтень': 10, 'листопад': 11, 'грудень': 12}
#
#    # Переведення назви місяця в порядковий номер
#    номер_місяця = місяці.get(назва_місяця.lower())
#
#    if номер_місяця is not None:
#        # Визначення кількості днів у місяці
#        дні_у_місяці = calendar.monthrange(2023, номер_місяця)[1]
#        return дні_у_місяці
#    else:
#        return "Невірна назва місяця"
#
## Введення назви місяця
#назва_місяця = input("Введіть назву місяця: ")
#
## Отримання та виведення результату
#результат = кількість_днів_у_місяці(назва_місяця)
#print(результат)

# Розробіть програму для виведення інформації про операційну систему, яка встановлена на комп’ютері користувачa, при введенні відповідного номера:
# 1 - Window, 2 - Linux, 3 - MacOS. Передбачте у роботі програми ситуації, коли користувач вводить інший номер, відмінний від наведених, або програма на вхід отримує порожній рядок.

#import sys
#try:
#    a = int(input('Enter OS id number: '))
#    if a == 1:
#        print('Windows')
#    elif a == 2:
#        print('Linux')
#    elif a == 3:
#        print('MacOS')
#    else:
#        print('We could not determine your operating system.')
#        sys.exit()
#except ValueError:
#    print('You did not enter a number. Program has completed work.')

# Подорожуючи на автомобілі, ви заїхали на автозаправну станцію. До наступної заправки 200 кілометрів.
# Напишіть програму, яка буде визначати, чи потрібно вам заправлятися або ж можна почекати до наступної станції.
# Програма повинна запитати: який розмір вашого бензобаку в літрах; скільки пального в бензобаку (у відсотках);
# скільки кілометрів проходить автомобіль на одному літрі палива.
# Результатом роботи програми має бути інформація про кількість кілометрів, які ще можна проїхати і почекати до наступної автозаправної станції, або негайно заправитись.

#import sys
#size = int(input('який розмір вашого бензобаку в літрах: '))
#fuel_amount = int(input('скільки пального в бензобаку (у відсотках): '))
#km_per_litre = int(input('кільки кілометрів проходить автомобіль на одному літрі палива: '))
#fuel_amount_left = fuel_amount * size * 0.01
#can_drive = fuel_amount_left * km_per_litre
#print(f'You can drive another {can_drive} kilometers.\nNext refueling after 200 kilometers.')
#if can_drive > 200:
#    sys.exit()
#else:
#    print('FILL IN NOW!')

# Дано натуральне число. Визначити, чи закінчується воно цифрою 5.

# var = int(input('enter value: '))
# var = var % 10
# if var == 5:
#     print('True')
# else:
#     print('False')

# Дано три цілих числа. Необхідно надрукувати ті з них, які є парними.

#var1 = int(input('enter 1st: '))
#var2 = int(input('enter 2nd: '))
#var3 = int(input('enter 3rd: '))
#res1 = var1 % 2
#res2 = var2 % 2
#res3 = var3 % 2
#if res1 == 0:
#    print(var1)
#if res2 == 0:
#    print(var2)
#if res3 == 0:
#    print(var3)

# Перевірити, чи належить число, введене з клавіатури, інтервалу (-5, 3)

#var = int(input('enter value'))
#if -5 <= var <= 3:
#    print('true')
#else:
#    print('false')

# Визначити, чи є число а дільником числа b або, навпаки, число b дільником числа a.

#a = int(input('enter a value'))
#b = int(input('enter b value'))
#
#if a % b == 0 or b % a == 0:
#    print('true')
#else:
#    print('false')

# Перевести число, введене користувачем, у байти або кілобайти в залежності від його вибору.
# Користувач вводить значення у мегабайтах і, відповідно, вводить напрямок переведення: B (у байти) або KB (у кілобайти).

#MB = int(input('enter value: '))
#value = str(input('enter value type to convert: '))
#value = value.lower()
#res = 0
#if value == 'kb':
#    res = MB * 1024
#    print(f'{MB} MB = {res} KB')
#if value == 'b':
#    res = MB * 1024 ** 2
#    print(f'{MB} MB = {res} B')

# На станції ремонту автомобілів працює кілька працівників. Якщо який-небудь працівник працює понад 40 годин на тиждень, він отримує в 1,5 рази більше від звичайної погодинної оплати.
# Розробіть програму, яка розраховує заробітну плату працівника, включаючи оплату за додаткові години. Програма отримує на вхід два цілих числа - кількість робочих годин і ставку погодинної оплати.

# h = int(input('enter hours amount: '))
# m = int(input('enter salary per hour amount: '))
# total = 0
# overtime = 0
# overtime_m = 0
# if h <= 40:
#     total = h * m
# if h > 40:
#     overtime = h - 40
#     overtime_m = m * 1.5
#     total = (40 * m) + (overtime * overtime_m)
# print(total)

#  Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0. Користувач вводить значення коефіцієнтів a, b, c.
#  У вхідних даних наведено три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.

#import math
#a = float(input('enter a value: '))
#b = float(input('enter b value: '))
#c = float(input('enter b value: '))
#delta = (b ** 2) - (4 * a * c)
#if delta > 0:
#    x1 = (-b + math.sqrt(delta)) / (2 * a)
#    x2 = (-b - math.sqrt(delta)) / (2 * a)
#    print(f'{x1:.2f} and {x2:<3.2f}')
#elif delta == 0:
#    x = -b / (2 * a)
#    print(x)
#else:
#    print('No roots.')

# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.
#import math
#x1 = float(input('enter A point x1 value: '))
#y1 = float(input('enter A point y1 value: '))
#x2 = float(input('enter B point x2 value: '))
#y2 = float(input('enter B point y2 value: '))
#x0 = 0
#y0 = 0
#d1 = (x0 - x1) ** 2 + (y0 - y1) ** 2
#d1 = math.sqrt(d1)
#d2 = (x0 - x2) ** 2 + (y0 - y2) ** 2
#d2 = math.sqrt(d2)
#if d1 > d2:
#    print('The A point is farther from zero')
#elif d1 < d2:
#    print('The B point is farther from zero')
#elif d1 == d2:
#    print('The distance is the same')

# Робота світлофора для пішоходів запрограмована таким чином: на початку кожної години протягом трьох хвилин горить зелений сигнал, потім протягом двох хвилин - червоний,
# а потім протягом трьох хвилин - знову зелений і т. д. Дано ціле число t, що означає час в хвилинах, що минув від початку чергової години. Визначити, сигнал якого кольору горить для пішоходів в цей момент.

#t = int(input('Час в хвилинах, що минув від початку чергової години:  '))
#if t > 60:
#    t = t % 60
#if 0 <= t <= 2 or 0 <= t % 5 <= 2:
#    print('Green')
#else:
#    print('Red')

# Робота світлофора для водіїв запрограмована таким чином: на початку кожної години протягом трьох хвилин горить зелений сигнал,
# потім протягом однієї хвилини - жовтий, потім протягом двох хвилин - червоний, а далі протягом трьох хвилин - знову зелений і т. д.
# Дано ціле число t, що позначає час у хвилинах, що минув з початку чергової години. Визначити, сигнал якого кольору горить для водіїв в цей момент.

#t = int(input('Час в хвилинах, що минув від початку чергової години:  '))
#if t > 60:
#    t = t % 60
#if 0 <= t <= 3 or 0 <= t % 6 <= 3:
#    print('Green')
#if t == 4 or t % 6 == 4:
#    print('Yellow')
#if 5 <= t <= 5 or 5 <= t % 6 <= 6:
#    print('Red')

# Дано чотирицифрове число. Перевірте, чи є воно паліндромом. Паліндромом називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
# Наприклад, в нашому випадку, числами-паліндромами будуть: 1221, 4444, 9119 і т. д. Приклади інших цілих чисел-паліндромів, що не відносяться до розв’язуваної задачі: 2, 454, 33, 91219 і т. д.

# var = str(input('enter 4 digit value: '))
#if var == var[::-1]:
#    print('palendrom nax')
#else:
#    print('ne palendrom nax')

# Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.

#var = int(input('enter natural positive number: '))
#a = var % 10
#b = (var // 10) % 10
#c = (var % 1000) // 100
#c = int(c)
#d = var / 1000
#d = int(d)
#if a % 2 == 0:
#    a = '*'
#if b % 2 == 0:
#    b = '*'
#if c % 2 == 0:
#    c = '*'
#if d % 2 == 0:
#    d = '*'
#a=str(a)
#b=str(b)
#c= str(c)
#d= str(d)
#print(d + c + b + a)

# Дано натуральне число n (n ≤ 9999). З’ясувати, чи різні усі чотири цифри цього числа (з урахуванням чотирьох цифр). Наприклад, в числі 5623 усі цифри різні, в числі 0012 - ні.

# var = int(input('enter natural positive number: '))
# a = var % 10
# b = (var // 10) % 10
# c = (var % 1000) // 100
# c = int(c)
# d = var / 1000
# d = int(d)
# if a == b or a == c or a == d or b == c or b == d or c == d:
#     print('true')
# else:
#     print('false')

# Дано однобайтове десяткове число (у межах 128-255).
# Перевірити, чи є двійкове подання десяткового числа паліндромом, з урахуванням зберігання старших нулів у двійковому поданні.
# Приклад таких десяткових чисел: 102 (у двійковому форматі 01100110), 129 (у двійковому вигляді 10000001) і т. д.

# import sys
# dec_var = int(input('enter a number maximum size = 1byte (128 - 255): '))
# if dec_var in range(128, 256):
#     dec_var = bin(dec_var)[2:].zfill(8)
# else:
#     print('enter correct value')
#     sys.exit()
# if dec_var == dec_var[::-1]:
#     print('true', dec_var)
# else:
#     print('false')

# Напишіть програму, у якій користувач вводить значення поточної дати: день, місяць і рік (цілі числа), а програма виводить завтрашню дату у форматі: дд.мм.рррр.

# from datetime import datetime, timedelta
# day = int(input('Enter day: '))
# mon = int(input('Enter month: '))
# year = int(input('Enter year: '))
# time_now = datetime(year=year, month=mon, day=day)
# one_day = timedelta(days=1)
# time_tomorrow = time_now + one_day
# form_time_tomorrow = time_tomorrow.strftime('%d.%m.%Y')
# print(form_time_tomorrow)

# Напишіть програму, у якій користувач вводить значення поточної дати: день, місяць і рік (цілі числа),
# а програма виводить вчорашню дату у форматі: дд.мм.рррр.

# from datetime import datetime, timedelta
# day = int(input('Enter day: '))
# mon = int(input('Enter month: '))
# year = int(input('Enter year: '))
# time_now = datetime(year=year, month=mon, day=day)
# one_day = timedelta(days=1)
# time_tomorrow = time_now - one_day
# form_time_tomorrow = time_tomorrow.strftime('%d.%m.%Y')
# print(form_time_tomorrow)

# Плитка шоколаду має вигляд прямокутника, розділеного на n × m частинок.
# Плитку шоколаду можна один раз розламати по прямій на дві частини. Визначте, чи можна таким чином відламати від плитки шоколаду шматок, що складається рівно з k частин.
# Програма отримує на вхід три числа: n, m, k і повинна вивести Yes або No.

# n = int(input('enter number of pieces horisontal vector: '))
# m = int(input('enter number of pieces vertical vector: '))
# k = int(input('enter number of pieces vafter chocolate cut: '))
# n = n / 2
# m = m / 2
# if n * m == k:
#     print('yes')
# else:
#     print('no')

# Дано три цілих числа. Упорядкуйте їх у порядку зростання. Програма повинна зчитувати три числа a, b, c.
# Далі програма повинна змінювати їх значення так, щоб стали виконані умови a ≤ b ≤ c.
# Резельтатом роботи програми буде виведення трійки чисел a, b, c в одному рядку.
# При розв’язуванні задачі не можна використовувати додаткові змінні, тобто єдиною допустимою операцією присвоювання є обмін значень двох змінних типу (a, b) = (b, a).

# a = int(input('enter A: '))
# b = int(input('enter B: '))
# c = int(input('enter C: '))
# if a < b:
#     (a, b) = (b, a)
# if a < c:
#     (a, c) = (c, a)
# if b < c:
#     (b, c) = (c, b)
# print(c,b,a)

# Визначити максимальну і мінімальну цифри із введеного трицифрового числа і вивести цифри в одному рядку через пропуск.
# Якщо цифри однакові, то вивести лише одну цифру.

# var = int(input('enter value: '))
# var = str(var)
# if max(var) == min(var):
#     print(max(var))
# else:
#     print(max(var), min(var))

# Провайдер здійснює підключення до Інтернету за таким тарифним планом.
# Щомісячна абонентська плата становить a гривень, і в цю абонентську плату включено b гігабайт трафіку. Невитрачені гігабайти в кінці місяця «згорають».
# Якщо трафік перевищує b гігабайт, то кожен гігабайт трафіку понад передплачених коштує с гривень.
# Відомо, що за минулий місяць один з абонентів витратив d гігабайт трафіку.
# Визначте, у скільки обійшовся йому доступ в Інтернет в минулому місяці (вважаючи, в тому числі і абонентську плату)? Вводяться чотири натуральних числа a, b, c, d.
# Всі числа не перевищують 100. Виведіть одне число - суму (у гривнях), яку абонент повинен заплатити за Інтернет.

# mon_charge = int(input('Щомісячна абонентська плата: '))
# gb_limit = int(input('габайт трафіку: '))
# extra_gb_price = int(input('ціна гігабайт трафіку понад передплачених: '))
# gb_spent = int(input('абонентів витратив гігабайт: '))
# extra_gb_amount = gb_spent - gb_limit
# extra_mon_charge = 0
# if gb_limit >= gb_spent:
#     print(f'Pay standart {mon_charge} UAH')
# else:
#     extra_mon_charge = extra_gb_amount * extra_gb_price + mon_charge
#     print(extra_mon_charge)

# Напишіть програму, у якій до введеного числа додаються написи: «гривень» (hryven), «гривня» (hryvnia), «гривні» (hryvni), згідно з правилами українського правопису.

# a = int(input('enter amount: '))
# b = a % 10
# c = 0
# if b == 1:
#     c = 'hryvnia'
# if b in range(5, 10) or b == 0 or a in range(11, 21):
#     c = 'hryven'
# elif b in range(2, 5):
#     c = 'hryvni'
# print(f'{a} {c}')

#

# 190 Напишіть програму, яка отримує на вхід три цілих числа, по одному числу в рядку, і виводить у три рядки спочатку максимальне, потім мінімальне, після чого число, що залишилося.
# Вводитися можуть повторювані числа. Використайте лише конструкції розгалуження, без обміну значеннями між двома змінними.
