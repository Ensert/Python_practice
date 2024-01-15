#Напишіть програму, яка отримує три цілих числа, введені з клавіатури (кожне число вводиться на окремому рядку), і друкує на екрані їх суму, добуток, результат піднесення першого числа до степеня різниці другого і третього чисел.

#a = int(input('enter variable a:'))
#b = int(input('enter variable b:'))
#c = int(input('enter variable c:'))
#print(a + b + c)
#print(a * b * c)
#d = b - c
#print(a ** d)




#Напишіть програму, яка приймає ціле число n і обчислює значення виразу n + nn + nnn.
#def calculate_expression(n):
#    # Перетворюємо n у рядок для зручності обробки
#    n_str = str(n)
#
#    # Обчислюємо значення виразу n + nn + nnn
#    result = n + int(n_str * 2) + int(n_str * 3)
#
#    return result
#
## Введення цілого числа від користувача
#try:
#    n = int(input("Введіть ціле число n: "))
#    result = calculate_expression(n)
#    print(f"Результат виразу {n} + {n}{n} + {n}{n}{n} дорівнює {result}")
#except ValueError:
#    print("Будь ласка, введіть правильне ціле число.")





#Напишіть програму, яка отримує такі дані: ім’я, вік, хобі, введені з клавіатури (вводяться на окремих рядках), і друкує на екрані одним повідомленням повну інформацію на основі введених даних.
#name = input('enter your name: ')
#age = str(input('enter your age: '))
#hobby = input('enter your hobby: ')
#
#print('My name is ' + name + '. I am',  age, 'and my hobby is', hobby + '.')

# Напишіть програму, яка зчитує довжину основи та висоту прямокутного трикутника (цілі числа),
# обчислює площу і друкує її значення на екрані у відформатованому вигляді (два символи після десяткової крапки).
# Кожен параметр вводиться на окремому рядку.
#try:
#    a = int(input(' Введіть довжину основи трикутника (ціле число): '))
#    h = int(input('Введіть висоту трикутника (ціле число): '))
#except ValueError:
#    print('Введіть ціле число')
#s = (a * h) / 2
#formatted_s = '{:.2f}'.format(s)
#print('Площа трикутника', formatted_s)

#Напишіть програму, яка зчитує ціле число, і друкує попереднє та наступне числа відносно введеного.

#try:
#    var = int(input('Введіть ціле число: '))
#    print('The next number for the number ', var, ' is ', var + 1)
#    print('The previous number for the number ', var, ' is ', var -1)
#except ValueError:
#    print('Введіть ціле число')

#Вводиться ціле додатне число. Надрукуйте останню цифру числа.
#try:
#    var = int(input('Введіть ціле додатнє число: '))
#    print('Остання цифра числа ', var, ' це ', var % 10)
#except ValueError:
#    print('ціле сука число додатнє має бути')

# Напишіть програму, яка друкує на екрані наступне повідомлення: Hello, Starlink subscriber!
# Your current balance is 125.56 UAH. Назва стільникової мережі і значення балансу вводиться з клавіатури.

#network = str(input('Enter network name: '))
#balance = str(input('Enter yor balance: '))
#print('Hello, ' + network + ' subscriber! Your current balance is ' + balance + ' UAH')

# Напишіть програму, яка приймає ім’я та прізвище від користувача у різних рядках
# та роздруковує їх у зворотному порядку з пропуском між ними у вітальному повідомленні.

#name = str(input('Enter you name: '))
#surname = str(input('Enter your surname: '))
#print('Hello, ' + surname + ' ' + name)

# Напишіть програму, яка вітає користувача, виводячи слово Hello, введене ім’я і розділові знаки за зразком
# (дивитися приклади вхідних і вихідних даних). Програма повинна зчитувати в рядкову змінну значення і виводити відповідне вітання.
# Зверніть увагу, що після коми повинен обов’язково стояти пропуск, а перед знаком оклику пропуску немає.
# Операцією конкатенації (об’єднанням) рядків (+) користуватися не можна.

#name = str(input('Enter you name: '))
#print('Hello, ', '{}!'.format(name))

#Вводиться ціле невід’ємне число n (n ≤ 100). Виведіть 2n.

#try:
#    var = int(input('Введіть ціле невід\'ємне число: '))
#    if var <= 100:
#        print(2 ** var)
#    if var >= 100:
#        print('Число повинно бути <= 100')
#except ValueError:
#    print(' Ціле невід\'ємне число дибіл')


#Дано двоцифрове число. Знайдіть число десятків у ньому.

#var = int(input('Enter number between 10 and 99: '))
#a = var / 10
#a = int(a)
#print('number of 10 in ', var, ' is ', '{}.'.format(int(a)))

#Напишіть програму для друку чисел, у яких розділювачами груп розрядів (групи по три цифри) є коми.

#var = int(input('Enter number to format: '))
#print('Formated value is: ', '{:,}'.format(var))


# Напишіть програму, яка отримує значення радіуса кола (дробове число) від користувача та обчислює площу круга і довжину колу.
# Виведення результату відбувається з трьома символами після десяткової крапки. Значення числа Пі округлити до сотих.

#import math
#pi = round(math.pi, 2)
#r = float(input('Введіть радіус кола: '))
#A = pi*r ** 2
#P = 2*(pi*r)
#print('Площа кола становить: ', '{:.3f}'.format(A))
#print('Довжина кола становить: ', '{:.3f}'.format(P))
#print(pi)

# Напишіть програму для перетворення висоти (вказується окремо у футах (1 фут = 30,48 см) і дюймах (1 дюйм = 2,54 см) у сантиметри.

#Feet = float(input('Enter your feet value: '))
#Inch = float(input('Enter your Inches value: '))
#h1 = Feet * 30.48
#h2 = Inch * 2.54
#total_h = h1 + h2
#final_h = round(total_h)
#print('Your height is:', '{} сm'.format(final_h))

# Напишіть програму для перетворення відстані (вказана у футах) у дюйми (1 фут = 12 дюймів),
# ярди (1 фут = 0,333333333 ярда) і милі (1 фут = 0,000189393939 милі).
#import sys
#try:
#    Feet = int(input('Введіть значення кількість футів: '))
#except ValueError:
#    print('Потрібно ввести ціле число')
#    sys.exit()
#Feet = float(Feet)
#Inch = Feet * 12
#Inch = int(Inch)
#Yard = Feet * 0.333333333
#Mile = Feet * 0.000189393939
#print('The distance in inches is ', '{:,} inches'.format(int(Inch)))
#print('The distance in yards is ', '{:,.3f} yards'.format(Yard))
#print('The distance in miles is ', '{:,.3f} miles'.format(Mile))


#17 Напишіть програму, щоб отримати ASCII значення введеного з клавіатури символа.
#char = input('enter value: ')
#ascii_code = ord(char)
#print('ASCII code of ', char, ' is ', ascii_code)

# Напишіть програму, щоб вивести символ за введеним ASCII значенням.

#ascii_code = int(input('Enter ASCII value: '))
#char = chr(ascii_code)
#print('Char value of ', ascii_code, ' is ', char)

# Користувач вводить значення чисел a і b з клавіатури.
# Напишіть програму для друку дії додавання і результату обчислення як у вихідних даних.

#import sys
#try:
#    a = float(input('Enter a value: '))
#    b = float(input('Enter b value: '))
#except ValueError:
#    print(' Enter numeric value')
#    sys.exit()
#print('{:,.0f}'.format(a), ' + ', '{:,.0f}'.format(b), ' = ', '{:,.0f}'.format(a + b))

# Напишіть програму, яка зчитує значення двох змінних a і b, потім змінює їх значення місцями
# (тобто в змінній a має бути записано те, що раніше зберігалося в b, а в змінній b записано те, що раніше зберігалося в a).
# Потім виведіть значення змінних. Виконайте подане завдання без використання третьої змінної.
# У якому порядку значення змінних були введені, у тому ж порядку повинні і виводитися.

#a = input('enter a value: ')
#b = a
#a = input('enter b value: ')
#print('\n', a, '\n',  b)

# Напишіть програму для друку дробових чисел у форматі до 2 десяткових знаків.
#var = float(input('Enter numeric value: '))
#print('rounded value is: ', '{:,.2f}'.format(var))

# Напишіть програму для друку цілих чисел з нулями ліворуч, якщо введене число має у своєму записі менше 5 розрядів.

#var = int(input('Enter numeric value: '))
#print(f'{var:05d}')

# Напишіть програму, щоб надрукувати цілі числа із ∗ справа, якщо введене число має у своєму записі менше 7 розрядів.

#var = input('Enter any value')
#print(f'{var:*<7}')

# Напишіть програму для форматування числа з відсотком.

#var = float(input('Enter value: '))
#percentage = f'{var:.2%}'
#print(percentage)

# Напишіть програму, щоб конвертувати усі введені користувачем одиниці часу (дні, години, хвилини, секунди) в загальну кількість секунд.

#import sys
#try:
#    day = int(input('Enter days number: '))
#    hour = int(input('enter hours number: '))
#    minutes = int(input('enter minutes number: '))
#    second = int(input('enter seconds number: '))
#except ValueError:
#    print('Value shold be a positive number!')
#    sys.exit()
#day_sec = day * 24 * 60 * 60
#hour_sec = hour * 60 * 60
#minutes_sec = minutes * 60
#total_sec = day_sec + hour_sec + minutes_sec + second
#print('Total seconds value is: ', total_sec)

# Необхідно певну суму грошей залишити на банківському рахунку, щоб отримувати відсотки по закінченню певного часу.
# Наприклад, через 10 років ви хотіли б отримати 10 000 доларів США на власному рахунку.
# Скільки потрібно внести грошей на депозит сьогодні, щоб це сталося?
# Для розв’язування цієї задачі можна використовувати формулу
# p = f/(1+r)*n, де p - це поточна сума, яку потрібно внести сьогодні,
# f - майбутнє значення, яке ви хочете отримати (у нашому випадку становить 10 000 доларів США),
# r - річна відсоткова ставка, n - кількість років перебування грошей на рахунку.

#f = float(input('Enter the desired future value: ')) #10000
#r = float(input('Enter the annual interest rate: ')) #0.05
#n = float(input('Enter the number of years the money will grow: ')) #10
#p1 = (1 + r) ** n
#p = f/p1
#print('value: ', p)

# Напишіть програму, яка обчислює значення a + aa + aaa + aaaa із заданою цифрою як цілочисельне значення a.
#import sys
#try:
#    a = int(input('enter value of a: '))
#except ValueError:
#    print('enter positive numeric value')
#    sys.exit()
#a = str(a)
#b = a
#b = int(b)
#c = a+a
#c = int(c)
#d = a+a+a
#d= int(d)
#e = a+a+a+a
#e = int(e)
#print(b + c + d + e)

# Вивести на екран три цілих числа в один рядок через пропуск у порядку, зворотному введенню чисел.

#a = input('enter a: ')
#b = input('enter b: ')
#c = input('enter c: ')
#print(f'{c} {b} {a}')

# Обчисліть n181 і виведіть на екран обчислене значення. Значення n - ціле число, яке вводиться з клавіатури.

#import sys
#try:
#    n = int(input('Enter solid positive number value: '))
#    print(n**181)
#except ValueError:
#    print('normal number must be you bitch')
#    sys.exit()

# Дано два цілих додатних числа a і b, які не перевищують 1000. Обчисліть і виведіть гіпотенузу трикутника із заданими катетами.

#import math
#try:
#    while True:
#        a = int(input('enter a (<1000): '))
#        if 0 <= a <= 1000:
#            break
#        else:
#            print('enter correct')
#    while True:
#        b = int(input('enter b (<1000): '))
#        if 0 <= b <= 1000:
#            break
#        else:
#            print('enter correct')
#    g = math.sqrt(a**2+b**2)
#    print('result: ', g)
#except ValueError:
#    print('xuiny vviv')

# Вводяться три додатних числа - довжини сторін трикутника. Обчисліть площу трикутника за формулою Герона.
#import math
#import sys
#try:
#    while True:
#        a = int(input('enter a side size: '))
#        if 0 <= a:
#            break
#        else:
#            print('enter correct value')
#            sys.exit()
#    while True:
#        b = int(input('enter b side size: '))
#        if 0 <= b:
#            break
#        else:
#            print('enter correct value')
#            sys.exit()
#    while True:
#        c = int(input('enter c side size: '))
#        if 0 <= c:
#            break
#        else:
#            print('enter correct value')
#            sys.exit()
#except ValueError:
#    print('xuita')
#    sys.exit()
#s = (a + b + c) / 2
#try_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#print('area is: ', f'{float(try_area):.1f}')

# Напишіть програму, яка виконує усі арифметичні дії і піднесення до степеня з двома змінними a і b в такому порядку:
# додавання, віднімання, множення, ділення, піднесення до степеня.

#a = int(input('a: '))
#b = int(input('b: '))
#print(a + b)
#print(a - b)
#print(a * b)
#print(a/b)
#print(a**b)

# Цілі числа a і b вводяться користувачем.
# Напишіть програму для обчислення значення математичного виразу (45 + a - 11) / (b - 5)3.

#a = int(input('a: '))
#b = int(input('b: '))
#c = (45 + a - 11) / (b - 5)**3
#print(c)

# Напишіть програму, яка обчислює суму, різницю, добуток, частку двох чисел, піднесення до степеня,
# розділяючи результати, записані в один рядок, символом &.

#a = int(input('a: '))
#b = int(input('b: '))
#
#print(f'{a + b}&{a - b}&{a * b }&{a / b:.1f}&{a ** b}')

# Напишіть програму, яка виводить результат ділення цілих змінних a / b і b / a
# з роздільником ∗∗∗ у форматі 9 знакових позицій і 5 знаків після десяткової крапки відповідно.

#a = int(input('a: '))
#b = int(input('b: '))
#print(f'{a / b:*<10.5f}   {b / a:.5f}')

# Напишіть програму для виведення такого повідомлення на екран: Points: 145, 67, 111.
# Довільні цілі числа вводить користувач з клавіатури і їх значення підставляються у повідомлення автоматично.

#a = input('a: ')
#b = input('b: ')
#c = input('c: ')
#print('Points: ', f'{a},', f'{b},', f'{c}.')

#Напишіть програму для перетворення значення введеного користувачем з клавіатури
# (як відомо, вводиться текстовий рядок) у дійсне і ціле число.

#a = input('value: ')
#a = float(a)
#b = int(a)
#
#print(float(a), b)

# Введіть з клавіатури в окремих рядках різні типи величин: ціле число, текстовий рядок, дійсне число.
# Виведіть інформацію про типи введених даних.

#a = int(input('int: '))
#b = str(input('str: '))
#c = float(input('float: '))
#
#print(type(a))
#print(type(b))
#print(type(c))

# Введіть з клавіатури в окремих рядках різні типи величин: ціле число, текстовий рядок, дійсне число.
# Виведіть інформацію про типи введених даних.

#a = int(input('int: '))
#b = int(input('str: '))
#c = int(input('float: '))
#a = float(a)
#b = float(b)
#c = float (c)
#print(f'{a:.3f}\n{b:.3f}\n{c:.3f}')

# Перевірте приналежність до типу int таких величин як ціле число, текстовий рядок, дробове число.

#a = int(input('int: '))
#b = str(input('str: '))
#c = float(input('float: '))
#
#a = isinstance(a, int)
#b = isinstance(b, int)
#c = isinstance(c, int)
#print(a)
#print(b)
#print(c)

# Напишіть програму для друку повідомлення: «Значення змінної назва змінної дорівнює значення змінної, а її тип тип змінної.»
# Значення змінної вводять з клавіатури і у повідомленні виводиться у лапках.

#a = str(input('str: '))
#b = int(input('int: '))
#c = float(input('float: '))
#
#print('Value of a is', f'"{a}",','and its type',type(a))
#print('Value of b is', f'"{b}",','and its type',type(a))
#print('Value of c is', f'"{c}",','and its type',type(a))

# Обчисліть, скільки коштуватиме певний товар в магазині, якщо діє знижка на нього.
# Значення ціни товару і відсоток знижки вводяться в окремих рядках користувачем з клавіатури.

#a = int(input('enter price: '))
#b = float(input('enter discount %: '))
#d = a-(a*b)
#print('price is: ', d)

# Напишіть програму, яка зчитує три цілих числа і виводить найбільше значення з них.
# Не можна користуватися розгалуженнями і циклами.

#a = int(input('a: '))
#b = int(input('b: '))
#c = int(input('c: '))
#
#print(max(a, b, c))

# Визначити, яку платню одержить на фірмі сумісник за виконану роботу, якщо йому нараховано s гривень, а податок становить p.
# Значення платні і податку (у %) вводяться користувачем.

#s = int(input('Enter your sallary amount: '))
#p = float(input('Enter tax amount: '))
#m = s - (s/100) * p
#print('Your total  sallary amount is: ', float(m))

# 50 Троє друзів отримали в кафе рахунок на суму n гривень, який вони вирішили розділити порівну.
# Скільки повинен заплатити кожен з них, якщо чайові складають 10% від суми рахунку?

#import sys
#try:
#    while True:
#        n = float(input('Введіть суму рахунку: '))
#        if 0 <= n:
#            break
#        else:
#            print('Введіть додатнє число: ')
#except ValueError:
#    print('Потрібно ввести число: ')
#    sys.exit()
#a = n / 3
#tip = a * 0.1
#total_pay = a + tip
#print('Сума сплати: ', f'{total_pay:.2f}')

# Дано відстань n в метрах. Знайти кількість повних кілометрів в ній.

#k = int(input('enter m value: '))
#m = k /1000
#m = int(m)
#print('Km amount is: ', m)

# Знайдіть модуль значення y, де y = (a / b)x + (a(x+1)) / (b(x)).

#a = float(input('enter a: '))
#b = float(input('enter b: '))
#x = float(input('enter x: '))
#
#y = (a / b)**x + (a**(x+1)) / (b**x)
#y = abs(y)
#print(f'{y:.1f}')

# В магазині канцелярських товарів Дарина купила a олівців, b ручок та c фломастерів.
# Відомо, що ціна ручки на 2 гривні більша ціни на олівець і на 7 гривень менша ціни на фломастера.
# Так само відомо, що вартість олівця становить d гривень. Користувачем вводяться по порядку в окремих рядках кількість олівців,
# ручок, фломастерів і ціна одного олівця. Необхідно обчислити загальну вартість покупки.

#a = int(input('enter pencil amount: '))
#b = int(input('enter pen amount: '))
#c = int(input('enter marker amount: '))
#d = int(input('enter pencil price: '))
#pen_price = d + 2
#marker_price = pen_price + 7
#total_pencil_price = a * d
#total_pen_price = b * pen_price
#total_marker_price = c * marker_price
#purchase_sum = total_pen_price + total_marker_price + total_pencil_price
#print('total price is: ', purchase_sum)

# n студентів беруть k яблук і розподіляють між собою порівну. Решта фруктів залишається в кошику.
# Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
# Програма зчитує числа n і k і друкує на екрані дві відповіді на поставлені вище запитання.

#n = int(input('Введіть кількість судентів: '))
#k = int(input('Введіть кількість фруктів: '))
#on_hand, inside = divmod(k, n)
#print('Кожен студетн отримає', f'{on_hand} яблук(а)')
#print('В корзині залишиться', f'{inside} яблук(а)')

# Дано натуральне число.
# Знайдіть цифру, що стоїть в розряді десятків в десятковому записі числа (друга цифра, якщо рахувати з кінця запису).

#n = int(input('enere value: '))
#n = (n // 10) % 10
#print(n)

# Мама спекла пиріг з яблуками, в якому було 60% яблук, а решта - тісто. При цьому 30% тіста становили яйця і цукор, решта - борошно.
# Вся маса пирога дорівнює m кг. Яка маса борошна в пирозі в грамах?

#pie_m = float(input('enter pie weight in kg: '))
#apple_piece = (pie_m / 100) * 60
#pie_m = pie_m - apple_piece
#other = (pie_m / 100) * 30
#pie_m = (pie_m - other) * 1000
#print('pie mass in grams is: ', f'{pie_m:.1f}')

# Знайти кількість відрізків b, розміщених на відрізку a, і довжину незайнятої частини на відрізку a.
# Користувачем вводиться довжина відрізка a, а потім довжина відрізка b на окремих рядках.
# Відповідь виводиться в одному рядку: кількість відрізків b і довжина незайнятої частини відрізка a.

#a = int(input('enter a value: '))
#b = int(input('enter b value: '))
#left_a = (a % b)
#b_in_a = a / b
#print(int(b_in_a), left_a)

# Вводиться додатне ціле трицифрове число. Знайти суму цифр числа.

#a = int(input('enter value: '))
#b = (a // 10) % 10
#c = (a % 10)
#d = (a / 100) % 10
#d = int(d)
#res = b + c + d
#print(res)

# Тетяна кожен день лягає спати рівно опівночі і нещодавно дізналась, що оптимальний час для її сну становить t хвилин.
# Тетяна хоче поставити собі будильник так, щоб він продзвенів рівно через t хвилин після півночі,
# однак для цього необхідно вказати час сигналу у форматі години і хвилини. Допоможіть Тані визначити, на який час завести будильник.
# Години і хвилини у виведенні програми повинні розташовуватися на різних рядках.
#t = int(input('enter time in minutes: '))
#h = t / 60
#m = t % 60
#h = int(h)
#print(' time in hours is: ', f'\n {h} hours \n {m} minutes')

# Напишіть програму для перетворення введених секунд у кількість днів, годин, хвилин та секунд.

#s = int(input('Enter amount of saeconds: '))
#day = s / 86400
#day = int(day)
#s_left = s % 86400
#hour = s_left / 3600
#hour = int(hour)
#s_left = s_left % 3600
#minute = s_left / 60
#minute = int(minute)
#s_left = s_left % 60
#print(f'{day} day(s), {hour} hour(s), {minute} minutes, {s_left} second(s).')

# Враховуючи ціле число n - кількість хвилин, що пройшли з опівночі, - скільки годин і хвилин відображаються
# на екрані 24-годинного цифрового годинника?
# Програма повинна друкувати два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59).
# Наприклад, якщо n = 150, то після опівночі пройшло 150 хвилин, тобто зараз 2:30 ранку. Так що програма повинна друкувати 2 30.

#from datetime import datetime, timedelta
#m_pass = int(input("enter amount of minutes passed: "))
#time_mid = datetime(year=2023, month=12, day=18, hour=00, minute=00)
#m_pass = int(input('Enter passed mins amount: '))
#h_pass = m_pass / 60
#h_pass = int(h_pass)
#m_pass = m_pass % 60
#new_time = time_mid + timedelta(hours=h_pass, minutes=m_pass)
#print('Time passed is:', f'{new_time:%H:%M}')

# Вводиться додатне дійсне число, надрукуйте його дробову частину.

#var = float(input('enter value: '))
#var_f = var % 1
#print(round(var_f, 7))

# Автомобіль може проїхати відстань n кілометрів за день.
# Скільки днів пройде для проїзду маршруту довжиною m кілометрів? Програма отримує два цілих додатних числа: n і m.

#n = float(input('enter car km performance value: '))
#m = float(input('enter km value: '))
#d = m / n
#d_left = m % n
#if d_left > 1:
#    d = d + 1
#if d < 0:
#    d = d + 1
#print(f'you need {int(d)} days to pass the distance')
# or
#import math
#n = float(input('enter car km performance value: '))
#m = float(input('enter km value: '))
#d = math.ceil(m/n)
#print(f'you need {d} days to pass the distance')

# Вводиться число n, необхідно «відрізати« від нього k останніх цифр. Наприклад, при n = 123456 і k = 3 відповідь повинна бути 123.

#n = int(input('enter value: '))
#k = 3
#res = n // 10**k
#print(res)

# Книга коштує a гривень і b копійок. Визначте, скільки гривень і копійок потрібно заплатити за n книг.
# Значення вводяться користувачем у порядку a, b, n на окремих рядках, а сума до сплати в одному рядку через пропуск: кількість гривень і копійок відповідно.

#grn_price = int(input('enter amount of ghryvnya: '))
#kop_price = int(input('enter amount of kopiyka: '))
#book_amount = int(input('enter books amount: '))
#kop_amount = kop_price * book_amount
#kop_left = kop_amount % 100
#grn_from_kop = kop_amount / 100
#grn_from_kop = int(grn_from_kop)
#grn_amount = grn_price * book_amount + grn_from_kop
#print(grn_amount, kop_left)
# or
#grn_price = int(input('enter amount of ghryvnya: '))
#kop_price = int(input('enter amount of kopiyka: '))
#book_amount = int(input('enter books amount: '))
#total_price_kop = (grn_price * book_amount *100) + (kop_price * book_amount)
#grn_total = total_price_kop / 100
#grn_total = int(grn_total)
#kop_total = total_price_kop % 100
#print(grn_total, kop_total)

# Вводиться цифра 0 або 1, необхідно вивести 1 або 0 відповідно, не використовуючи конструкцію розгалуження.

#n = int(input('input: '))
#a = 1
#res = a -n
#print(res)

# Задане число n записали 100 разів поспіль і потім піднесли до квадрату. Що вийшло?
# Зчитування числа n від користувача
#n = input("Введіть число n: ")
## Створення рядку, в якому n повторюється 100 разів
#repeated_string = n * 100
## Піднесення рядку до квадрату
#result = int(repeated_string) ** 2
## Виведення результату
#print("Результат:", result)

# Напишіть програму сумування перших n натуральних чисел. Результатом має бути ціле число.

#n = int(input('enter amount of natural numbers to sum'))
#n_sum = 0
#for i in range(1, n + 1):
#    n_sum = n_sum + i
#print(n_sum)

# Напишіть програму для обчислення координат середини відрізка.

#x1 = int(input('enter x1:'))
#y1 = int(input('enter y1:'))
#x2 = int(input('enter x2:'))
#y2 = int(input('enter y2:'))

#mid_x = (x1 + x2)/2
#mid_y = (y1 +y2)/2

#print(f'The midpoint\'s x value is: {mid_x} \nThe midpoint\'s y value is: {mid_y}')

# Напишіть програму, щоб перетворити ціле число в бінарне (двійкове). Передбачте зберігання провідних нулів у двійковому записі.

#dec = int(input('enterd decimal value: '))
#bin_c = bin(dec)[2:].zfill(8)
#print(bin_c)

# Напишіть програму для перетворення десяткового числа у шістнадцяткове.

#dec = int(input('enterd decimal value: '))
#hex_c = hex(dec)[2:]
#print(hex_c)

# Число n**10 записали чотири рази поспіль, де n - ціле число, яке вводить користувач. З числа, що вийшло, обчислили корінь степеня 10. Скільки вийшло?

#n = int(input('enter n: '))
#n = n ** 10
#repeated_n = int(str(n) * 4) # перетворюємо в натуральне число стрінгу помножену на 4
#res = repeated_n ** (1/10)
#print(repeated_n)
#print(res)

# За правилами числа округлюються до найближчого цілого числа, а якщо дробова частина числа дорівнює 0.5, то число округляється вгору.
# Дано невід’ємне число a, яке необхідно округлити за цими правилами. Зверніть увагу, що функція round() не годиться для цього завдання!
# Використовувати розгалуження, цикли, математичний модуль math не можна.

#var = float(input('enter number: '))
#var_d = var % int(var)
#var = var_d + var
#var = int(var)
#print(var)

# 76 Припустимо, учнівські канікули тривали кілька днів. Напишіть програму, на вхід якої подається кількість днів,
# а на екран виводиться у відформатованому вигляді (вирівнювання за лівим краєм, ширина поля: 10 знаків) загальна тривалість канікул у годинах, хвилинах, секундах.

#n = int(input('enter days amount: '))
#h = n * 24
#m = h * 60
#s = m * 60
#print(f'{h:<10}{'hours':<10}')
#print(f'{m:<10}{'minutes':<10}')
#print(f'{s:<10}{'seconds':<10}')

# Виконайте перетворення значення температури у градусах Цельсія (С) для інших температурних шкал: Фаренгейта (F) і Кельвіна (K).
# Програма повинна відображати еквівалентну температуру у градусах Фаренгейта (F = 32 + 9/5 * C) і у градусах Кельвіна (K = C + 273,15).

#c = int(input('enter celsium value: '))
#f = 32 + 9 / 5 * c
#k = c + float(273.15)
#print(f'{c} Celsius = {f:.3f} Fahrengeit = {k:.3f} Kelvin')

# Отримати реверсний (в зворотному порядку) запис введеного користувачем трицифрового числа.

#n = int(input('enter value: '))
#b = n // 10 % 10
#b = str(b)
#c = n % 10
#c = str(c)
#a = n / 100
#a = int(a)
#a = str(a)
#print(c+b+a)

# Школа вирішила замінити парти у трьох кабінетах. Кожна парта розрахована на двох учнів.
# Враховуючи кількість учнів у кожному класі, надрукуйте найменшу можливу кількість парт, які треба придбати.
# Програма повинна прочитати три цілих числа: кількість учнів в кожному з трьох класів a, b та c відповідно.

#a = int(input('enter pupil amount in a class: '))
#b = int(input('enter pupil amount in b class: '))
#c = int(input('enter pupil amount in c class: '))
#a_d = a / 2
#a_d = int(a_d)
#if a % 2 > 0:
#    a_d = a_d + 1
#b_d = b / 2
#b_d = int(b_d)
#if b % 2 > 0:
#    b_d = b_d + 1
#c_d = c / 2
#c_d = int(c_d)
#if c % 2 > 0:
#    c_d = c_d + 1
#print('Minimum amount of descs to purchase is: ', a_d + b_d + c_d)

# Дано п’ятизначне десяткове число. Побудуйте нове десяткове число за наступними правилами.
# Необхідно обчислити два числа, з яких перше - це сума першої, третьої та п’ятої цифр і друге число - це сума другої і четвертої цифр введеного числа.
# Відповідь - це отримані два числа, які записуються один за одним в одному рядку.

#n = int(input('enter 5 digits: '))
#fst = n / 10000
#fst = int(fst)
#scnd = n / 1000 % 10
#scnd = int(scnd)
#thrd = n / 100 % 10
#thrd = int(thrd)
#frth = n / 10 % 10
#frth = int(frth)
#fith = n % 10
#
#f_to_print = fst + thrd + fith
#s_to_print = scnd + frth
#f_to_print = str(f_to_print)
#s_to_print = str(s_to_print)
#print(f_to_print + s_to_print)

# Дано ціле число n. Виведіть наступне за ним парне число.
# var = int(input('enter number: '))
# if var % 2 != 0:
#     var = var + 1
# else:
#     var = var + 2
# print(var)

# Електронний годинник показує час в форматі h: mm: ss, тобто спочатку записується кількість годин (число від 0 до 23, потім обов’язково двозначна кількість хвилин, потім обов’язково двозначна кількість секунд.
# Кількість хвилин і секунд при необхідності доповнюються до двозначного числа нулями. З початку доби минуло n секунд. Виведіть, що покаже годинник.

#from datetime import datetime, timedelta
#time = datetime(year=2023, month=12, day=19, hour=00, minute=00)
#sec = int(input('enter the seconds amount: '))
#hour = sec / 60 / 60
#hour = int(hour)
#h_without_day = hour % 24
#sec = sec - (hour * 60 * 60)
#minute = sec / 60
#minute = int(minute)
#sec = sec - minute * 60
#sec = round(sec, 2)
#new_time = time + timedelta(hours=h_without_day, minutes= minute, seconds=sec)
#print(f'{new_time:%H:%M:%S}')

# Дано два моменти часу в межах однієї доби. Для кожного моменту вказано години, хвилини і секунди.
# Відомо, що другий момент часу настав не раніше першого. Визначте скільки секунд пройшло між двома моментами часу.
# Програма на вхід отримує шість цілих чисел в окремих рядках. Перші три цілих числа відповідають годинам, хвилинам і секундам першого моменту, наступні три числа відповідають другому моменту.
# Години задаються числом від 0 до 23 включно. Хвилини і секунди - від 0 до 59.

from datetime import datetime, timedelta
import sys

#while True:
#    h_st = int(input('Enter hours amount: '))
#    if h_st in range(0, 23):
#        h_st = h_st
#        break
#    else:
#        print("enter valuse between 0 and 23!")
#        sys.exit()
#while True:
#    m_st = int(input('Enter min amount: '))
#    if m_st in range(0, 23):
#        m_st = m_st
#        break
#    else:
#        print("enter valuse between 0 and 59!")
#        sys.exit()
#while True:
#    s_st = int(input('Enter seconds amount: '))
#    if s_st in range(0, 23):
#        s_st = s_st
#        break
#    else:
#        print("enter valuse between 0 and 59!")
#        sys.exit()
#while True:
#    h_nd = int(input('Enter hours amount: '))
#    if h_nd in range(0, 23):
#        h_nd = h_nd
#        break
#    else:
#        print("enter valuse between 0 and 23!")
#        sys.exit()
#while True:
#    m_nd = int(input('Enter min amount: '))
#    if m_nd in range(0, 23):
#        m_nd = m_nd
#        break
#    else:
#        print("enter valuse between 0 and 59!")
#        sys.exit()
#while True:
#    s_nd = int(input('Enter seconds amount: '))
#    if s_nd in range(0, 23):
#        s_nd = s_nd
#        break
#    else:
#        print("enter valuse between 0 and 59!")
#        sys.exit()
#time_st = datetime(year=2023, month=12, day=19, hour=h_st, minute=m_st, second=s_st)
#time_nd = datetime(year=2023, month=12, day=19, hour=h_nd, minute=m_nd, second=s_nd)
#time_res = time_nd - time_st
#time_in_sec = (h_nd - h_st) * 60 *60 + (m_nd - m_st) * 60 + (s_nd - s_st)
#print(time_res, time_in_sec)

# Равлик повзе по вертикальній жердині висотою h метрів, піднімаючись за день на a метрів, а за ніч спускаючись на b метрів.
# На який день равлик доповзе до вершини жердини? Дані вводяться у порядку h, a, b.

#def days_to_reach_top(h, a, b):
#    days = (h - b - 1) // (a - b) + 1
#    return days
#
## Зчитуємо введені дані
#h = int(input("Висота жердини, h: "))
#a = int(input("Піднімається за день на, a: "))
#b = int(input("Спускається за ніч на, b: "))
#
## Виводимо результат
#result = days_to_reach_top(h, a, b)
#print("Равлик доповзе до вершини жердини на день:", result)

# 87 У цьому завданні необхідно перевірити, чи ділиться число a на число b без остачі і вивести YES або NO.
# Використовувати можна тільки арифметичні операції, використання будь-яких видів розгалужень, функцій заборонено.

# a = int(input('enter a value: '))
# b = int(input('enter b value: '))
# res = (a % b) * 100
# res = str(res)
# y = 'YES'
# n = 'NO00' + res
# print(max(n, y))











