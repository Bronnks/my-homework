from faker import Faker
import json

fake = Faker()


def create_dict():
    test = {}
    for i in range(fake.random_digit()):
        test[fake.random_lowercase_letter()] = fake.random_digit()
    return test


def check_dicts(d1, d2):
    res1, res2, res3, res4 = [], [], [], []
    for k, v in d2.items():
        if k in d1:
            if d1[k] == v:
                res1.append(k)
            else:
                res2.append(k)
        else:
            res3.append(k)
    for k in d1.keys():
        if k not in d2:
            res4.append(k)
    print_res(res1, res2, res3, res4)


def print_res(r1, r2, r3, r4):
    if len(r1) == 0 and len(r2) == 0:
        print('В словарях нет ни одного общего ключа')
    else:
        if r1:
            if len(r1) == 1:
                print(f'Ключ {r1[0]} есть в обоих словарях и его значения равны.', end=' ')
            else:
                print(f'Ключи {', '.join(r1)} есть в обоих словарях и их значения равны.', end=' ')
        if r2:
            if len(r2) == 1:
                print(f'Ключ {r2[0]} есть в обоих словарях, но его значения разные.', end=' ')
            else:
                print(f'Ключи {', '.join(r2)} есть в обоих словарях, но их значения разные.', end=' ')
    if len(r3) == 0 and len(r3) == 0:
        print('В словарях нет отсутствующих ключей')
    else:
        if r3:
            if len(r3) == 1:
                print(f'Ключ {r3[0]} отсутствует в первом словаре.', end=' ')
            else:
                print(f'Ключи {', '.join(r3)} отсутствуют в первом словаре.', end=' ')
        if r4:
            if len(r4) == 1:
                print(f'Ключ {r4[0]} отсутствует во втором словаре.', end=' ')
            else:
                print(f'Ключи {', '.join(r4)} отсутствуют во втором словаре.', end=' ')


with open('first.json', 'w+', encoding="utf-8") as f:
    json.dump(create_dict(), f)
with open('second.json', 'w+', encoding="utf-8") as f:
    json.dump(create_dict(), f)

with open('first.json', encoding="utf-8") as f:
    dct1 = json.load(f)
with open('second.json', encoding="utf-8") as f:
    dct2 = json.load(f)
check_dicts(dct1, dct2)
