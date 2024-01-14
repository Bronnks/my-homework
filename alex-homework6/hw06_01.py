def nod(num1, num2):
    match num1, num2:
        case 0, 0:  # когда оба числа 0
            return 0
        case 0, a:  # когда одно из чисел 0
            return abs(a)
        case a, 0:  # когда второе из чисел 0
            return abs(a)
        case _:
            divisors1 = [1, abs(num1)]  # делителем любого числа является 1 и само это число
            for i in range(2, abs(num1) // 2 + 1):  # ищем делители первого числа(до середины), дальше они повторяются
                if num1 % i == 0:
                    divisors1.append(i)

            divisors2 = [1, abs(num2)]  # ищем делители второго
            for i in range(2, abs(num2) // 2 + 1):
                if num2 % i == 0:
                    divisors2.append(i)

            common_divisors = []        # ищем общие делители
            for i in divisors1:
                if i in divisors2:
                    common_divisors.append(i)

            return max(common_divisors)


num1 = int(input('Введите первое число - '))
num2 = int(input('Введите второе число - '))

print(f'Наибольший общий делитель {num1} и {num2} = {nod(num1, num2)}')
