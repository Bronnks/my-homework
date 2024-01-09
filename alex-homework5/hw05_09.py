def from_nrzi_to_int(word):
    word = word.replace('|_', '1')
    word = word.replace('|¯', '1')
    word = word.replace('¯', '0')
    word = word.replace('_', '0')
    word = int(word, 2)
    return word


x1 = '|¯¯|_|¯¯¯¯¯|_|¯|_'
x2 = '|¯¯¯¯¯¯|___|¯|___|¯'
x3 = '|¯|_|¯|______|¯¯|_'
x4 = '|¯|__|¯¯|___|¯|__|¯'
res_sum = from_nrzi_to_int(x1) + from_nrzi_to_int(x2) + from_nrzi_to_int(x3) + from_nrzi_to_int(x4)

print(f'{res_sum}')
print('%s' % res_sum)
print('{0}'.format(res_sum))
