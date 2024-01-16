def create_set_without_word(word):
    res = {chr(i) for i in range(97, 123) if chr(i) not in word}
    print(f'Множество букв, которые не входят в строку: {sorted(res)}')


test = input('Введите строку - ').lower()
create_set_without_word(test)
