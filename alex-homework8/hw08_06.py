import pickle
from faker import Faker

fake = Faker()


def create_matrix():
    n = fake.random_element(elements=(2, 3))
    m = fake.random_element(elements=(2, 3))
    test = [[fake.random_digit() for _ in range(n)] for _ in range(m)]
    return test


def valid_matrix(s):
    if len(s) != len(s[0]):
        print('Матрица не квадратная.')
    else:
        check_len_matr(s)


def check_len_matr(r):
    match len(r):
        case 2:
            calculate_determinate_2(r)
        case 3:
            calculate_determinate_3(r)


def calculate_determinate_2(s):
    res = s[0][0] * s[1][1] - s[0][1] * s[1][0]
    print(f'Определитель матрицы = {res}')


def calculate_determinate_3(s):
    res = s[0][0] * s[1][1] * s[2][2] + s[0][1] * s[1][2] * s[2][0] + s[0][2] * s[1][0] * s[2][1] - s[0][0] * \
          s[1][2] * s[2][1] - s[0][1] * s[1][0] * s[2][2] - s[0][2] * s[1][1] * s[2][0]
    print(f'Определитель матрицы = {res}')


with open('matrix.pickle', 'wb') as f:
    pickle.dump(create_matrix(), f)

with open('matrix.pickle', 'rb') as f:
    lst = pickle.load(f)

for row in lst:
    print(*row)
valid_matrix(lst)
# искали определитель только х2 и х3 матриц, для х1 слишком легко, для х4 и выше слишком сложно
