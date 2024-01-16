def create_div_set(s):
    res = {i for i in range(1, s + 1) if s % i == 0}
    print(f'Множество делителей: {res}')


n = int(input('Введите число: '))
create_div_set(n)
