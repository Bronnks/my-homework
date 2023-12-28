# в расчет берем данные григорианского календаря

def is_leap_year(year):
    
    match year:
        case year%4 == 0:
            print('Високосный')

        case _:
            print('Не високосный')

x = int(input())
is_leap_year(x)