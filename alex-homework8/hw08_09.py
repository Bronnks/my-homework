from faker import Faker

fake = Faker()


def create_requests():
    request = [fake.date_this_month(), fake.time(), fake.ipv4_public(), fake.http_method(),
               fake.random_element(elements=('index.html', 'login.php', 'upload.php')),
               fake.random_int(min=100, max=599), fake.random_int(min=0, max=2048)]
    res = ''
    for c in request:
        res += str(c) + ' '
    return res.strip(' ') + '\n'


count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# счетчик, где индекс соответствует своему счетчику
# 0/1   = ind get+/- | 2/3   = ind post +/- | 4/5   = ind put +/-
# 6/7   = log get+/- | 8/9   = log post +/- | 10/11 = log put +/-
# 12/13 = upl get+/- | 14/15 = upl post +/- | 16/17 = upl put +/-

def change_count(n):  # меняем счетчик
    global count
    count[n] += 1
    return count


def check_req(n, m):  # проверяем успешные и не успешные запросы
    if 200 <= n <= 399:
        change_count(0 + m)
    elif 400 <= n:
        change_count(1 + m)


def count_index(s: list):
    x = int(s[5])
    match s[4]:
        case 'index.html':
            match s[3]:
                case 'GET':
                    check_req(x, 0)
                case 'POST':
                    check_req(x, 2)
                case 'PUT':
                    check_req(x, 4)
        case 'login.php':
            match s[3]:
                case 'GET':
                    check_req(x, 6)
                case 'POST':
                    check_req(x, 8)
                case 'PUT':
                    check_req(x, 10)
        case 'upload.php':
            match s[3]:
                case 'GET':
                    check_req(x, 12)
                case 'POST':
                    check_req(x, 14)
                case 'PUT':
                    check_req(x, 16)


def print_statistics(s):
    print(f'К файлу index.html было {s[0]} положительных GET запросов и {s[1]} отрицательных.')
    print(f'А также {s[2]} положительных POST запросов и {s[3]} отрицательных.')
    print(f'И {s[4]} положительных PUT запросов и {s[5]} отрицательных.')
    print('-' * 70)
    print(f'К файлу login.php было {s[6]} положительных GET запросов и {s[7]} отрицательных.')
    print(f'А также {s[8]} положительных POST запросов и {s[9]} отрицательных.')
    print(f'И {s[10]} положительных PUT запросов и {s[11]} отрицательных.')
    print('-' * 70)
    print(f'К файлу upload.php было {s[12]} положительных GET запросов и {s[13]} отрицательных.')
    print(f'А также {s[14]} положительных POST запросов и {s[15]} отрицательных.')
    print(f'И {s[16]} положительных PUT запросов и {s[17]} отрицательных.')


with open('requests.txt', 'w+', encoding="utf-8") as f:
    for i in range(150):
        f.write(create_requests())

with open('requests.txt', encoding="utf-8") as f:
    for i in f:
        z = i.split()
        count_index(z)
print_statistics(count)
