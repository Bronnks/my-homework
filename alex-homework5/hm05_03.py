lst = input().split('. ')
dct = {}

for i in range(len(lst)):
    res = lst[i].split()
    dct[i+1] = len(res)


for key, value in dct.items():
    # print(f'Sentence {key} has {value} words.', end = ' ')
    print('Sentence {} has {} words.'.format(key, value), end=' ')
    # print('Sentence %s has %s words.' % (key, value), end=' ')
