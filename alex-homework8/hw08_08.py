from faker import Faker

fake = Faker()


def create_city_weather():
    city = [fake.city(), fake.random_int(min=-50, max=40), fake.random_int(min=0, max=100),
            fake.random_int(min=850, max=1064), fake.random_int(min=0, max=35), fake.random_int(min=0, max=35)]
    res = ''
    for c in city:
        res += str(c) + ','
    return res.strip(',') + '\n'


with open('citys.txt', 'w+', encoding="utf-8") as f:
    for i in range(100):
        f.write(create_city_weather())

with open('citys.txt', encoding="utf-8") as f:
    x = f.readline().split(',')
    min_weather = int(x[1])
    max_weather = int(x[1])
    city_min_weather = x[0]
    city_max_weather = x[0]
    for i in f:
        x = i.split(',')
        if int(x[1]) < min_weather:
            min_weather, city_min_weather = int(x[1]), x[0]
        elif int(x[1]) > max_weather:
            max_weather, city_max_weather = int(x[1]), x[0]
    print(f'Самая высокая температура в {city_max_weather}, а самая низкая в {city_min_weather}')
